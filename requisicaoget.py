import json
import os
import requests

MY_TOKEN = os.getenv('MY_TOKEN')
CODENATION_URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + MY_TOKEN


def requisicao_get():
    response = requests.get(CODENATION_URL)
    
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')
    
    print('\n Getting data... \n')

    try:
        texto_a_decifrar = response.json()
        with open('/home/juliana/projeto_Alice_no_Pais_dos_Dados/aceleradevpythonwomen/texto_a_decifrar.json', 'w') as f:
            json.dump(texto_a_decifrar, f) 
        
    except KeyError:
        print('Could not parse request results')



if __name__ == '__main__':
    requisicao_get()
