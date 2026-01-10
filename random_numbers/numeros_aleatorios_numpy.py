import numpy as np 

array_numeros_aleatorios = np.random.rand(4)

print(array_numeros_aleatorios) 

matriz = np.random.rand(3, 3)

print(matriz)

# Números inteiros 

array_inteiros = np.random.randint(0, 10, 3)

print(array_inteiros)


# Matriz inteiros. 

matriz_inteiros = np.random.randint(0, 10 + 1, (3, 4))
print(matriz_inteiros) 

array_teste = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array_teste)

np.random.shuffle(array_teste)
print(array_teste)

# Também são números que podem ser reproduzidos, existe uma regra 
# de formação clara. 

np.random.seed(1)
print(np.random.rand(3, 3))

np.random.seed(1)
print(np.random.rand(3, 3))