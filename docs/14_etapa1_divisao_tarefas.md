### 📋 **Divisão da Etapa 1 em 5 Tarefas de Documentação e UML**

#### **1. Tarefa 1: Descrição do Problema, Mapeamento do GeoJSON e UML do Parser**

* **Integrante:** Member 1
* **Escopo no Documento:**
  * Contextualização do **Tema 2 (Otimização de Rotas Urbanas com Base em Mapas)** e especificação dos dados de entrada (malha viária extraída do OpenStreetMap/GeoJSON).
  * Especificação dos atributos viários a serem processados: `oneway` (sentido das vias), `maxspeed` (velocidade máxima), `highway` (tipo de via) e `lanes` (quantidade de faixas).
* **Modelagem UML Obrigatória:**
  * **Diagrama de Classes UML (Parser):** Modelar a classe `GeoJsonParser`, suas dependências de leitura de arquivos `.geojson`, conversores de geometria (`LineString` para pontos/arestas) e tratamento de exceções de parsing.

#### **2. Tarefa 2: Modelagem Conceitual do Grafo, Planaridade e UML das Entidades**

* **Integrante:** Member 2
* **Escopo no Documento:**
  * Abstração matemática do mapa: cruzamentos/interseções como **Vértices** e vias/ruas como **Arestas** com ponderação dupla (distância em metros e tempo teórico em segundos).
  * Redação da **Justificativa de Modelagem**: fundamentar o uso da **Lista de Adjacência** em vez de Matriz de Adjacência, utilizando a propriedade matemática de planaridade de redes viárias (E = 3V - 6), demonstrando que o grafo é esparso com (E = O(V))).
* **Modelagem UML Obrigatória:**
  * **Diagrama de Classes UML (Estrutura do Grafo):** Modelar com atributos, métodos e visibilidade as classes core: `Grafo`, `Vertice`, `Aresta` e `ListaDeAdjacencia`.

#### **3. Tarefa 3: Especificação Teórica e UML dos Algoritmos (Caminho Mínimo, Conectividade e TSP)**

* **Integrante:** Member 3
* **Escopo no Documento:**
  * Descrição formal e pseudocódigo do algoritmo de **Dijkstra** (algoritmo principal) e do **Bellman-Ford** (algoritmo comparativo de performance).
  * Descrição da verificação prévia de conectividade por **BFS/DFS** para validar se origem e destino pertencem ao mesmo componente conexo.
  * Formulação da estratégia para rotas com múltiplos POIs (> 2 pontos) utilizando a heurística do Vizinho Mais Próximo (*Nearest Neighbor*) sobre os menores caminhos calculados.
* **Modelagem UML Obrigatória:**
  * **Diagrama de Classes UML (Motor de Algoritmos):** Modelar as classes e interfaces `DijkstraSolver`, `BellmanFordSolver`, `BfsDfsConectividade` e `VrpTspOptimizer`.

#### **4. Tarefa 4: Geoprocessamento, Arquitetura de Comunicação e UML da API**

* **Integrante:** Member 4
* **Escopo no Documento:**
  * Especificação da função espacial de proximidade (*Snap to Nearest Node*) via fórmula de Haversine para converter cliques no mapa em vértices válidos do grafo.
  * Arquitetura do sistema: integração entre a aplicação console em C# (servidor Kestrel / Minimal API) e a interface gráfica baseada em Leaflet.js.
  * Especificação dos contratos da API REST (endpoints `GET /api/rota`, parâmetros de entrada e estrutura de resposta em JSON).
* **Modelagem UML Obrigatória:**
  * **Diagrama de Classes UML (API e DTOs):** Modelar as classes `SpatialNearestNodeFinder`, `RouteApiController`, `RouteRequestDTO`, `RouteResultDTO` e `MetricsDTO`.

#### **5. Tarefa 5: Plano de Desenvolvimento, Mapeamento de Métricas e Diagrama de Sequência UML**

* **Integrante:** Member 5
* **Escopo no Documento:**
  * Cronograma do **Plano de Desenvolvimento** dividido nas fases de implementação, integração, testes e escrita do artigo final SBC.
  * Metodologia de medição e benchmarking de desempenho: especificação da coleta de tempo (`Stopwatch`), contagem de vértices explorados e estimativa de memória.
  * Matriz de responsabilidades e estratégia de versionamento via Git para acompanhamento das contribuições individuais.
* **Modelagem UML Obrigatória:**
  * **Diagrama de Sequência UML (Fluxo End-to-End):** Modelar o fluxo completo desde a interação do usuário no Leaflet.js, passagem pelo controller da API C#, localização do vértice mais próximo, checagem de BFS/DFS, cálculo pelo Dijkstra até o retorno e renderização da rota.

---

### 🗺️ **Resumo do Diagrama de Classes UML Unificado**

No documento final da Etapa 1, todas essas classes estarão interligadas no **Diagrama de Classes Geral do Sistema**:

```
[Leaflet.js Frontend] <--- HTTP/JSON ---> [RouteApiController]
                                                 |
         +---------------------------------------+---------------------------------------+
         |                                       |                                       |
[GeoJsonParser]                     [SpatialNearestNodeFinder]                   [RouteResultDTO]
         |                                       |                                       |
         +-------------------+-------------------+-------------------+-------------------+
                             |                                       |
                      [Grafo (C#)] <=================== [ListaDeAdjacencia]
                      /     |     \                             |
             [Vertice]  [Aresta]  [BfsDfsConectividade]      [MetricsDTO]
                                            |
                         +------------------+------------------+
                         |                                     |
                 [DijkstraSolver]                      [BellmanFordSolver]
                         |                                     |
                         +------------------+------------------+
                                            |
                                   [VrpTspOptimizer]
```
