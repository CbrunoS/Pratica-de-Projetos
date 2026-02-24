def somar(num1, num2):
    return num1 + num2
 
def subtrair(num1, num2):
    return num1 - num2
 
def multiplicar(num1, num2):
    return num1 * num2
 
def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2

def calculadora():
    try:
        num1 = float(input('Digite o primeiro número: '))
        operacao = input('Escolha a operação (+, -, *, /): ')
        num2 = float(input('Digite o segundo número: '))

        if operacao == '+':
            resultado = somar(num1, num2)
        elif operacao == '-':
            resultado = subtrair(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = dividir(num1, num2)
        else:
            print('Operação inválida!')
            return
        
        print(f'Resultado: {resultado}')

    except ValueError:
        print('Entrada inválida! Por favor, apenas números.')
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')

if __name__ == "__main__":
    calculadora()


""""Problema central: O problema central é criar uma calculadora simples que permita ao usuário realizar operações básicas (adição, subtração, multiplicação e divisão) entre dois números, com tratamento de erros para entradas inválidas e divisão por zero."""