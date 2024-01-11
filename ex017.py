#programa que lê o comprimento do cateto oposto e do adjacente de um triângulo, calcula e mostra a hipotenusa
import math
cateto_oposto = int(input('Digite comprimento do cateto oposto: '))
cateto_adjacente = int(input('Digite comprimento do cateto adjacente: '))
#print('O valor da Hipotenusa é: {}'.format(((cateto_adjacente ** 2)+(cateto_oposto ** 2))**(1/2)))
print('O valor da Hipotenusa é: {}'.format(math.hypot(cateto_oposto,cateto_adjacente)))