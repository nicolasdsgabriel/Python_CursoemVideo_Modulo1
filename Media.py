nome = input('Informe seu nome completo: ')
test = float(input('Informe a nota da prova: '))
homework = float(input('Informe a nota da pesquisa: '))
seminar = float(input('Informe a nota do seminário: '))
med = (test + homework + seminar)/3

if med < 5:
    print('Aluno de nome {0}, possuí média {1}\nSituação: Reprovado'.format(nome, med))
else:
    print('Aluno de nome {0}, possuí média {1}\nSituação: Aprovado'.format(nome, med))