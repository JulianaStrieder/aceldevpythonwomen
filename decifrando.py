import json
#from requisicaoget import requisicao_get


alfabeto = 'abcdefghijklmnopqrstuvwxyz'


decifrado = []


with open('texto_a_decifrar.json', 'r') as read_file:
    texto = json.load(read_file)

texto_a_decifrar = texto['cifrado'].lower()
numero_de_casas = texto['numero_casas']

def decifra():
    for i in range(0, len(texto_a_decifrar)):
        if texto_a_decifrar[i] in alfabeto:
            letra = texto_a_decifrar[i]
            #print(letra)
            contador_de_casas = alfabeto.find(letra) - numero_de_casas
            #print(contador_de_casas)
            if contador_de_casas <= 25:
                decifrado.append(alfabeto[contador_de_casas])
            elif contador_de_casas == 26:
                decifrado.append(alfabeto[0])
            elif contador_de_casas == 27:
                decifrado.append(alfabeto[1])
            elif contador_de_casas == 28:
                decifrado.append(alfabeto[2])
            else:
                decifrado.append(alfabeto[3])
        elif texto_a_decifrar[i] == ' ':
            decifrado.append(' ')
        elif texto_a_decifrar[i] == ',':
            decifrado.append(',')
        elif texto_a_decifrar[i] == '\\':
            decifrado.append('\\')
        elif texto_a_decifrar[i] == '"':
            decifrado.append('"')                
        else:
            decifrado.append('.')         
        
    string_pronta = ''.join(decifrado)

    return string_pronta


texto['decifrado'] = decifra()

with open('answer.json', 'w') as outfile:
    json.dump(texto, outfile)


if __name__ == '__main__':
    decifra()