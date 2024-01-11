from random import randint
pc = randint(1,5)
acertou = False

while acertou == False:
    user = int(input('tente advinhar o numero de 1 a 5 que eu pensei: '))
    if user > pc:
        print('Quase, tente um número menor...')
    elif user < pc: 
        print('Quase, tene um número maior...')
    elif user == pc:
        acertou = True
        print('Você acertou, Parabéns!')