# Cópias 

import copy 

# Cópias superficiais vs cópias reais. 

lista = [1, 2, 3, 4, 5, 6]

copia_a = copy.copy(lista)

copia_a[0] = -15

copia_b = lista.copy()

print(lista)
print(copia_a)

copia_b[0] = -5

copia_c = list(copia_a)

# print(copia_b)

copia_c[2] = -10

print(copia_c)

copia_d = lista[:]

copia_d[4] = 10
print(copia_d)

# Como lista de profundidade 

lista_a =  [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10]]


copia_lista_a = copy.copy(lista_a)

copia_lista_a[0][1] = -10 


print(lista_a)      # As duas foram alteradas pois cópias superficiais copiam apenas o primeiro nível da lista .  
print(copia_lista_a)

# Copiando Objetos 

class Pessoa:

    def __init__(self, nome: str= "nome", idade: int= 10):

        self.nome = nome 
        self.idade = idade 


pessoa_1 = Pessoa("Mateus", 20)
pessoa_2 = copy.copy(pessoa_1)

pessoa_2.idade = 25 

print(pessoa_1.idade)
print(pessoa_2.idade) 
