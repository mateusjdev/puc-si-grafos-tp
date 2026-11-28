## MVP

- Estrutura de Grafos do Zero (C#):  
  - Implementar Grafo, Vertice, Aresta e ListaDeAdjacencia sem uso de bibliotecas externas.  
  - Busca e Conectividade: BFS ou DFS para validar se origem e destino estão no mesmo componente conexo antes do roteamento.  
  - Caminho Mínimo Base: Algoritmo de Dijkstra.  
  - Algoritmo Comparativo: Bellman-Ford (para benchmarking no relatório).  
  - Roteamento Multi-Ponto (2 POIs): Otimizador TSP/VRP (Dijkstra + Heurística do Vizinho Mais Próximo).  
- Parser de GeoJSON: Extração de coordenadas e atributos viários: oneway (sentidos de direção), maxspeed (velocidade máxima), highway (tipo de via) e lanes (faixas, se disponível).  
- Ponderação de Arestas: Cálculo e armazenamento de peso por distância física (Haversine em metros) e tempo teórico (Distância, Velocidade).  
- Função Espacial de Proximidade (Snap to Nearest Node): Módulo no backend em C# que recebe uma coordenada GPS (latitude/longitude) clicada no mapa e localiza o vértice do grafo mais próximo.  
- Interface Frontend (Leaflet.js):
  - Captura de clique para definição de 2 ou mais POIs.  
  - Estrutura de camadas (layers) exibindo o mapa base (OpenStreetMap) e a rota otimizada calculada (L.polyline).

## Funcionalidades Futuras

- Chave Seletora de Critério no Frontend: Alternador na interface gráfica para escolher entre Caminho Mais Curto (metros) e Caminho Mais Rápido (tempo).  
- Painel Visual de Métricas de Execução: Exibição gráfica na interface com tempo de processamento (Stopwatch), vértices/arestas explorados e consumo estimado de memória.  
- Algoritmo A: Implementação do A\* com heurística geográfica para ampliação da análise de desempenho no artigo.  
- Pesquisa e Filtros de POIs: Campo de busca por nome ou categoria (Shoppings, Faculdades, Hospitais).  
- Layers Avançadas e Penalidades por Tipo de Via: Filtro visual por hierarquia de vias e aplicação de fatores de preferência/penalidade baseados na tag highway.
