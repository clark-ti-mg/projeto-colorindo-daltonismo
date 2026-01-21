# Registro e Tratamento de Não Conformidades (GQA 3 e 4)
**Projeto:** Colorindo o Daltonismo  
**Responsáveis:** Clark e Miguel  
**Última Atualização:** 21/01/2026

## 1. Definição de Severidade
* **Crítica:** Impede a entrega do requisito ou compromete a segurança/precisão (95%).
* **Maior:** Afeta a manutenibilidade ou padrões SOLID, mas não quebra a função.
* **Menor:** Erros estéticos, comentários ou bibliotecas desnecessárias.

## 2. Log de Não Conformidades (NCs)

| ID | Descrição da Não Conformidade | Origem | Severidade | Ação Corretiva Realizada | Status |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **NC-001** | Erro de Injeção de Dependência no `test_core.py`. | GQA 2 | **Crítica** | Atualizada assinatura do mock para incluir `math_service`. | ✅ Fechada |
| **NC-002** | Trava de similaridade em 60% gerando falsos positivos. | GPR 12 | **Crítica** | Código e Requisito (RD05) alterados para trava de 95%. | ✅ Fechada |
| **NC-003** | Presença de bibliotecas não utilizadas no `requirements.txt`.| GQA 2 | **Menor** | Limpeza do arquivo e novo build de teste realizado. | ✅ Fechada |
| **NC-004** | Falha na revisão semanal do Plano de Riscos (GPR 9). | GQA 1 | **Maior** | Realizada revisão retroativa e atualização do GPR 12. | ✅ Fechada |

## 3. Fluxo de Comunicação e Fechamento (GQA 4)
As NCs identificadas nas auditorias de 21/01 foram comunicadas imediatamente entre a dupla via Issues do GitHub. 

* **Critério de Fechamento:** Uma NC só é considerada "Fechada" após a re-execução do teste ou auditoria que a originou.
* **Verificação Final:** Clark e Miguel confirmam que, na data de hoje, **não existem Não Conformidades abertas** que impeçam a liberação da versão v1.0.0-beta.

## 4. Análise de Recorrência
Observou-se que as NCs técnicas (001 e 002) ocorreram durante a transição para a arquitetura SOLID. A equipe decidiu reforçar a revisão de código (*Peer Review*) antes de cada merge para evitar novos erros de injeção.