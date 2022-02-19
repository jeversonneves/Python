while True:
    numero = int(input('Quer ver a tabuada de qual valor: '))
    print(f'-' * 20)
    if numero < 0:
        print('Programa Tabuada Encerrado. Volte Sempre!')
        break
    for i in range(0, 10):
        i += 1
        multiplicacao = numero * i
        
        print(f'{numero} x {i} = {multiplicacao}')
    print(f'-' * 20)

