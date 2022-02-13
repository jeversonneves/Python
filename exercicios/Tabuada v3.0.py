n = resultado = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-' * 30)
    for i in range(1, 11):
        resultado = n * i
        print(f'{n} x {i} = {resultado}')
