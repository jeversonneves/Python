from random import randint

computador = randint(0,10)

contador = 0

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

while True:
    numero = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I]: ')).upper()[0]

    soma = numero + computador

    if (soma % 2) == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    
    print('-' * 25)
    print(f'Você jogou {numero} e o computador {computador}. Total de {soma} DEU {resultado}')
    print('-' * 25)

    if escolha == resultado[0]:
        print('Você VENCEU!')
        contador += 1
    else:
        print('Você PERDEU!')
        break
    print('=-' * 20)

print(f'GAME OVER! Você venceu {contador} vezes.')
