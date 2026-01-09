# FASE 1 — FUNDAMENTOS DE ARQUITETURA DE DADOS

<a href="../../README.md" title="Voltar para a página principal">
🏠 Voltar para Home
</a>

## TAREFAS REALIZADAS

- ✅ Aprendizado dos principais fundamentos de Big Data e Data Engineering
- ✅ Criação do repositório Git do projeto
- ✅ Definição do objetivo e escopo da plataforma
- ✅ Criação da estrutura inicial de diretórios
- ✅ Criação do README arquitetural
- ✅ Definição das camadas de dados (Raw, Curated e Analytics)

## OBJETIVO DA FASE
O objetivo desta fase foi compreender o que é Big Data de fato, indo além de ferramentas e tecnologias específicas, e entendendo Big Data como um conjunto de princípios arquiteturais voltados à organização, escalabilidade e governança de dados.

Buscou-se separar claramente:

- OLTP vs OLAP
- Código vs Dados
- Ingestão vs Transformação

Criando assim uma base conceitual sólida para todas as fases seguintes do projeto.

## CONHECIMENTO ADQUIRIDO
Durante esta fase, foram consolidados os seguintes conceitos fundamentais:

- Big Data não é volume, mas arquitetura e propósito
- Data Lake como repositório central de dados
- Separação clara de responsabilidades entre sistemas
- ELT como abordagem moderna e segura
- Importância de dados históricos imutáveis

- Camadas de dados:
    - Raw (Bronze): dados brutos, sem tratamento
    - Curated (Silver): dados limpos, padronizados e validados
    - Analytics (Gold): dados modelados para consumo analítico

Também ficou claro que:
- ETL dentro de banco OLTP é uma má prática
- Transformações pesadas devem ocorrer fora do ambiente transacional
- Dados devem ser tratados como ativos históricos, não como tabelas descartáveis

## ENTREGÁVEIS GERADOS
- Repositório Git versionado
- Estrutura inicial de diretórios da plataforma
- README com visão geral do projeto
- Definição conceitual das camadas de dados
- Base para evolução incremental da arquitetura

# CONCLUSÕES E RESSALVAS TÉCNICAS
Durante esta fase, algumas reflexões importantes surgiram:

- Big Data pode existir mesmo com pouco volume, desde que a arquitetura esteja correta
- Centralizar dados sem governança não é Big Data
- “BI” não é ferramenta de dashboard, mas um ecossistema analítico completo
- Arquitetura correta evita retrabalho, truncates destrutivos e dependência de frontend
- Overengineering é tão prejudicial quanto soluções improvisadas

A principal conclusão é que arquitetura vem antes de ferramenta.
Sem uma base conceitual sólida, qualquer stack técnica tende a se tornar frágil, difícil de manter e pouco escalável.

## PONTOS MAIS IMPORTANTES DA FASE

- Separação entre sistemas operacionais e analíticos
- ELT como pilar central
- Dados como ativos históricos
- Arquitetura orientada a evolução
- Pensamento arquitetural acima de implementação imediata

## 📬 Contato

**LinkedIn:** [Tiago Lima](https://www.linkedin.com/in/tiago-lima-935049154/)  
**GitHub:** [tiago466](https://github.com/tiago466)

---

<div align="left">
  <a href="#topo" title="Voltar ao início do README">⬆️ Topo</a>
</div>