print('Gerador de PA')
print('-=' * 10)

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão do PA: '))

termo = primeiroTermo
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
