# Projeto para DevOps - Automatizando seu ambiente com Rundeck e Watchdog



# Sobre o projeto:

Projeto implementando rundeck e watchdogs para execução de jobs através do rundeck sempre que houver alterações em uma determinada pasta monitorada pelo watchdog. 



# Ferramentas utilizadas:

  - Watchdog
  - Rundeck
  - Python
  - Sistema Operacional Linux CentOs 7
 

# Como executar o projeto:

```bash
# clonar repositório
git clone https://github.com/DiegoClemente/DevOps.git


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

# OUTPUT

Sempre que uma alteração (Criação, Deleção, Alteração) for feita na pasta informada na variavel MONITORED_FOLDER no arquivo .py o job do rundeck configurado será chamado e executará. 
O processo ficará em loop ate que seja trazido para o terminal em primeiro plano

```bash
fg %(N° do processo criado na etapa # Executando o arquivo)
```
e teclado Ctrl + C para finalizar o .py
