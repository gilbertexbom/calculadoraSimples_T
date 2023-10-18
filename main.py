from calculadora import soma


# Implementação da calculadora simples

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora Simples --\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Sair')

    # Ler a opção de escolha do usuário
    op = int(input('\n\tOpção: '))

    if op == 1:
        print('\nSoma\n')

        #Entrada
        v1 = int(input('Informe o valor1: '))
        v2 = int(input('Informe o valor2: '))

        #Processamento
        total = soma(v1,v2)

        #Saída
        print(f'\n{v1} + {v2} = {total}\n')

    elif op == 2:
        print('\nSubtração\n')

        #Entrada

        #Processamento

        #Saída

    elif op == 3:
        # Sair do sistema
        print('Forte abraço!')
        break
    else:
        #Tratamento de exceção
        print(f'\nOpção {op} incorreta!\n')