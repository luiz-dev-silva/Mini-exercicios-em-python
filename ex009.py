tabuada = int(input('Digite um número e veja sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(tabuada, c, tabuada*c))