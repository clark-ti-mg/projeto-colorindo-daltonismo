# Relatório de Desempenho e Riscos (GPR 12)
**Projeto:** Colorindo o Daltonismo 3.0  
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark

## 1. Monitoramento de Desempenho Técnico
O desempenho é medido através da eficácia dos algoritmos e da aderência aos Requisitos Não Funcionais (RNF).

| Indicador de Desempenho | Meta | Real (21/01) | Status |
| :--- | :--- | :--- | :--- |
| **Acurácia de Similaridade (RD05)** | 95% | 96.4% | ✅ |
| **Tempo de Resposta (RNF02)** | < 2s | 1.1s (c/ cache) | ✅ |
| **Cobertura de Testes (GQA)** | > 80% | 85% | ✅ |
| **Dívida Técnica (Sonar)** | < 5% | 2.1% | ✅ |

**Análise:** O desempenho da busca Fuzzy atingiu a meta rigorosa de 95%, garantindo que apenas cores extremamente próximas sejam sugeridas. O uso de Cache (RD03) reduziu o tempo de resposta em 45% comparado aos testes iniciais sem cache.

## 2. Monitoramento de Riscos (Evolução do GPR 9)
Reavaliação dos riscos identificados no início do projeto.

* **R01 (Latência de Tradução):** **Mitigado.** O monitoramento mostra que o `@lru_cache` está absorvendo 80% das requisições repetidas. Risco reduzido para nível Baixo.
* **R03 (Falsos Positivos na Busca):** **Controlado.** A implementação da trava de 95% e os testes unitários específicos em `test_core.py` provaram que o risco de erro de identificação foi neutralizado.
* **R04 (Falha no Sonar):** **Resolvido.** A configuração do `coverage.xml` foi estabilizada. A cobertura agora é visível e mantida em 85%.

## 3. Identificação de Novos Riscos
* **R06 (Manutenibilidade de Dados):** Identificado que o crescimento do `color_names.csv` pode degradar a performance da busca linear do Pandas. 
* **Ação:** Planejada futura migração para indexação em MariaDB (GPR 16).

---
**Responsável:** Miguel (Líder)  
**Revisado por:** Clark (Líder)