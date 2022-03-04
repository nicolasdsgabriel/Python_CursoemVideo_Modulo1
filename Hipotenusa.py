from math import sqrt, pow

oposto = float(input('Informe o valor do cateto oposto: '))
adjacente = float(input('Informe o valor do cateto adjacente: '))
catetos_sum = pow(oposto, 2) + pow(adjacente, 2)
hipotenusa = sqrt(catetos_sum)

print('O valor da hipotenusa é igual a {0}'.format(hipotenusa))