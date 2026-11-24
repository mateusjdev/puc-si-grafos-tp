"""
Processador de export.geojson para extração de geometrias lineares (LineString / MultiLineString).
Ignora Points, Polygons e exporta para edges.json leve para consumo no front-end.
"""

import json
import os
import sys

INPUT_FILE = "export.geojson"
OUTPUT_FILE = "edges.json"

def process_geojson(input_path: str = INPUT_FILE, output_path: str = OUTPUT_FILE):
    if not os.path.exists(input_path):
        print(f"[ERRO] Arquivo '{input_path}' não encontrado no diretório raiz.")
        print(f"Coloque o seu arquivo '{input_path}' na raiz ou passe o caminho como argumento.")
        return False

    print(f"[INFO] Lendo '{input_path}'...")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    features = []
    if data.get("type") == "FeatureCollection":
        features = data.get("features", [])
    elif data.get("type") == "Feature":
        features = [data]
    elif data.get("type") == "GeometryCollection":
        features = [{"geometry": g} for g in data.get("geometries", [])]
    else:
        print("[AVISO] Formato GeoJSON não usual, tentando ler geometrias diretamente...")
        if "coordinates" in data:
            features = [{"geometry": data}]

    edges = []
    min_lon = float("inf")
    min_lat = float("inf")
    max_lon = float("-inf")
    max_lat = float("-inf")

    def update_bbox(coord):
        nonlocal min_lon, min_lat, max_lon, max_lat
        lon, lat = coord[0], coord[1]
        if lon < min_lon: min_lon = lon
        if lat < min_lat: min_lat = lat
        if lon > max_lon: max_lon = lon
        if lat > max_lat: max_lat = lat

    for feat in features:
        geom = feat.get("geometry")
        if not geom:
            continue

        gtype = geom.get("type")
        coords = geom.get("coordinates")

        if not coords:
            continue

        # Extrai apenas LineString e MultiLineString, ignorando Points e Polygons
        if gtype == "LineString":
            # coords é uma lista de pares [lon, lat]
            if len(coords) >= 2:
                # Arredondamento opcional para 6 casas decimais (~10cm de precisão) para reduzir tamanho do JSON
                clean_line = []
                for pt in coords:
                    clean_pt = [round(pt[0], 6), round(pt[1], 6)]
                    update_bbox(clean_pt)
                    clean_line.append(clean_pt)
                edges.append(clean_line)

        elif gtype == "MultiLineString":
            # coords é uma lista de LineStrings
            for line in coords:
                if len(line) >= 2:
                    clean_line = []
                    for pt in line:
                        clean_pt = [round(pt[0], 6), round(pt[1], 6)]
                        update_bbox(clean_pt)
                        clean_line.append(clean_pt)
                    edges.append(clean_line)

    has_data = len(edges) > 0 and min_lon != float("inf")
    bbox = [min_lon, min_lat, max_lon, max_lat] if has_data else [0, 0, 0, 0]

    output_data = {
        "totalEdges": len(edges),
        "bbox": {
            "minLon": bbox[0],
            "minLat": bbox[1],
            "maxLon": bbox[2],
            "maxLat": bbox[3]
        },
        "edges": edges
    }

    print(f"[INFO] Total de segmentos de vias extraídos: {len(edges)}")
    if has_data:
        print(f"[INFO] Bounding Box: Lon [{bbox[0]:.6f}, {bbox[2]:.6f}], Lat [{bbox[1]:.6f}, {bbox[3]:.6f}]")

    print(f"[INFO] Salvando resultado em '{output_path}'...")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, separators=(",", ":"))

    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"[SUCESSO] '{output_path}' gerado com sucesso ({file_size_kb:.1f} KB).")
    return True

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else INPUT_FILE
    dst = sys.argv[2] if len(sys.argv) > 2 else OUTPUT_FILE
    process_geojson(src, dst)
