import hashlib
import json


with open('answer.json', 'r') as read_file:
    texto = json.load(read_file)

texto_decifrado = texto['decifrado'].lower()

def criptografia():
    resumo_cripto = hashlib.sha1(texto_decifrado.encode())
    resumo_cripto = resumo_cripto.hexdigest()
    
    return resumo_cripto

resumo_criptog = criptografia()

    
texto['resumo_criptografico'] = resumo_criptog


with open('answer.json', 'w') as outfile:
    json.dump(texto, outfile)


if __name__ == '__main__':
    criptografia()