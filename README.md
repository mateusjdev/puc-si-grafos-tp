# Prova de Conceito (PoC): Visualizador de Malha Viária OSM

Esta PoC lê um arquivo GeoJSON do OpenStreetMap (ex: exportado do Overpass Turbo), extrai apenas as vias (`LineString` e `MultiLineString`), descarta pontos e polígonos, e renderiza as arestas em um `<canvas>` HTML5 de tela cheia com fundo branco puro (`#FFFFFF`).

---

## 📁 Estrutura de Arquivos

```text
.
├── export.geojson          # Seu arquivo GeoJSON (coloque aqui na raiz)
├── sample_export.geojson   # Amostra de teste caso export.geojson não exista
├── process.py              # Script extrator de LineStrings -> edges.json
├── server.py               # Servidor HTTP local integrado (Python Standard Library)
├── index.html              # Interface web com Canvas (Pan, Zoom, Projeção BBox)
└── README.md               # Instruções de uso
```

---

## 🚀 Como Executar

### Pré-requisito
- Ter o **Python 3** instalado (nenhuma dependência externa necessária).

### Opção 1: Inicialização em 1 Passo (Recomendado)
Coloque o seu arquivo `export.geojson` na pasta raiz e execute:

```bash
python server.py
```

O script irá:
1. Detectar o `export.geojson` (ou `sample_export.geojson` se não houver).
2. Processar e gerar o arquivo otimizado `edges.json`.
3. Iniciar um servidor HTTP local em `http://localhost:8000`.

Abra o seu navegador em [http://localhost:8000](http://localhost:8000).

---

### Opção 2: Processamento Manual e Qualquer Servidor Estático
Se preferir gerar o arquivo `edges.json` separadamente:

```bash
# 1. Processa o export.geojson e gera o edges.json
python process.py

# 2. Inicia qualquer servidor estático
python -m http.server 8000
```

Abra o navegador em [http://localhost:8000](http://localhost:8000).

---

## 🔍 Funcionalidades Implementadas

- **Filtro Estrito de Geometrias:** Captura somente `LineString` e `MultiLineString`. Geometrias do tipo `Point`, `MultiPoint`, `Polygon` e `MultiPolygon` são descartadas.
- **Fundo Branco Puro:** `<canvas>` com `100vw` x `100vh` e `#FFFFFF`.
- **Projeção e Escala Automática:** Bounding Box calculada com correção longitudinal baseada no cosseno da latitude média (`cos(lat)`), preservando o aspect ratio real e invertendo o eixo Y.
- **Interatividade (Pan & Zoom):**
  - **Pan:** Clique com o botão esquerdo e arraste pelo mapa.
  - **Zoom:** Roda do scroll do mouse (zoom centrado onde o cursor está apontando) ou botões `+` e `-` no painel.
  - **Centralizar Vista:** Botão para resetar a visualização para a bounding box original.
- **Renderização Nítida:** Tratamento para displays High-DPI / Retina (`devicePixelRatio`), com linhas de 1px nítidas (`#111111`).
