# Função map()

# A função map percorre um iteravel de valores executando uma função e 
# cria uma nova lista com os valores retornados. 

numeros = [1, 2, 3, 4, 5]

numeros_multiplicados = map(lambda numero: numero * 2, numeros)

print(list(numeros_multiplicados))

list_compression = [numero * 2 for numero in numeros]
print(list_compression)