"""
Servidor HTTP local simples para a Prova de Conceito (PoC).
- Verifica e processa automaticamente export.geojson caso edges.json não exista.
- Serve os arquivos da aplicação estática (index.html, edges.json).
- Totalmente autocontido, utilizando apenas a biblioteca padrão do Python.
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from process import process_geojson, INPUT_FILE, OUTPUT_FILE

PORT = 8000

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Desabilita cache local durante desenvolvimento para refletir alterações de imediato
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def check_and_prepare_data():
    if not os.path.exists(INPUT_FILE) and not os.path.exists(OUTPUT_FILE):
        if os.path.exists("sample_export.geojson"):
            print("[INFO] 'export.geojson' não encontrado. Usando 'sample_export.geojson' para demonstração.")
            process_geojson("sample_export.geojson", OUTPUT_FILE)
        else:
            print(f"[AVISO] '{INPUT_FILE}' não encontrado. Por favor, coloque seu arquivo na raiz do projeto.")
            return

    # Se export.geojson existe e edges.json não existe ou está desatualizado
    if os.path.exists(INPUT_FILE):
        should_process = False
        if not os.path.exists(OUTPUT_FILE):
            should_process = True
        elif os.path.getmtime(INPUT_FILE) > os.path.getmtime(OUTPUT_FILE):
            print(f"[INFO] '{INPUT_FILE}' foi modificado. Re-processando...")
            should_process = True

        if should_process:
            process_geojson(INPUT_FILE, OUTPUT_FILE)

def run_server(port=PORT):
    check_and_prepare_data()

    handler = CustomHTTPHandler
    
    # Tenta subir na porta configurada ou tenta próximas se estiver ocupada
    current_port = port
    httpd = None
    for attempt in range(5):
        try:
            httpd = socketserver.TCPServer(("", current_port), handler)
            break
        except OSError:
            current_port += 1

    if not httpd:
        print(f"[ERRO] Não foi possível iniciar o servidor nas portas {port}-{current_port-1}.")
        sys.exit(1)

    url = f"http://localhost:{current_port}"
    print("\n" + "="*60)
    print("   PoC: Visualizador de Malha Viária (OSM GeoJSON)")
    print("="*60)
    print(f" Servidor rodando em: {url}")
    print(f" Pressione CTRL+C para encerrar.")
    print("="*60 + "\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[INFO] Servidor finalizado.")
        httpd.server_close()

if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else PORT
    run_server(p)
