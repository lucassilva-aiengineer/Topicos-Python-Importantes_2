# Product
# Nos retorna o produto cartesiano relacionando valores 
# em listas. 

from itertools import product

lista_a = [1, 2]
lista_b = [3, 4]


produto_a = product(lista_a, lista_b, repeat= 2)


# Então temos uma lista com pontos cartesianos, pares ordenados 
# formados pelos pontos mensionados


print(list(produto_a))