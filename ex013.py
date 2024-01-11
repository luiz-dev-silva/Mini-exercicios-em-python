#lê o salário de um funcionário e mostra o novo salário com 15% de aumento
salario = float(input('Digite o salário do funcionário: '))
print('O salário do funcionário teve um reajuste de 15 por cento, o novo salário agora é de R${:.2f}'.format(salario + ((salario * 15) / 100) ))