from time import sleep

primeiroValor = int(input('Primeiro valor: '))
segundoValor = int(input('Segundo valor: '))

sair = False

while not sair:
    print('''
    
       [ 1 ] somar
       [ 2 ] multiplicar
       [ 3 ] maior
       [ 4 ] novos números
       [ 5 ] sair do programa
       
    ''')
    
    menu = int(input('>>> Qual é a sua opção? '))

    if menu == 5:
        sair = True
        print('Finalizando...')
    elif menu == 1:
        soma = primeiroValor + segundoValor
        print('A soma de {} + {} é igual a {}'.format(primeiroValor, segundoValor, soma))
    elif menu == 2:
        mult = primeiroValor * segundoValor
        print('A multiplicação de {} x {} é igual a {}'.format(primeiroValor, segundoValor, mult))
    elif menu == 3:
        if primeiroValor > segundoValor:
            maior = primeiroValor
        else:
            maior = segundoValor
            print('O maior entre {} e {} é {}'.format(primeiroValor, segundoValor, maior))
    elif menu == 4:
        print('Informe os números novamente:')
        primeiroValor = int(input('Primeiro valor: '))
        segundoValor = int(input('Segundo valor: '))
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
