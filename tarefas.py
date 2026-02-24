def gerenciador_tarefas():
    tarefas = []
    while True:
        print('\n1. Adicionar tarefa')
        print('2. Visualizar tarefas')
        print('3. Remover tarefa')
        print('4. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            tarefa = input('Digite a tarefa: ').strip()
            if tarefa: #Verifica se a string não está vazia
                tarefas.append(tarefa)
                print('Tarefa adicionada!')
            else:
                print('Tarefa não pode ser vazia!')
        elif opcao == '2':
            if tarefas:
                print('\nTarefas:')
                for i, tarefa in enumerate(tarefas, 1):
                    print(f'{i}. {tarefa}')
            else:
                print('Nenhuma tarefa cadastrada!')

        elif opcao == '3':
            if not tarefas:
                print('Erro: Nenhuma tarefa para remover.')
                continue

            try:
                indice = int(input('Digite o número da tarefa a ser removida: ')) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f'Tarefa "{removida}" removida!')
                else:
                    print('Erro: Número da tarefa inválido.')
            except ValueError:
                print('Erro: Entrada inválida. Por favor, digite um número.')

        elif opcao == '4':
            print('Saindo do gerenciador de tarefas. Até mais!')
            break
        else:
            print('Opção inválida! Por favor, escolha uma opção entre 1 e 4.')

if __name__ == "__main__":
    gerenciador_tarefas()


""""Problema central: O problema central é criar um gerenciador de tarefas simples, onde o usuário pode adicionar, visualizar e remover tarefas de uma lista, com tratamento de erros para entradas inválidas e opções inexistentes."""

