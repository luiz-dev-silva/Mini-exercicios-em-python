#programa que lê um ângulo qualquer e mostra o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o valor do ângulo: '))
print('o seno de {} é {:.2f}\nO cosseno de {} é {:.2f}\nA tangente de {} é {:.2f}'.format(angulo,math.sin(math.radians(angulo)),angulo,math.cos(math.radians(angulo)),angulo,math.tan(math.radians(angulo))))