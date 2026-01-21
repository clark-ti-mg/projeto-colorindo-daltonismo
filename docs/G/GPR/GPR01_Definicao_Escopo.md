# Declaração de Escopo do Projeto (GPR 1)
**Projeto:** Colorindo o Daltonismo 
**Versão:** 1.0  
**Responsáveis:** Miguel e Clark
**Status:** Linha de Base Estabelecida

---

## 1. Objetivo do Projeto
Desenvolver uma aplicação web baseada em FastAPI para a identificação e conversão de cores, utilizando algoritmos de similaridade e distância perceptual (HSL). O projeto serve como base acadêmica para aplicação de princípios SOLID e processos de qualidade MPS.Br Nível G.

---

## 2. Descrição do Escopo (Entregas Principais)
O escopo do projeto está dividido em quatro pilares fundamentais para garantir o cumprimento dos 23 requisitos estabelecidos:

### 2.1 Módulo de Backend (Lógica de Negócio)
* **Identificação Perceptual:** Implementação de algoritmo de distância HSL para encontrar a cor mais próxima em dataset CSV.
* **Busca Fuzzy:** Implementação de busca por nome de cor com tolerância a erros ortográficos (Similaridade > 60%).
* **Motor de Tradução:** Integração com serviço de tradução automática (EN/PT) com camada de cache.

### 2.2 Interface de Usuário (Front-End)
* **Módulo de Identificação:** Página web para entrada de códigos HEX e visualização de resultados.
* **Módulo de Conversão:** Página web para conversão de nomes de cores em valores hexadecimais.
* **Visualização Dinâmica:** Elemento visual (swatch) para exibição da cor processada.

### 2.3 Engenharia e Qualidade
* **Arquitetura SOLID:** Refatoração completa para desacoplamento de classes e inversão de dependência.
* **Suíte de Testes:** Implementação de testes unitários automatizados para as funções core de matemática e repositório.

---

## 3. Limites do Projeto (O que NÃO está no escopo)
* Integração com bancos de dados relacionais complexos nesta fase (foco em MariaDB via terminal Debian para persistência futura).
* Reconhecimento de cores via câmera ou upload de imagens em tempo real.
* Suporte a sistemas de cores industriais (ex: Pantone).

---

## 4. Critérios de Aceite
1.  O sistema deve identificar corretamente cores a partir de HEX com erro visual imperceptível.
2.  A busca por nome deve funcionar tanto em Português quanto em Inglês.
3.  O código deve passar em 100% dos testes unitários definidos para os Requisitos Funcionais.

---

## 5. Manutenção do Escopo (Controle de Mudanças)
Conforme exigido pelo processo **GRE 4**, qualquer alteração neste escopo deve:
1.  Ser registrada como uma nova **Issue** no GitHub.
2.  Passar por análise de impacto nos 23 requisitos originais.
3.  Ser aprovada via **Pull Request** antes da implementação na branch principal.

---
**Data de Aprovação:** 21/01/2026  
**Aprovação Técnica:** Miguel e Clark (Lead Developer)