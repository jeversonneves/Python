primeiroValor = int(input('Primeiro valor: '))
segundoValor = int(input('Segundo valor: '))

sair = False

while not sair:
    print('')
    print('   [ 1 ] somar')
    print('   [ 2 ] multiplicar')
    print('   [ 3 ] maior')
    print('   [ 4 ] novos números')
    print('   [ 5 ] sair do programa')
    print('')
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
        primeiroValor = int(input('Primeiro valor: '))
        segundoValor = int(input('Segundo valor: '))
    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa! Volte sempre!')
