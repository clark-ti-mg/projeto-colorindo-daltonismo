# Plano de Gerência de Riscos (GPR 9)
**Projeto:** Colorindo o Daltonismo 
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Identificação e Análise de Riscos
Utilizamos uma matriz de Impacto x Probabilidade para priorizar as ações de mitigação.

| ID | Descrição do Risco | Impacto | Prob. | Mitigação (Plano A) | Contingência (Plano B) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R01** | Indisponibilidade ou latência da API de Tradução. | Médio | Alta | Implementação de `@lru_cache` para evitar chamadas repetidas (RD03). | Uso de um dicionário estático local para as cores mais comuns. |
| **R02** | Imprecisão visual no cálculo de distância RGB. | Alto | Alta | Substituição do cálculo Euclidiano simples pela distância Perceptual HSL (RF06). | Implementação de Delta-E (CIE76) se o HSL falhar. |
| **R03** | Inconsistência na busca Fuzzy (muitos falsos positivos). | Alto | Média | Elevação da trava de similaridade para 95% (RD05). | Desativação da busca Fuzzy, permitindo apenas busca exata. |
| **R04** | Falha na integração do SonarQube (Cobertura 0%). | Médio | Média | Configuração manual do `coverage.xml` via Pytest-cov. | Uso do relatório de cobertura nativo do Pytest como evidência de GQA. |
| **R05** | Corrupção ou erro de leitura no arquivo CSV. | Alto | Baixa | Scripts de validação no `setup_project.py` e normalização via Pandas (RD02). | Recuperação via histórico de versão do Git (GCO). |

## 2. Monitoramento de Riscos
Miguel e Clark revisam este plano ao final de cada iteração. 
* O risco **R03** foi "gatilhado" recentemente, o que levou à decisão técnica de subir a trava para 95% para garantir a qualidade exigida.
* O risco **R04** foi mitigado com sucesso durante a Sprint 3 através da configuração do `sonar-project.properties`.

## 3. Matriz de Severidade
* **Crítico (R02, R03):** Pode invalidar os requisitos funcionais core.
* **Moderado (R01, R04):** Afeta a performance ou a documentação, mas não a funcionalidade principal.