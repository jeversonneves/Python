'''from math import factorial

num = int(input('Digite um número para calcular seu Fatorial: '))

fatorial = factorial(num)

print('O fatorial de {}! é {}.'.format(num, fatorial))'''

# ---------------------------------------------------

n = int(input('Digite um número para calcular seu Fatorial: '))

contador = n
print('Calculando {}! = '.format(n), end='')
f = 1

while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print('{}'.format(f))

''' Utilizando o FOR
n = int(input('Digite um número: '))

c = n
f = 1

print('Calculando {}! = '.format(n), end='')

for i in range(1, n+1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))'''
