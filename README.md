# Data Platform

**Autor:** Tiago Lima  
**Data:** 06/01/2026  

---

## Visão Geral

Este projeto tem como objetivo a construção de uma **plataforma de dados moderna (Data Platform)**, voltada ao desenvolvimento de **pipelines de Big Data**, organização de dados por domínios e camadas, e aplicação de boas práticas de **Engenharia de Dados, Arquitetura de Dados e Machine Learning**.

A plataforma foi projetada para ser **escalável, extensível e reutilizável**, permitindo a adição de novos domínios de negócio ao longo do tempo, mantendo governança, rastreabilidade e separação clara de responsabilidades entre ingestão, curadoria, análise e modelagem.

O projeto serve tanto como **ambiente de estudo estruturado** quanto como **portfólio técnico**, demonstrando desde fundamentos de Big Data até pipelines completos prontos para análises e modelos de Machine Learning.

---

## Objetivo

- Construir uma **base arquitetural sólida** para projetos de Big Data
- Aplicar conceitos modernos de Engenharia de Dados (ELT, Data Lake, camadas)
- Separar claramente OLTP e OLAP
- Organizar dados por **domínios de negócio**
- Criar pipelines reprocessáveis, versionados e governáveis
- Evoluir do dado bruto até análises e modelos de Machine Learning
- Documentar decisões técnicas e aprendizados ao longo do projeto

---

## Escopo

### Inclui
- Ingestão de dados a partir de múltiplas fontes (APIs, bancos, arquivos)
- Data Lake organizado por camadas (RAW, CURATED, ANALYTICS)
- Pipelines de dados desacoplados do banco OLTP
- Engenharia de atributos (feature engineering)
- Modelagem analítica e preparação para ML
- Uso de Docker para reprodutibilidade
- Documentação arquitetural detalhada

### Não inclui (neste momento)
- Sistemas de recomendação em produção
- Trading automatizado real
- Streaming em tempo real
- Orquestração distribuída complexa (Airflow, Kubernetes)
- Ambientes cloud produtivos (foco inicial local)

---

## Arquitetura (Resumo)

A plataforma segue uma arquitetura moderna baseada em camadas e domínios:

**Fontes de Dados → Data Lake (RAW / CURATED / ANALYTICS) → Consumo Analítico / ML**

- **RAW:** dados armazenados exatamente como recebidos, de forma imutável  
- **CURATED:** dados tratados, padronizados e validados  
- **ANALYTICS:** dados orientados ao negócio, features e data marts  

Mais detalhes estão disponíveis em:
- [`docs/architecture.md`](docs/architecture.md)

---

## Domínios de Dados
A plataforma é organizada por **domínios de negócio**, permitindo evolução independente de cada contexto de dados.

<details>
<summary>➕ Clique para expandir</summary>

- **[Fluxo Operacional](docs/fluxo_operacional.md)**  
  Domínio voltado ao estudo de pipelines analíticos a partir de dados operacionais  
  *(atualmente em standby)*

- **[Mercado Financeiro](docs/mercado_financeiro.md)**  
  Domínio ativo, focado em dados históricos do mercado financeiro, engenharia de atributos
  e aplicação de modelos de Machine Learning para séries temporais

</details>

---

## Documentação Complementar

A documentação do projeto está organizada para facilitar navegação e entendimento técnico:

- **[Técnicas e Conceitos Utilizados](docs/documentacao/tecnicas.md)**  
  ELT, Data Lake, camadas de dados, reprocessamento, governança, feature engineering, etc.

- **[Tecnologias Utilizadas](docs/documentacao/tecnologias.md)**  
  Linguagens, bibliotecas, ferramentas e frameworks utilizados na plataforma

- **[Dependências do Projeto](docs/documentacao/requirements.md)**  
  Explicação das principais bibliotecas Python utilizadas  
  *(o arquivo `requirements.txt` será criado conforme os pipelines forem implementados)*

- **[Decisões Arquiteturais](docs/decisions.md)**  
  Registro das principais decisões técnicas tomadas ao longo do projeto

- **[Glossário](docs/glossary.md)**  
  Definições e padronização de termos técnicos e de negócio

---

## 🐳 Ambiente de Execução

O projeto utiliza **Docker e Docker Compose** para garantir:

- Paridade entre ambientes
- Runtime controlado
- Execução previsível dos pipelines

O setup completo do ambiente está documentado em:
📄 [`docs/roadmap/fase_02_ambiente_dockerizacao.md`](docs/roadmap/fase_02_ambiente_dockerizacao.md)

---

## Estrutura de Diretórios

```bash
data-platform/
├── data-lake/
│ ├── raw/
│ ├── curated/
│ └── analytics/
│
├── pipelines/
│ ├── fluxo_operacional/
│ └── mercado_financeiro/
│
├── docs/
│
├── docker/
│
└── README.md
```

Cada novo domínio adicionado segue este mesmo padrão estrutural.

---

## ▶️ Como Rodar o Projeto (Resumo)

Pré-requisitos:
- Docker
- Docker Compose

Subir o ambiente:
```bash
cd docker
docker compose up -d
```

Entrar no container:
```bash
docker exec -it data-platform-python bash
```
Para mais detalhes, consulte a [`documentação da FASE 2`](docs/roadmap/fase_02_ambiente_dockerizacao.md).

---

## Roadmap de Aprendizado

Este projeto é estruturado em fases progressivas de aprendizado e implementação.

- [Fase 1 — Fundamentos de Arquitetura de Dados](docs/roadmap/fase_01_fundamentos_arquitetura.md)
- [Fase 2 — Ambiente e Dockerização](docs/roadmap/fase_02_dockerizacao.md)
- [Fase 3 — Ingestão RAW(Bronze)](docs/roadmap/fase_03_ingestao_dados_bronze.md)
- [Fase 4 — Curadoria e Transformação CURATED(Silver)](docs/roadmap/fase_04_curadoria_transformacao_silver.md)
- [Fase 5 — Analytics e ML(Gold)](docs/roadmap/fase_05_datawarehouse_modelos.md)
- [Fase 6 — Consumo, Governança e Observabilidade](docs/roadmap/fase_06_consumo_governanca.md)

Cada fase contém objetivos, decisões técnicas, dúvidas, aprendizados e conclusões.

---

## Referências e Bibliografia

- Artigos e materiais sobre Big Data e Engenharia de Dados
- Documentações oficiais das bibliotecas utilizadas
- Materiais acadêmicos e profissionais da área
- Conteúdos utilizados durante o MBA e estudos independentes

---

## 📬 Contato

**LinkedIn:** [Tiago Lima](https://www.linkedin.com/in/tiago-lima-935049154/)  
**GitHub:** [tiago466](https://github.com/tiago466)

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>