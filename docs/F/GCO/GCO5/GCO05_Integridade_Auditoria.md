# Garantia da Integridade e Auditoria de Configuração (GCO 5)
**Projeto:** Colorindo o Daltonismo  
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Mecanismos de Proteção da Integridade
Para garantir que os Itens de Configuração (ICs) não sejam corrompidos ou alterados de forma não autorizada, utilizamos:

* **Imutabilidade de Commits:** Cada alteração gera um Hash SHA-1 exclusivo. Se um único caractere no `color_names.csv` for alterado, o Hash mudará, alertando a equipe.
* **Tags de Baseline:** Após a aprovação da v1.0.0, criamos uma Tag fixa no GitHub. Isso impede que commits posteriores "sujem" a versão de entrega.
* **Trincas de Validação:** Uma release só é considerada íntegra se passar por:
    1. Build sem erros.
    2. Testes unitários com 100% de sucesso.
    3. Cobertura SonarQube > 80%.

## 2. Auditoria Física de Configuração (AFC)
Realizamos uma verificação para garantir que todos os itens listados no GCO 1 estão presentes no pacote de entrega.

| Item de Configuração | Status no Repositório | Verificado por |
| :--- | :---: | :--- |
| Código Fonte (`/app`) | Presente | Clark |
| Base de Dados (`.csv`) | Presente | Miguel |
| Documentação GPR/GCO | Presente | Clark |
| Dependências (`requirements.txt`) | Atualizado | Miguel |

## 3. Auditoria Funcional de Configuração (AFO)
Verificamos se o item de configuração se comporta conforme o requisito planejado.
* **Evidência:** O código na branch `main` (Hash: `a1b2c3d`) foi testado e confirmou a trava de similaridade em **95%** (RD05).

## 4. Registro de Verificação de Integridade
"Em 21/01/2026, Miguel e Clark realizaram o 'checksum' visual e funcional da versão v1.0.0-beta. Confirmamos que o código-fonte corresponde à documentação de design e que os artefatos de teste estão sincronizados."