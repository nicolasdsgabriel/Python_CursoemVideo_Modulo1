num = float(input('Informe o preço do produto: '))
desc = float(input('Informe a porcentagem de desconto: '))
perc = desc/100
total = num - (num * perc)

print('{0} com {1} % de desconto fica um total de {2} R$'. format(num, desc, total))