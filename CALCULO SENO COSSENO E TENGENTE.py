import math
an = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an,seno))
print('O ângulo de {} tem COSSENO DE {:.2f}'.format(an,co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,tan))
