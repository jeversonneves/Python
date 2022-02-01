for c in range(1,11):
  print(c)
print('Fim')

Resultado: 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10.

------------------------------------------

for x in range(1, 5):
  n = int(input('Digite um valor: '))
print('Fim')

Resultado: Pedi três entradas de números inteiros.

------------------------------------------

x = 1
while x != 0:
  x = int(input('Digite um valor: '))
print('Fim')

Resultado: Só finaliza o programa quando for digitado "0".

------------------------------------------

resposta = 'S'
while resposta == 'S':
  n = int(input('Digite um valor: '))
  resposta = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

Resultado: Enquanto a resposta for 'S' continua.
  
