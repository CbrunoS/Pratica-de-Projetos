def validar_cpf(cpf):
    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números.'
    if len(cpf) != 11:
        return 'Erro: O CPF deve conter exatamente 11 dígitos.'
    return 'CPF válido.'

cpf = input('Digite seu CPF: ')
print(validar_cpf(cpf))

"""Problema central: O problema central é verificar se um CPF fornecido pelo usuário possui exatamente 11 dígitos e contém apenas números, garantindo que ele esteja no formato correto antes de ser utilizado.

Etapas do processo:

Passo 01 - Receber os dados de entrada

Pedir ao usuário que digite o CPF.
Manter a entrada como uma string, pois o CPF pode conter zeros à esquerda.
Passo 02 - Verificar se o CPF contém apenas números

Utilizar o método .isdigit() para garantir que não há letras ou caracteres especiais.
Se houver caracteres inválidos, exibir a mensagem: "Erro: O CPF deve conter apenas números."
Passo 03 - Verificar se o CPF tem exatamente 11 dígitos

Utilizar len(cpf) != 11 para verificar o tamanho.
Se o tamanho for diferente de 11, exibir a mensagem: "Erro: O CPF deve ter exatamente 11 dígitos."
Passo 04 - Exibir a validação do CPF

Se todas as verificações forem bem-sucedidas, exibir: "CPF válido."
"""