texto = input('Digite um texto: ')

palavras_longas = []

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)

if palavras_longas:
    print('Palavras longas encontradas:')
    for palavra in palavras_longas:
        print(palavra)

else:
    print('Nenhuma palavra longa encontrada.')


"""
Problema central: O problema central é analisar um texto fornecido pelo usuário, identificar palavras que possuam mais de 10 letras e exibi-las. Caso não haja palavras longas, o programa deve informar o usuário.

Etapas do processo:

Passo 01 - Receber o texto de entrada

Solicitar que o usuário digite um texto.
Armazenar a entrada em uma variável texto.
Passo 02 - Separar o texto em palavras

Utilizar .split() para dividir o texto em uma lista de palavras, considerando espaços como separadores.
Passo 03 - Identificar palavras longas

Criar uma lista vazia chamada palavras_longas para armazenar palavras com mais de 10 letras.
Percorrer a lista de palavras usando um loop for.
Verificar o comprimento de cada palavra com len(palavra) > 10.
Se a palavra for longa, adicioná-la à lista palavras_longas.
Passo 04 - Exibir o resultado

Se houver palavras na lista palavras_longas, exibi-las uma por linha.
Caso contrário, exibir a mensagem "Nenhuma palavra longa foi encontrada no texto."
"""