#FAÇA UM PROGRMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #FORMULA PARA SABER SE UM ANO É OU NÃO BISSEXTO
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))


