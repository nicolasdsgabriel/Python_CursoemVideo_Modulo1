km = float(input('Quantidade de km percorridos: '))
days = int(input('Quantidade de dias de uso: '))

kmpr = km * 0.15
dayspr = days * 60
total = kmpr + dayspr

print('O carro foi alocado por {0} dias e percorreu {1} km'
      '\nO preço por dias de alocação é igual a R${2}'
      '\nO preço por kilomêtros rodados é igual R${3}'
      '\nTotal a pagar: R${4}'.format(days, km, dayspr, kmpr, total))
