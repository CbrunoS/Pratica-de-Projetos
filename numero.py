import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input('Tente adivinhar o número entre 1 e 100: '))

            if not 1 <= palpite <= 100:
                raise ValueError('Número fora do intervalo! Digite um número entre 1 e 100.')
            tentativas += 1

            if palpite < numero_secreto:
                print('Muito baixo! Tente novamente.')
            elif palpite > numero_secreto:
                print('Muito alto! Tente novamente.')
            else:
                print(f'Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.')
                break

        except ValueError as e:
            print(f'Entrada inválida: {e}')

if __name__ == "__main__":
    adivinhar_numero()


""""
Problema central: O problema central é criar um jogo de adivinhação de números, onde o usuário deve adivinhar um número secreto gerado aleatoriamente entre 1 e 100. O programa deve fornecer feedback sobre se o palpite do usuário é muito alto, muito baixo ou correto, e contar o número de tentativas."""