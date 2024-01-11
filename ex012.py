#lê o preço do produto e mostra o novo preço com 5% de desconto
produto = float(input('Digite valor do produto: R$'))
print('O valor do produto com 5 por cento de desconto é de R${:.2f}'. format( produto - ((produto * 5) / 100) ))