# Namedtuple

from collections import namedtuple 

# Criamos uma tupla nomeada, bem parecida com um objeto 
# são realmente tuplas que possuem nomes e atributos e 
#  podemos acessar os seus valores por meio de seus nomes. 

Point = namedtuple('Point', 'x,y')


ponto_1 = Point(1, -4)
print(ponto_1.x, ponto_1.y)