# Relatório de Estimativas de Tamanho e Complexidade (GPR 3)
**Projeto:** Colorindo o Daltonismo
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Metodologia de Estimativa
Para o estabelecimento das estimativas, a equipe utilizou a técnica de **Analogia e Julgamento Especialista**, considerando projetos anteriores de web development e data mining. As tarefas foram classificadas em níveis de complexidade (Baixa, Média, Alta) baseadas no impacto na arquitetura SOLID.

## 2. Tabela de Estimativas por Produto de Trabalho
Abaixo, detalhamos a complexidade estimada para os principais componentes da aplicação:

| Produto de Trabalho (Entrega) | Tamanho (Linhas/Arquivos) | Complexidade | Justificativa Técnica |
| :--- | :--- | :--- | :--- |
| **Arquitetura de Interfaces** | 1 Arquivo / 4 Interfaces | Média | Exige abstração correta para atender ao Princípio DIP (SOLID). |
| **Cálculo Distância HSL** | ~50 Linhas de Código | Alta | Envolve lógica matemática de conversão de sistemas de cores (RGB -> HSL). |
| **Normalização de Dados** | ~30 Linhas de Código | Baixa | Limpeza de strings e manipulação básica de CSV via Pandas. |
| **Interface Responsiva** | 2 Arquivos HTML/CSS | Média | Necessidade de garantir usabilidade em múltiplos dispositivos (RI01). |
| **Busca Fuzzy (Similarity)** | ~20 Linhas de Código | Alta | Implementação de algoritmos de similaridade de texto para RF05. |

## 3. Manutenção das Estimativas
As estimativas foram revisadas após a primeira iteração. Identificou-se que a complexidade da **Tradução com Cache** foi subestimada inicialmente, sendo reclassificada de Média para Alta devido aos testes de latência exigidos pelo RNF02.

---
**Aprovado por:** Miguel e Clark
**Data da Última Revisão:** 21/01/2026