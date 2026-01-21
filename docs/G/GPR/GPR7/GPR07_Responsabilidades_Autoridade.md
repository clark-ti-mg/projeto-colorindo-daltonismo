# Matriz de Responsabilidades e Autoridade (GPR 7)
**Projeto:** Colorindo o Daltonismo 3.0  
**Data:** 21/01/2026  
**Equipe:** Miguel e Clark  

## 1. Definição de Papéis
Embora ambos atuem como Líderes e Desenvolvedores, as áreas de autoridade foram segregadas para garantir a integridade dos processos MPS.Br.

* **Líder de Desenvolvimento (Backend/Dados):** Responsável pela arquitetura SOLID e lógica matemática.
* **Líder de Qualidade (GQA/Testes):** Responsável pela validação do Sonar e cobertura de testes.
* **Gestor de Configuração (GCO):** Responsável pela integridade das branches e releases.

## 2. Matriz RACI (Responsável, Autoridade, Consultado, Informado)
Esta matriz define quem executa e quem tem a autoridade de aprovação para os 23 requisitos.

| Atividade / Processo | Miguel | Clark |
| :--- | :---: | :---: |
| **Definição de Escopo (GPR 1)** | **A** | **A** |
| **Arquitetura SOLID (RNF01)** | **R** | **A** |
| **Lógica de Distância HSL (RF06)** | **A** | **R** |
| **Configuração do Sonar e GQA** | **R** | **A** |
| **Aprovação de Pull Requests** | **A** | **R** |
| **Gestão de Requisitos (GRE)** | **R** | **R** |

**Legenda:**
* **R (Responsável):** Quem executa a tarefa.
* **A (Autoridade):** Quem aprova e tem a palavra final (prestação de contas).

## 3. Autoridade de Decisão
* **Mudanças Técnicas:** Decisões que alterem o cálculo de similaridade (como a mudança para 95%) devem ter consenso de ambos os líderes.
* **Conflitos de Código:** Em caso de divergência em PRs (Pull Requests), o Líder de Qualidade tem autoridade para vetar o merge caso a cobertura de testes seja inferior a 80%.

## 4. Manutenção das Responsabilidades
As responsabilidades são revisadas no início de cada sprint. Qualquer alteração de papel devido a impedimentos técnicos deve ser registrada em ata de reunião e atualizada neste documento.

---
**Aprovado por:** Miguel e Clark  
**Data da Última Revisão:** 21/01/2026