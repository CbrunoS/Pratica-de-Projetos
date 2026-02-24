def caixa_eletronico():
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor = int(input('Digite o valor a ser sacado: '))

        if valor <= 0:
            print('Valor inválido! O valor deve ser maior que zero.')
        elif valor % 2 != 0:
            print('Valor inválido! O valor deve ser múltiplo de 2.')
        else:
            print('Cédulas entregues:')

            for cedula in cedulas:
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f'{quantidade} cédula(s) de R${cedula}')
                    valor = valor % cedula

    except ValueError:
        print('Erro: Digite um valor numérico válido.')

if __name__ == "__main__":
    caixa_eletronico()

""""
Problema central: O problema central é criar um programa que simule um caixa eletrônico, onde o usuário pode digitar um valor a ser sacado e o programa deve calcular a quantidade de cédulas necessárias para entregar esse valor, utilizando as cédulas disponíveis (100, 50, 20, 10, 5 e 2). O programa também deve validar a entrada do usuário para garantir que seja um valor positivo e múltiplo de 2.
"""