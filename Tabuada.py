num = int(input('Informe um valor: '))

for count in range(10):
    print('{0} x {1} = {2}'.format(num, count+1, num * (count+1)))
