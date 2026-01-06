from itertools import count, cycle, repeat 
import random


for numero in count(10):
    print(numero)

    if numero == 15:
        break 



lista_numeros = [1, 2, 3, 4]

for numero in cycle(lista_numeros):
    print(numero)

    if numero == 4:

        break 



for numero in repeat(1, 10):

    print(numero)


lista_numero_1 = [numero + 5 if random.randint(0, 9) % 2 == 0 else numero for numero in repeat(10, 100)]
print(lista_numero_1)