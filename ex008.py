#programa que lê um valor em metros e é convertido em centímetros e milímetros
valor = float(input('Digite valor em metros: '))
print('O valor {} em metros convertido pra cm e mm é, respectivamente: {}cm e {}mm'.format(valor, valor *100, valor*1000))