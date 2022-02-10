resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a soma foi de {} e media de {}.'.format(quant, soma, media))
print('O maior número {} e o menor número {}.'.format(maior, menor))
