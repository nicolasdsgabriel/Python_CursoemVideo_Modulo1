wallWidth = float(input('Informe a largura da parede: '))
wallHeight = float(input('Informe a altura da parede: '))
wallArea = wallWidth * wallHeight
ink = wallArea/2

print('A área total da parede é igual a {0} m²\nConsiderando que 1 litro de tinta pinta 2m²...\nSerá necessário um total de {1} litros para pintar a parede'. format(wallArea, ink))
