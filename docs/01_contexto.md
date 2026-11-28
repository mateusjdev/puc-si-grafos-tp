# Especificação do Projeto de Algoritmos em Grafos

## Objetivo

Desenvolver uma ferramenta computacional para resolver um problema aplicado por meio da modelagem, implementação e análise de grafos. O projeto deve contemplar:

* Definição da estrutura do grafo.
* Implementação de algoritmos compatíveis com o problema escolhido.
* Construção de uma interface de interação com a ferramenta.
* Avaliação dos resultados obtidos, demonstração da correção da solução, análise de complexidade e discussão das limitações no contexto da aplicação.

## Requisitos Técnicos e Restrições

* Linguagem principal: C# para as estruturas de dados e algoritmos em grafos.

* Interface: qualquer linguagem ou framework de front-end pode ser utilizado para a interface gráfica.

* Implementação própria: é proibida a utilização de bibliotecas prontas para a criação e processamento do grafo (como NetworkX), exceto se utilizadas estritamente para comparação de desempenho.

* Bases de dados: utilizar datasets reais (como os disponíveis no Kaggle) para execução e testes do sistema.

* Versionamento: todo o código deve ser versionado em um repositório Git com histórico de commits.

## Temas Sugeridos

1. Segmentação hierárquica de imagens com base em grafos: receber imagens, representá-las por meio de grafos, agrupar pixels ou regiões com características semelhantes e construir uma hierarquia de partições para identificar objetos e estruturas em diferentes níveis de granularidade.

2. Otimização de rotas urbanas com base em mapas: receber mapas com pontos de interesse e calcular rotas otimizadas com base em tempo, distância ou custo.

3. Análise de redes sociais com grafos: construção e visualização de redes sociais com métricas como centralidade, grau, agrupamento e detecção de comunidades.

4. Monitoramento de distribuição de energia ou água: modelagem da rede de distribuição e análise de falhas, gargalos ou rotas alternativas usando grafos.

5. Análise de redes de transporte público: construção de grafos baseados em linhas de ônibus, metrô ou trem, com simulação de trajetos, tempo de espera e eficiência.

6. Detecção de Fraudes em Redes de Transações: modelagem de transações financeiras como grafos dirigidos, com análise de padrões suspeitos, detecção de ciclos e identificação de nós com comportamentos anômalos.

7. Simulador de Epidemias em Redes: representação de uma rede de indivíduos e simulação de propagação de doenças ou informações, permitindo ajustes de parâmetros como taxa de contágio, recuperação e isolamento.

8. Análise de Redes de Colaboração Científica: análise de redes de coautoria acadêmica com foco em identificação de comunidades de pesquisa, autores centrais, áreas de conhecimento conectadas e evolução da rede ao longo do tempo.

9. Gestão de Conflitos em Sistemas de Dependência: modelagem de dependências entre tarefas ou pacotes com detecção de ciclos, visualização de dependências e execução segura baseada em ordenação topológica.

10. Roteamento e Carga de Veículos em Centros Logísticos: criação de um sistema para planejamento de rotas logísticas com restrições de tempo, distância, prioridade e capacidade de carga dos veículos.

## Etapas de Desenvolvimento

### Etapa 1 - Modelagem e Planejamento da Solução

* Atividades: escolha do tema, definição do problema, levantamento de dados e modelagem do grafo utilizando diagramas UML.

* Entregável: documento com a descrição do problema, justificativa da modelagem e plano de desenvolvimento.

### Etapa 2 - Desenvolvimento da Ferramenta

* Atividades: implementação da estrutura de grafos, aplicação dos algoritmos, testes com bases de dados e construção da interface gráfica com exibição dos resultados.

* Entregável: protótipo funcional com código versionado no Git.

### Etapa 3 - Documentação e Finalização

* Atividades: contextualização, consolidação da modelagem, análise dos resultados obtidos, avaliação de desempenho e conclusões.

* Entregáveis:
* Arquivo zip contendo o código-fonte do projeto, o código-fonte do relatório (.tex) e o PDF compilado.

* Repositório Git contendo todo o histórico de desenvolvimento.

## Especificações da Documentação (Relatório Técnico)

* Formato: artigo em LaTeX utilizando o template oficial da SBC ([https://www.overleaf.com/latex/templates/sbc-conferences-template/blbxwjwzdngr](https://www.overleaf.com/latex/templates/sbc-conferences-template/blbxwjwzdngr)).

* Extensão: entre 12 e 15 páginas.

* Conteúdo obrigatório:
* Contextualização da ideia escolhida.

* Apresentação da modelagem proposta e diagramas UML.

* Demonstração de todos os artefatos produzidos, resultados obtidos e telas da interface.

* Análise de complexidade, demonstração da correção da solução, avaliação de desempenho e limitações no contexto da aplicação.

* Descrição das responsabilidades e contribuições técnicas de cada membro no desenvolvimento.
