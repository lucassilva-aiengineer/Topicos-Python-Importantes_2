# Tuplas 
# As tuplas são muito parecidas com as listas, são estruturas de dados 
# que podem armazenar uma quantidade indeterminada de termos de diferentes tipos, porém 
# as tuplas são declaradas entre parentêses e são imutáveis, também permitem dados dúplicados. 


minha_tupla = ("Nome", 10, 3.5)
print(minha_tupla)

tupla_a = ("Mateus", )
print(type(tupla_a))

tupla_b = "Marcos", "Lucas", 10, 1, 1
print(tupla_b)

print(tupla_a[0])


for valor in minha_tupla:
    print(valor)


if "Lucas" in tupla_b:
    print("SIm!")

else:

    print("O Lucas não está nesta lista.")

print(len(tupla_a))


print(tupla_b.count(1))



print(tupla_a.index("Mateus"))

print(tupla_a.index("Mateus")) if "Mateus" in tupla_a else None 



# Convertendo tupla em lista 

minha_tupla_3 = (1, 2, 3, 4, 5, 6, 7)

minha_lista = list(minha_tupla)

nova_tupla = tuple(minha_lista)

print(minha_lista)

print("Minha tupla: ")
print(nova_tupla)

fatiamento = minha_tupla_3[2: 5]

print(fatiamento)

reverse = fatiamento[::-1]

print(reverse)

# Desempacotamento 

# tupla_4 = "Mateus", 20, "Floryda"

# nome, idade, cidade = tupla_4

# print("Nome: ", nome)
# print("Idade: ", idade)
# print("Cidade: ", cidade)

# Desempacotando vários itens 

minha_tupla_5 = (0, 1, 2, 7, 8)

primeiro_valor_a, *valor_meio_a, ultimo_valor_a = minha_tupla_5

print(f"Primeiro valor: {primeiro_valor_a}")
print(f"Valor do meio: {ultimo_valor_a}")
print(f"Último valor: {ultimo_valor_a}")


# Comparando tuplas e listas 
import sys 

minha_lista = [0, 1, 2, 3, 4]
minha_tupla = (0, 1, 2, 3, 4)

print(sys.getsizeof(minha_lista), "bytes")
print(sys.getsizeof(minha_tupla), "bytes")

import timeit 

print(timeit.timeit(stmt= "[0, 1, 2, 4, 5]", number= 1000000))
print(timeit.timeit(stmt= "(0, 1, 2, 4, 5)", number= 1000000))
