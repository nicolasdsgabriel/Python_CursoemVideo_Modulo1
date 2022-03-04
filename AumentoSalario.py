sal = float(input('Informe seu salário: '))
aum = float(input('Informe a porcentagem de aumento: '))
perc = aum/100
total = sal + (sal * perc)

print('O salário {0} com {1} % de aumento é igual a {2}'.format(sal, aum, total))
