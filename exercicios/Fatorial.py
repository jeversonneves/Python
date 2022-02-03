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
