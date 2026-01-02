# Listas 
# Listas são estruturas de dados mutáveis que permitem elementos dúplicados, 
# e aceitam uma quantidade indeterminada de elementos de diferentes tipos. 

minha_lista = ["banana", "cereja", "maça"]

print(minha_lista)

minha_lista_a = list()

print(minha_lista_a)

minha_lista_2 = [5, True, None, "Mateus", "Mateus"]

print(minha_lista_2[2])

print(minha_lista_2[-3])

for fruta in minha_lista:
    print(fruta)


if None in minha_lista_2:
    print("há uma elemento None na lista.")

tamanho_lista = len(minha_lista_2)
print(tamanho_lista)


minha_lista.append("Marcos")

print(minha_lista[-1])

# Adicionando elementos a um índice específico da lista 

minha_lista_2.insert(2,"Mateus")

print(minha_lista_2)

item_removido = minha_lista_2.pop()
print(item_removido)

print(minha_lista_2)


# Removendo Itens. 

# minha_lista_2.remove("Marcos")
# print(minha_lista_2) 


# Limpando a lista 

# minha_lista_2.clear()
print(minha_lista_2) 


# Revertento a lista

lista_em_reverso = minha_lista_2.reverse()

print(lista_em_reverso) 

lista_3 = [1, 5, 3, 2, 4, 9, 7, 8, 6]
print(lista_3)

lista_3.sort()

print(lista_3)

minha_lista_4 = [0] * 5

print(minha_lista_4)

lista_5 = [1, 2, 3, 4, 5, 6]

nova_lista = minha_lista_4 + lista_5 
print(nova_lista)

minha_lista_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = minha_lista_6[1: 5]
b = minha_lista_6[: 5]
c = minha_lista_6[1: ]


# A quantidade de passos percorridos padrão por uma lista 
#  é 1. 

print(minha_lista_6[::-1])
print(c)

lista_original = ["banana", "cereja", "maça"]

lita_copia = lista_original 

# Copiando de verdade 

lista_copia_a = list(lista_original)
lista_copia_b = lista_original[:]

print(lista_original)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_a = [numero * numero for numero in numeros]

numeros_a[0] = "Lucas"

print(numeros_a)