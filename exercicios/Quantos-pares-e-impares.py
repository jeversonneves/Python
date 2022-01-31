n = 1
p = i = 0
while n != 0:
  n = int(input('Digite um valor: '))
  if n % 2 == 0:
    p += 1
  if n % 2 != 0:
    i += 1
print('Qtd de Pares: '.format(c))
print('Qtd de Impares: '.format(i))
