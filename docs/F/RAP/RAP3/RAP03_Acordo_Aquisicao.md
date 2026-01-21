# Acordo de Aquisição e Termos de Uso (RAP 3)
**Projeto:** Colorindo o Daltonismo  
**Data:** 21/01/2026  
**Responsáveis:** Clark e Miguel  

## 1. Identificação dos Acordos
Formalizamos a utilização dos componentes externos selecionados no RAP 2 através da adesão às suas respectivas licenças e termos de serviço.

| Componente | Fornecedor / Origem | Tipo de Acordo (Licença) | Responsabilidade de Suporte |
| :--- | :--- | :--- | :--- |
| **Pandas** | PyData / NumFOCUS | BSD 3-Clause License | Comunidade GitHub / Documentação Oficial |
| **Deep-Translator**| Nidhal Baccouri | MIT License | Comunidade GitHub |
| **FastAPI** | Tiangolo | MIT License | Comunidade GitHub |

## 2. Termos de Nível de Serviço (SLA)
Dado que as aquisições são de custo zero (Open Source/Free Tier), o acordo de manutenção estabelece que:
* **Disponibilidade:** A API de tradução depende da disponibilidade dos servidores do provedor (ex: Google/Libre via Deep-Translator).
* **Segurança:** A equipe (Miguel e Clark) é responsável por monitorar vulnerabilidades nas versões adquiridas via `pip audit` ou GitHub Dependabot.
* **Atualizações:** O projeto manterá as versões fixas no `requirements.txt` (IC-06) para garantir a estabilidade (GCO 5), realizando updates apenas sob Solicitação de Mudança (GCO 3).

## 3. Direitos de Propriedade Intelectual
* O código desenvolvido por Miguel e Clark permanece propriedade da organização.
* As dependências externas mantêm seus créditos e licenças originais, respeitando a política de atribuição de cada biblioteca.

## 4. Gestão do Acordo
Qualquer mudança nos termos de uso (ex: a API de tradução passar a ser paga) disparará uma revisão do portfolio (GPP 5) e uma análise de riscos (GPR 9).