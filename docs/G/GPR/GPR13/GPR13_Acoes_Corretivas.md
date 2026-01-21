# Registro de Ações Corretivas (GPR 13)
**Projeto:** Colorindo o Daltonismo
**Responsáveis:** Miguel e Clark  

## 1. Ação Corretiva AC-01: Inconsistência na Suíte de Testes
* **Identificado em:** 21/01/2026 (Durante monitoramento GPR 11)
* **Desvio:** O comando `pytest` falhou com `TypeError` ao instanciar o `ColorRepository`, pois a assinatura do método exigia um `math_service` não fornecido no teste.
* **Causa Raiz:** A refatoração para SOLID (DIP) alterou o código principal, mas o código de teste estava desatualizado (Inconsistência de Configuração).
* **Ação Executada:** Atualização do arquivo `test_core.py` para incluir a Injeção de Dependência correta.
* **Resultado:** Sucesso na execução dos testes e geração do `coverage.xml` para o Sonar.

## 2. Ação Corretiva AC-02: Baixa Acurácia Perceptual (RD05)
* **Identificado em:** 16/01/2026 (Durante a Sprint 2)
* **Desvio:** Testes preliminares com 60% de similaridade retornavam cores visualmente distintas para o olho humano (Falsos Positivos).
* **Causa Raiz:** O limiar de 60% era muito permissivo para o algoritmo de distância HSL.
* **Ação Executada:** Alteração do requisito técnico e da constante no código para **95%** de similaridade mínima.
* **Resultado:** Acurácia técnica validada em 96.4% no GPR 12.

## 3. Acompanhamento e Fechamento
Todas as ações corretivas foram documentadas, implementadas via commits no Git e validadas pela dupla. Não há ações pendentes que impeçam a entrega final em 22/01.