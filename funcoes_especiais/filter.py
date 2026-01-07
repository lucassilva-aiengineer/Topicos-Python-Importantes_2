# Função filter()

numeros = [1, 2, 3, 4, 5]

numeros_filtrados = filter(lambda numero : numero % 2 == 0, numeros)

print(list(numeros_filtrados))

list_compression = [numero % 2 == 0 for numero in numeros]
print(list_compression)