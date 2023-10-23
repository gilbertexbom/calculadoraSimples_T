from calculadora import soma, sub, mult, div, rad, exp
from time import sleep


#  Implementação da calculadora simples

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora Simples --\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Exponenciação')
    print('6. Radiciação')
    print('7. Sair')

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

    elif op == 4:
        print('\nDivisão\n')

        # Entrada
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))
        if v2 == 0:
            print('Não é possível dividir por 0')
        else:
            # Processamento
            total = div(v1, v2)
            print(f'A divisão desses número será {total}')

        # Saída

    elif op == 5:
        print('\n\n\tOpção escolhida: EXPONENCIAÇÃO')
        v1 = float(input('Insira o valor da base: '))
        v2 = float(input('Insira o valor do expoente: '))
        print(f'O valor da operação de {v1:.2f} elevado a {v2:.2f} é igual a {exp(v1,v2)}')

    elif op == 6:
        print('\n\n\tRadiciação')
        v1 = int(input('Informe o valor 1: '))
        v2 = int(input('Informe o valor 2: '))

        total = rad(v1, v2)

        print(f'\n{v1} ** {v2} = {total}\n')

    elif op == 7:
        #Sair do sistema
        print('\nForte abraço e obrigado pela preferência!!\n')
        break

    else:
        #Tratamento de exceção
        print(f'\nOpção {op} incorreta!\n')

    stop = input('Deseja realizar outra operação? (Y/N) ').upper().strip()
    match stop:
        case 'Y':
            print('Sistema reiniciando, aguarde...')
            sleep(3)
            print('\n\n\n\t Sistema reiniciado!')

        case 'N':
            print('Forte abraço e obrigado pela preferência!!')
            break
