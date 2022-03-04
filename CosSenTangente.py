from math import cosh, sinh, tanh

angle = float(input('Insira um ângulo: '))
cos = cosh(angle)
sen = sinh(angle)
tan = tanh(angle)

print('Cosseno desse ãngulo = {0}\nSeno desse ângulo = {1}\nTangente desse ângulo = {2}'.format(cos, sen, tan))