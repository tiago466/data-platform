# ⚙️ FASE 3 — INGESTÃO DE DADOS (BRONZE / RAW)

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## ✔ TAREFAS DA FASE

- ✅ Analisar procedure legada
- ✅ Identificar fonte OLTP
- ✅ Definir estratégia de extração
- ✅ Criar pipeline de ingestão em Python
- ✅ Persistir dados em Parquet (RAW)
- ✅ Implementar logging de execução

---

## 🎯 OBJETIVO DA FASE

O objetivo desta fase é **implementar um processo de ingestão de dados moderno**, substituindo abordagens legadas e destrutivas (como ETLs em banco de dados relacional) por um pipeline **ELT**, **imutável**, **versionado** e **auditável**, armazenando os dados na **camada RAW (Bronze)** do Data Lake.

Esta fase estabelece a base de todo o ecossistema de dados, garantindo que os dados brutos sejam tratados como **ativos históricos**, preservando rastreabilidade, governança e possibilidade de reprocessamento futuro.

---

## 🧠 CONTEXTO E DECISÕES INICIAIS

### Ausência de procedure legada
Inicialmente, este projeto previa a análise de procedures legadas relacionadas ao domínio de **fluxo operacional**. Contudo, houve uma mudança estratégica de domínio para **mercado financeiro**, onde não existia um processo legado formal.

Portanto, esta fase foi construída **do zero**, permitindo aplicar boas práticas desde o início, sem herdar limitações técnicas anteriores.

---

## 🔌 IDENTIFICAÇÃO DA FONTE DE DADOS (OLTP / ORIGEM)

A fonte de dados escolhida foi o **Yahoo Finance**, acessado via biblioteca `yfinance`.

Características da fonte:
- Dados históricos de ativos financeiros
- Consulta realizada **por ativo**
- Granularidade diária
- Fonte externa (API pública)

Inicialmente, pretendia-se trabalhar com contratos futuros (WIN, WDO). Entretanto, verificou-se que os dados de mercado futuro no Yahoo Finance são inconsistentes e incompletos, o que poderia comprometer análises e modelos de Machine Learning.

### Decisão tomada
Optou-se por trabalhar com **Fundos Imobiliários (FIIs)** negociados na B3, pois:
- Os dados são mais consistentes
- A série histórica é mais estável
- O domínio é mais adequado para análises de longo prazo e recomendação de investimento

---

## 📋 ESTRATÉGIA DE EXTRAÇÃO (METADADOS)

A API do Yahoo Finance exige que as consultas sejam feitas **ativo por ativo**, o que inviabiliza qualquer abordagem manual.

Para resolver esse problema, foi criado um arquivo de metadados: *pipelines/mercado_financeiro/config/ativos.csv*

Este arquivo contém:
- `ticker`: código do ativo (ex: HGLG11.SA)
- `type`: tipo do ativo (ex: fii)
- `effective_date`: data inicial da série histórica

O `ativos.csv` atua como uma **tabela de controle da ingestão**, permitindo:
- Escalabilidade
- Inclusão ou exclusão de ativos sem alterar código
- Reprodutibilidade do pipeline

---

## ⚙️ PIPELINE DE INGESTÃO (PYTHON)

O pipeline de ingestão foi implementado em Python, executado dentro de um container Docker, seguindo o fluxo abaixo:

### Estrutura lógica do pipeline

1. Leitura das variáveis de ambiente:
   - `DATA_LAKE_PATH`

2. Leitura do arquivo de metadados (`ativos.csv`)

3. Configuração do sistema de logging:
   - Logs em arquivo
   - Logs no console
   - Registro de INFO e ERROR

4. Para cada ativo listado:
   - Registrar início da ingestão no log
   - Obter ticker, tipo e data inicial
   - Consultar dados históricos no Yahoo Finance
   - Validar retorno (DataFrame vazio ou não)
   - Enriquecer os dados com colunas de controle:
     - ativo
     - tipo
     - fonte
     - data_ingestao
   - Definir diretório RAW baseado em:
     - domínio
     - fonte
     - tipo
     - ativo
     - data da carga
   - Persistir os dados em formato Parquet
   - Registrar sucesso ou falha no log

O pipeline foi projetado para:
- Não interromper a execução em caso de falha de um ativo
- Garantir observabilidade completa da execução
- Facilitar diagnóstico de problemas de dados ou da fonte externa

---

## 🐳 AMBIENTE DE EXECUÇÃO (DOCKER)

Durante a execução inicial, foi identificado um erro de dependências (`ModuleNotFoundError: pandas`), pois a imagem `python:3.11-slim` não possui bibliotecas de dados instaladas por padrão.

### Solução adotada
- Criação de um `requirements.txt` na raiz do projeto
- Criação de um `Dockerfile` customizado
- Construção de uma imagem própria com:
  - pandas
  - yfinance
  - pyarrow (para Parquet)

Essa decisão garantiu:
- Ambiente reprodutível
- Paridade entre desenvolvimento e execução
- Controle explícito de dependências

---

## 🗄️ PERSISTÊNCIA NA CAMADA RAW (BRONZE)

Os dados foram armazenados seguindo rigorosamente os **princípios fundamentais da camada RAW**:

### Princípios aplicados

1. **RAW é imutável**  
   Dados já carregados nunca são alterados ou apagados.

2. **RAW é append-only**  
   Cada nova execução adiciona dados, sem sobrescrever histórico (exceto reexecuções no mesmo dia).

3. **RAW não possui regra de negócio**  
   Nenhuma transformação, cálculo ou regra analítica é aplicada.

4. **RAW preserva o formato original**  
   Estrutura e valores retornados pela fonte são mantidos.

5. **RAW é particionado por tempo**  
   Utilização do particionamento `dt_carga=YYYY-MM-DD`.

6. **RAW é organizado por domínio e fonte**  
   Estrutura clara e navegável do Data Lake.

### Estrutura resultante

```bash
raw/
└── mercado_financeiro/
  └── yahoo_finance/
    └── tipo=fii/
      └── ativo=HGLG11.SA/
        └── dt_carga=2026-01-10/
          └── hglg11.sa_diario.parquet
```

--- 


Execuções em dias diferentes criam novos diretórios, preservando o histórico completo.

---

## 🧪 OBSERVABILIDADE E LOGGING

Foi implementado um sistema de logging que registra:

- Início da ingestão de cada ativo
- Sucesso na gravação dos dados
- Casos de retorno vazio
- Erros da API (404, ativos deslistados, dados indisponíveis)

Exemplo de log:

```log
INFO | Iniciando ingestão do ativo HGLG11.SA
INFO | Dados salvos em ...
ERROR | $BCFF11.SA: possibly delisted
INFO | Nenhum dado retornado para BCFF11.SA
```


Esse mecanismo garante:
- Transparência do pipeline
- Facilidade de auditoria
- Base para alertas e monitoramento futuro

---

## 📦 ENTREGÁVEIS DA FASE

- Pipeline de ingestão em Python
- Arquivo de metadados (`ativos.csv`)
- Estrutura RAW versionada no Data Lake
- Arquivos Parquet persistidos
- Sistema de logging funcional
- Ambiente Docker com runtime customizado

---

## 📝 CONCLUSÃO DA FASE

Nesta fase, foi consolidado o entendimento de que **a ingestão de dados é o alicerce de toda a arquitetura de dados**. Decisões corretas neste estágio evitam retrabalho, perda de histórico e problemas de governança no futuro.

Ficou claro que:
- Dados devem ser tratados como ativos históricos
- A camada RAW não é um “lixão”, mas um repositório organizado
- Logging e observabilidade são tão importantes quanto o código
- Docker e variáveis de ambiente são essenciais para reprodutibilidade
- Separar ingestão de transformação é um princípio fundamental do ELT moderno

O projeto encontra-se, ao final desta fase, **tecnicamente sólido**, com uma base confiável para avançar para a **FASE 4 — CURADORIA E TRANSFORMAÇÃO (SILVER)**.

---

## 📬 Contato

**LinkedIn:** [Tiago Lima](https://www.linkedin.com/in/tiago-lima-935049154/)  
**GitHub:** [tiago466](https://github.com/tiago466)

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>