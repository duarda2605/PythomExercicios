preco=float(input('Qual é  o preço do Produto?'))
desconto=(preco - preco*5/100)
print('O produto que custva R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco,desconto))
