sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
  sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso')
elif sexo == 'F':
    print('Sexo Feminino registrado com sucesso')  
