# Relatório de Estabelecimento de Infraestrutura (GPR 16)
**Projeto:** Colorindo o Daltonismo 3.0  
**Data:** 21/01/2026  
**Responsáveis:** Miguel e Clark  

## 1. Planejamento da Infraestrutura
Conforme planejado no GPR 5, a infraestrutura foi estabelecida para suportar o desenvolvimento Python/FastAPI e a persistência em MariaDB.

### 1.1 Ambiente de Desenvolvimento (Workstation)
* **SO:** Windows 11 com WSL2 (Debian) para simular ambiente de produção Linux.
* **IDE:** VS Code com extensões para Python (Pylance) e SonarLint.
* **Python:** Versão 3.14.2 estável.

### 1.2 Ambiente de Banco de Dados e Servidor
* **Database:** MariaDB Server instalado via terminal Debian.
* **Servidor Web:** Uvicorn (ASGI) para execução do FastAPI.
* **Automação:** Script `setup_project.py` para criação automática da árvore de diretórios (`/app`, `/tests`, `/docs`, `/templates`).

## 2. Ferramentas de Apoio e Qualidade
* **Versionamento:** Git (GitHub) para controle de configuração (GCO).
* **Análise Estática:** SonarQube Local configurado na porta 9000.
* **Relatório de Cobertura:** Pytest-cov para geração do `coverage.xml`.

## 3. Manutenção da Infraestrutura
A integridade do ambiente é mantida através de:
1. **requirements.txt:** Travamento de versões das bibliotecas (Aquisição).
2. **Backups:** Sincronização automática do repositório local com o GitHub a cada commit.
3. **Scripts de Verificação:** O `setup_project.py` valida se o arquivo `color_names.csv` existe antes de iniciar o servidor.

## 4. Evidência de Instalação
O ambiente foi validado em 12/01/2026 com a execução bem-sucedida do comando:
`python -m uvicorn app.main:app --reload`