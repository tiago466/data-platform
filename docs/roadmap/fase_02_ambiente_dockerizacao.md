# 🐳 FASE 2 — AMBIENTE E DOCKERIZAÇÃO

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## ✔ TAREFAS REALIZADAS

- ✅ Criação do `docker-compose.yml` base da plataforma  
- ✅ Definição dos serviços essenciais do ambiente  
- ✅ Criação de um runtime Python isolado e reproduzível  
- ✅ Configuração de volumes para simular o Data Lake  
- ✅ Configuração de variáveis de ambiente via arquivo `.env`  
- ✅ Validação da subida e funcionamento do ambiente local  
- ✅ Execução de scripts Python dentro do container  
- ✅ Validação de bind mounts entre host e container  

---

## 🎯 OBJETIVO DA FASE

O objetivo desta fase foi construir um **ambiente de execução reproduzível**, independente da máquina local, que servisse como base sólida para toda a evolução da plataforma de dados.

Buscou-se eliminar dependências locais (Anaconda, versões distintas de Python, configurações manuais) e garantir que todo o código do projeto fosse executado sempre no **mesmo runtime**, respeitando boas práticas modernas de engenharia de software e os princípios dos **12 Fatores**.

---

## 🧠 CONHECIMENTO ADQUIRIDO

Durante esta fase, foram consolidados conceitos fundamentais relacionados a ambiente, runtime e execução de código:

- Docker como ferramenta de padronização de runtime
- Docker Compose como orquestrador local de serviços
- Diferença clara entre:
  - Dockerfile (construção de imagem)
  - Docker Compose (orquestração de containers)
- Conceito de **runtime** como o ambiente onde o código executa
- Separação entre:
  - Escrita de código (fora do container)
  - Execução de código (dentro do container)
- Uso de imagens oficiais e estáveis do Docker Hub
- Bind mounts como mecanismo de compartilhamento de filesystem
- Containers como entidades descartáveis (*cattle, not pets*)
- Volumes como forma de persistência de código e dados
- Variáveis de ambiente como contrato de configuração
- Introdução prática aos **12 fatores**, especialmente:
  - Configuração via ambiente
  - Paridade entre desenvolvimento e produção
  - Separação entre código e configuração

---

## 🔍 PRINCIPAIS DÚVIDAS E ESCLARECIMENTOS

### ❓ Docker Compose é um conjunto de Dockerfiles encadeados?

Foi esclarecido que **não**.  
O Dockerfile define **como uma imagem é construída**, enquanto o Docker Compose define **como múltiplos containers são executados e conectados**.

Eles são complementares, mas possuem responsabilidades distintas.

---

### ❓ O que é runtime e qual seu papel?

Runtime foi entendido como **o ambiente completo onde o código executa**, incluindo:
- versão do Python
- sistema operacional
- bibliotecas
- variáveis de ambiente
- filesystem disponível

O container Python criado via Docker passou a ser o **runtime oficial do projeto**, substituindo execuções locais via Anaconda.

---

### ❓ Desenvolver em Python 3.12 localmente e executar em 3.11 no container pode gerar problemas?

Sim. Foi reforçado que diferenças de versão de runtime podem causar falhas sutis ou explícitas.  
A regra adotada no projeto passou a ser:

> Escrever código fora do container, mas **executar e validar sempre dentro do runtime Docker**.

---

### ❓ O que acontece com os arquivos montados via `volumes`?

Foi validado na prática que os arquivos **não são copiados** para o container.  
O Docker cria um **bind mount**, onde o mesmo diretório do host é compartilhado com o container em tempo real.

Isso garante:
- persistência de dados
- versionamento via Git
- descarte seguro de containers

---

### ❓ O arquivo `.env` é seguro ou criptografado?

Foi corrigido o entendimento inicial de que o `.env` seria criptografado.  
Na prática:
- `.env` é texto puro
- não oferece segurança por si só
- sua função é **desacoplamento de configuração**
- segurança vem de processos, não do arquivo

---

### ❓ Por que os paths aparecem “mocados” no `docker-compose.yml` e também no `.env`?

Foi esclarecido que:
- `volumes` são responsabilidade da **infraestrutura (Docker)**
- variáveis no `.env` são responsabilidade da **aplicação (Python)**

Essa duplicidade não é erro, mas sim **separação correta de camadas**.

---

## 🧩 DECISÕES ARQUITETURAIS IMPORTANTES

- Utilização de imagem oficial `python:3.11-slim`
- Não criação de Dockerfile nesta fase (evitar overengineering)
- Uso de bind mounts em vez de volumes nomeados
- Centralização de configuração no `.env`
- Execução manual de scripts via `docker exec`
- Separação clara entre ambiente e código
- Foco em aprendizado conceitual antes de automação

---

## 📦 ENTREGÁVEIS GERADOS

- `docker-compose.yml` funcional e documentado
- Runtime Python isolado e reproduzível
- Diretórios `pipelines/` e `data-lake/` montados via bind mount
- Arquivo `.env` centralizando configuração
- Execução validada de scripts Python dentro do container
- Prova prática de compartilhamento de filesystem
- Ambiente pronto para ingestão de dados reais

---

## 📝 CONCLUSÕES DA FASE

Esta fase consolidou um dos pilares mais importantes de qualquer projeto de dados: **controle total do ambiente de execução**.

Ficou claro que:
- problemas de “funciona na minha máquina” são quase sempre problemas de runtime
- Docker não é apenas uma ferramenta de deploy, mas de **qualidade e previsibilidade**
- separar código, dados e ambiente é essencial para escalar projetos de dados
- ambientes reproduzíveis reduzem drasticamente erros futuros

A principal conclusão é que **não existe Big Data sustentável sem um ambiente sólido e padronizado**.  
Esta fase cria a base necessária para evoluir com segurança para ingestão, curadoria, analytics e machine learning.

---

## 🔑 PONTOS MAIS IMPORTANTES DA FASE

- Runtime controlado é tão importante quanto o código
- Docker resolve problemas estruturais, não apenas técnicos
- Bind mounts são essenciais para desenvolvimento
- `.env` é contrato de configuração, não mecanismo de segurança
- Execução deve sempre ocorrer no ambiente oficial
- Overengineering deve ser evitado nas fases iniciais

---

## 📬 Contato

**LinkedIn:** [Tiago Lima](https://www.linkedin.com/in/tiago-lima-935049154/)  
**GitHub:** [tiago466](https://github.com/tiago466)

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>