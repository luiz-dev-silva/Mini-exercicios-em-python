#programa que converte uma temperatura de C° em F°
temperatura_celcius = float(input('informe temperatura em C°: '))
print('A temperatura {}C° convertida pra F° é: {}F°'.format(temperatura_celcius,((temperatura_celcius * 9) / 5) + 32))