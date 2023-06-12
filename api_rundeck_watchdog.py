import requests
import os
import time


RUNDECK_BASE_URL = 'http://localhost:4440'  
API_TOKEN = 'seu_token_de_acesso'  # Lembrar de validar ACL e usuario
PROJECT_NAME = 'nome_do_projeto'  
JOB_ID = 'ID_do_job'  

# Pasta monitorada pelo watchdog
MONITORED_FOLDER = '/caminho/para/pasta/monitorada'


def trigger_rundeck_job():
    url = f'{RUNDECK_BASE_URL}/api/22/job/{JOB_ID}/run?authtoken={API_TOKEN}'
    headers = {
        'Content-Type': 'application/json',
        'X-Rundeck-Auth-Token': API_TOKEN
    }
    payload = {
        'argString': '-option1 value1 -option2 value2', # (opcional)
        'filter': '',  # (opcional)
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print('Job acionado com sucesso!')
    else:
        print(f'Falha ao acionar o job. Código de status: {response.status_code}')
        print(response.text)


def run_watchdog():
    print('Watchdog em execução...')
    last_modified = 0
    
    while True:
        current_modified = os.path.getmtime(MONITORED_FOLDER)
        
        if current_modified > last_modified:
            print(f'Detectada mudança na pasta {MONITORED_FOLDER}. Acionando o job...')
            trigger_rundeck_job()
            last_modified = current_modified
        
        time.sleep(1)

# Executa o watchdog
run_watchdog()
