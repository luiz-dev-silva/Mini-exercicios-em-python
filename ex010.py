#programa que lê a quanto dinheiro uma pessoa tem na carteira e mostra a conversao em dolar
#considerando US$1,00 = R$3,27
valor = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com {:.2f} reais você pode comprar {:.2f} doláres'.format(valor, valor/3.27))