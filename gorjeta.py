valor_conta = float(input('Digite o valor da conta: '))
porcentagem_gorjeta = float(input('Digite a porcentagem de gorjeta: '))
gorjeta = (porcentagem_gorjeta / 100) * valor_conta
total = valor_conta + gorjeta

print(f'Valor da gorjeta: R$ {gorjeta:.2f}')
print(f'Total a pagar: R$ {total:.2f}')


"""Problema central: O problema central é determinar o valor total da conta após adicionar uma gorjeta opcional, calculada como uma porcentagem do valor inicial.

Etapas do processo:
Passo 01 - Receber os dados de entrada

.Pedir ao usuário o valor da conta.
.Pedir ao usuário a porcentagem de gorjeta desejada.
.Converter as entradas para float para garantir precisão nos cálculos.

Passo 02 - Calcular o valor da gorjeta com base na fórmula: gorjeta = (porcentagem_gorjeta / 100) * valor_conta.

Passo 03 - Calcular o total a pagar, somando o valor da conta com o valor da gorjeta: total = valor_conta + gorjeta.

Passo 04 - Exibir os resultados formados.

.Mostrar o valor da gorjeta ecom duas casas decimais.
.Mostrar o total a pagar, também formatado corretamente com duas casas decimais."""