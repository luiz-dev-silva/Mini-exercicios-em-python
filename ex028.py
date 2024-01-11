from random import randint
pc = randint(1,5)
user = int(input('tente advinhar o numero de 1 a 5 que eu pensei: '))
if user == pc:
    print('parabéns você acetou!')
else:
    while user < pc or user > pc:
        user = int(input('quase, tente mais uma vez: '))
print('parabéns você acetou!')