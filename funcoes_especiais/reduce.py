# reduce()

from functools import reduce 

numeros = [1, 2, 3, 4, 5]


produto = reduce(lambda numero_a, numero_b : numero_a * numero_b, numeros)
print(produto)
