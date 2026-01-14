# Generators
# Geradores
import sys

def my_generator():

    yield 3
    yield 2 
    yield 1 


generator = my_generator()

# for i in generator:
#     print(i)

# valor = next(generator)

# print(valor)

# valor = next(generator)
# print(valor)

# valor = next(generator)
# print(valor)

#  Somando os geradores 

# print(sum(generator))

# print(sorted(generator)) 

# Exemplo de contagem regressiva. 

def contagem_regressiva(numero):
    print('Começo!')

    while numero > 0:
        yield numero 
        # numero = numero - 1 
        numero -= 1


def teste():

    contagem_r = contagem_regressiva(5)

    valor = next(contagem_r)
    print(valor)

    valor = next(contagem_r)
    print(valor)

    valor = next(contagem_r)
    print(valor)

# Os generators são muito úteis na econômia de memória. 

def lista_numeros(alvo):

    numeros = []
    numero = 0

    while numero < alvo:

        numeros.append(numero)
        numero += 1

    return numeros

# Da seguinte maneira podemos economizar bastante memória. 
# pois não precisamos de armazenar todos os números em uma mtriz. 


def numeros_generators(alvo):
    numero = 0

    while numero < alvo:
        yield numero 
        numero += 1

print(sum(numeros_generators(10)))


def fibocacci(alvo):

    a, b = 0, 1 

    while a < alvo:

        yield a 
        a, b = b, b + a


# print(list(fibocacci(10)))

fibonacci_a = fibocacci(10)

for numero_temporario in fibonacci_a:
    print(numero_temporario)

# Sequência de Fibonacci 

# 1 (1 + 2) = 3 (2 + 3) = 5 (3 + 5) = 8 (8 + 5) = 13 

# Compression de geradores. 

meu_gerador = (numero for numero in range(0, 1000) if numero % 2 == 0)
# print(list(meu_gerador))

# print(list(meu_gerador))

minha_lista = [numero for numero in range(0, 1000) if numero % 2 == 0]

print("Meu gerador: ")
print(sys.getsizeof(meu_gerador))

print("Minha lista: ")
print(sys.getsizeof(minha_lista))