# Projeto para DevOps - Automatizando seu ambiente com Rundeck e Watchdog



# Sobre o projeto:

Projeto implementando rundeck e watchdogs para execução de jobs através do rundeck sempre que houver alterações em uma determinada pasta monitorada pelo watchdog. 



# Ferramentas utilizadas:

  - Watchdog
  - Rundeck
  - Python
  - Sistema Operacional Linux CentOs 7
 


# Modelo de domínio:



# Como executar o projeto:

```bash
# clonar repositório
git clone https://github.com/DiegoClemente/workshop-springboot3-jpa.git


# Modificar projeto
vim api_rundeck_watchdog.py
```

Lembre de alterar o arquivo api_rundeck_watchdog.py para alterar os dados inseridos como exemplo. 


# Executando o arquivo .py

Depois de todas as modificações com suas informações executar: 
```bash 
python3 api_rundeck_watchdog.py & 
```
Isso fará o job no linux ficar em segundo plano para não segurar o terminal. Para ve-lo rodando execute:
```bash
jobs
```
