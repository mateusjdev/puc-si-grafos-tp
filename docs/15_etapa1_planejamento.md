# Etapa 1 — Modelagem e Planejamento da Solução

<!-- Identificação do grupo, tema escolhido (Tema 2: Otimização de Rotas Urbanas com Base em Mapas) e link do repositório Git -->

---

## 1. Descrição do Problema e Especificação dos Dados (Tarefa 1 — Member 1)

### 1.1 Contextualização do Problema
<!-- Descreva o contexto do Tema 2 (Otimização de Rotas Urbanas com Base em Mapas), o problema a ser resolvido e os objetivos da solução. -->

### 1.2 Dados de Entrada (OpenStreetMap / GeoJSON)
<!-- Especifique a origem da malha viária (OpenStreetMap/GeoJSON), área geográfica coberta e estrutura esperada dos arquivos de entrada. -->

### 1.3 Atributos Viários Processados
<!-- Detalhe como cada atributo será interpretado no processamento:
- oneway (sentido das vias)
- maxspeed (velocidade máxima)
- highway (tipo de via)
- lanes (quantidade de faixas)
-->

### 1.4 Modelagem UML — Parser (`GeoJsonParser`)
<!-- Insira o Diagrama de Classes UML do Parser (classe GeoJsonParser, dependências de leitura .geojson, conversores de geometria LineString para pontos/arestas e tratamento de exceções). -->

---

## 2. Modelagem Conceitual do Grafo e Justificativa (Tarefa 2 — Member 2)

### 2.1 Abstração Matemática do Mapa
<!-- Descreva a representação: cruzamentos/interseções como Vértices e vias/ruas como Arestas, com ponderação dupla (distância em metros e tempo teórico em segundos). -->

### 2.2 Justificativa da Estrutura de Dados (Lista de Adjacência)
<!-- Fundamente o uso de Lista de Adjacência em vez de Matriz de Adjacência, utilizando a propriedade de planaridade de redes viárias (E = 3V - 6) e demonstrando que o grafo é esparso (E = O(V)). -->

### 2.3 Modelagem UML — Estrutura do Grafo
<!-- Insira o Diagrama de Classes UML das entidades core (Grafo, Vertice, Aresta e ListaDeAdjacencia) com atributos, métodos e visibilidade. -->

---

## 3. Especificação Teórica dos Algoritmos (Tarefa 3 — Member 3)

### 3.1 Caminho Mínimo: Dijkstra e Bellman-Ford
<!-- Apresente a descrição formal, complexidade e pseudocódigo do algoritmo de Dijkstra (principal) e do Bellman-Ford (comparativo de performance). -->

### 3.2 Verificação de Conectividade (BFS / DFS)
<!-- Descreva a verificação prévia de conectividade por BFS/DFS para validar se origem e destino pertencem ao mesmo componente conexo. -->

### 3.3 Rotas com Múltiplos POIs (TSP / VRP)
<!-- Formule a estratégia para rotas com mais de 2 pontos de interesse utilizando a heurística do Vizinho Mais Próximo (Nearest Neighbor) sobre os menores caminhos calculados. -->

### 3.4 Modelagem UML — Motor de Algoritmos
<!-- Insira o Diagrama de Classes UML com as classes e interfaces: DijkstraSolver, BellmanFordSolver, BfsDfsConectividade e VrpTspOptimizer. -->

---

## 4. Geoprocessamento, Arquitetura de Comunicação e API (Tarefa 4 — Member 4)

### 4.1 Função Espacial de Proximidade (*Snap to Nearest Node*)
<!-- Especifique o cálculo via fórmula de Haversine para converter cliques no mapa (latitude/longitude) em vértices válidos do grafo. -->

### 4.2 Arquitetura do Sistema
<!-- Descreva a integração entre o backend em C# (servidor Kestrel / Minimal API) e o frontend em Leaflet.js. -->

### 4.3 Contratos da API REST
<!-- Especifique os endpoints (ex: GET /api/rota), parâmetros de entrada e estrutura de resposta em JSON. -->

### 4.4 Modelagem UML — API e DTOs
<!-- Insira o Diagrama de Classes UML para SpatialNearestNodeFinder, RouteApiController, RouteRequestDTO, RouteResultDTO e MetricsDTO. -->

---

## 5. Plano de Desenvolvimento, Métricas e Fluxo End-to-End (Tarefa 5 — Member 5)

### 5.1 Cronograma e Fases de Desenvolvimento
<!-- Detalhe o cronograma dividido nas fases de implementação, integração, testes e escrita do artigo final SBC. -->

### 5.2 Metodologia de Medição e Benchmarking
<!-- Especifique a coleta de tempo (Stopwatch), contagem de vértices explorados e estimativa de consumo de memória. -->

### 5.3 Matriz de Responsabilidades e Versionamento (Git)
<!-- Defina a matriz de responsabilidades dos integrantes e a estratégia de branches/commits no Git. -->

### 5.4 Modelagem UML — Diagrama de Sequência (Fluxo End-to-End)
<!-- Insira o Diagrama de Sequência UML completo: interação no Leaflet.js -> RouteApiController -> SpatialNearestNodeFinder -> BFS/DFS -> Dijkstra -> retorno e renderização da rota. -->

---

## 6. Diagrama de Classes Geral do Sistema (Unificado)

<!-- Insira o Diagrama de Classes Geral unificando todas as classes das Tarefas 1 a 5 (Leaflet.js Frontend, RouteApiController, GeoJsonParser, SpatialNearestNodeFinder, Grafo, ListaDeAdjacencia, Vertice, Aresta, BfsDfsConectividade, DijkstraSolver, BellmanFordSolver, VrpTspOptimizer, RouteResultDTO, MetricsDTO). -->
