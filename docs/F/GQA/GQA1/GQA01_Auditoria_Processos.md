# Auditoria de Aderência de Processos (GQA 1)
**Projeto:** Colorindo o Daltonismo  
**Data da Auditoria:** 21/01/2026  
**Avaliador e Responsáveis pelo Processo (GQA):** Clark e Miguel  

## 1. Objetivo da Avaliação
Verificar se as atividades executadas na Sprint 3 estão em conformidade com o Plano de Projeto (GPR 10) e com o Plano de Gerência de Configuração (GCO 2).

## 2. Itens Avaliados e Verificação de Conformidade

| Processo / Atividade | Procedimento Esperado | Evidência de Aderência | Status |
| :--- | :--- | :--- | :---: |
| **Gestão de Mudanças** | Toda mudança deve ter uma SM no GCO 3. | SM-002 (Trava de 95%) registrada e assinada. | ✅ |
| **Controle de Versão** | Uso de Pull Requests para merges na `main`. | Histórico de PRs no GitHub verificado. | ✅ |
| **Monitoramento** | Atualização do progresso no GPR 11. | Relatório de progresso reflete os 90% atuais. | ✅ |
| **Rastreabilidade** | Vínculo entre requisito e código no GRE 3. | Matriz atualizada com os novos testes de HSL. | ✅ |

## 3. Avaliação Objetiva
* **Padrões de Codificação:** O código segue as diretrizes SOLID estabelecidas no GPR 1? **Sim.** Verificado via análise manual de injeção de dependência.
* **Frequência de Commits:** As subidas de código seguem a cadência diária planejada? **Sim.** Média de 3 commits/dia por desenvolvedor.

## 4. Não Conformidades de Processo Identificadas
* **NC-PROC-001:** O Plano de Riscos (GPR 9) não foi revisado na última sexta-feira conforme o rito semanal.
    * **Ação Corretiva:** Revisão realizada retroativamente em 19/01 e documentada no GPR 12.

## 5. Conclusão do GQA
O projeto apresenta alta aderência aos processos definidos. As falhas administrativas foram pontuais e corrigidas sem impacto na integridade técnica do software.