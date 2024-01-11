#programa que lê a largura e altura de uma parede em metros e calcula a área e a quantidade de tinta
#sabendo que cada litro de tinta, pinta uma área de 2m²
largura = float(input('Qual é a largura da parede? (em metros) '))
altura = float(input('Qual é a altura da parede? (em metros) '))
print('a quantidade de tinta pra pintar a parede é: {}L'.format((largura * altura) / 2 ))