from calculadora import soma, sub, mult, div


# Implementação da calculadora simples

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora Simples --\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

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
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))

        #Processamento
        total = sub(v1, v2)

        #Saída
        print(f'\n{v1} - {v2} = {total}\n')
    elif op== 3:
        print('\nMultiplicação\n')

        # Entrada
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))

        # Processamento
        total = mult(v1, v2)

        # Saída
        print(f'\n{v1} x {v2} = {total}\n')

    elif op== 4:
        print('\nDivisão\n')

        # Entrada
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))

        # Processamento
        total = div(v1, v2)

        # Saída
        print(f'\n{v1} / {v2} = {total}\n')

    elif op == 5:
        #Sair do sistema
        print('\nForte abraço e obrigado pela preferência!!\n')
        break
    else:
        #Tratamento de exceção
        print(f'\nOpção {op} incorreta!\n')