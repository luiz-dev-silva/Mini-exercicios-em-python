import random
aluno1 = str(input('Digite O nome do primeiro aluno: '))
aluno2 = str(input('Digite O nome do segundo aluno: '))
aluno3 = str(input('Digite O nome do terceiro aluno: '))
aluno4 = str(input('Digite O nome do quarto aluno: '))
lista_alunos = [aluno1,aluno2,aluno3,aluno4]
print('o aluno sorteado foi: {}'.format(random.choice(lista_alunos)))