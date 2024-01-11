#programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado, depois calcula o preço a pagar
#sabendo que o carro custa 60 reais o dia e 0,15 reais por Km rodado
kms = float(input('Digite quantidade de Km percorridos: '))
dias = float(input('Digite a quantidade de dias que o carro foi usado: '))
print('De acordo com os valores informados, o valor a ser pago ser de R${:.2f}'.format( (kms * 0.15) + (dias * 60)))