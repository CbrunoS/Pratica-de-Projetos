import random

def gerar_senha():
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+-=[]{}|;:,.<>'

    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    todos_caracteres = maiusculas + minusculas + numeros + simbolos
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)

print(f'Senha gerada: {gerar_senha()}')


""""
Problema central: O problema central é gerar uma senha aleatória de 12 caracteres que contenha pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial, garantindo segurança mínima.

Etapas do processo:

Passo 01 - Definir os conjuntos de caracteres

Criar variáveis contendo os diferentes tipos de caracteres que serão utilizados:
maiusculas: letras maiúsculas (A-Z).
minusculas: letras minúsculas (a-z).
numeros: dígitos de 0 a 9.
especiais: caracteres especiais comuns (!@#$%&*).
Passo 02 - Garantir a inclusão de pelo menos um caractere de cada categoria

Utilizar random.choice() para selecionar uma letra maiúscula, uma letra minúscula, um número e um caractere especial.
Armazenar esses caracteres iniciais em uma lista chamada senha.
Passo 03 - Completar a senha com caracteres aleatórios

Criar uma variável todos_caracteres, contendo todos os caracteres possíveis.
Utilizar random.choices(todos_caracteres, k=8) para adicionar 8 caracteres aleatórios à senha, totalizando uma senha de 12 caracteres (4 fixos + 8 aleatórios).
Passo 04 - Embaralhar a senha para garantir aleatoriedade

Utilizar random.shuffle(senha) para reorganizar os caracteres da lista, para evitar que os primeiros caracteres sejam sempre das categorias fixas, garantindo mais aleatoriedade na senha final.
Converter a lista senha em uma string utilizando ''.join(senha).
Passo 05 - Exibir a senha gerada

Chamar a função gerar_senha() e imprimir o resultado.
"""