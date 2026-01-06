# Funções lambda. 

# São funções anônimas formadas por palavra chave 
# argumento e/ou expressão. 

adicionar_10 = lambda argumento: argumento + 10 
print(adicionar_10(20))

multiplicacao = lambda fator_a, fator_b : fator_a * fator_b 

print(multiplicacao(10, 5))


# São utilizadas como argumento de funções maiores. 

tuplas = [(1, 2), (15, 1), (5, -1), (10, 4)]
tuplas_ordenadas = sorted(tuplas)

tuplas_ordenadas_2 = sorted(tuplas, key= lambda tupla : tupla[1])

tuplas_ordenadas_soma = sorted(tuplas, key= lambda tupla : tupla[0] + tupla[1])

print(tuplas_ordenadas)
print(tuplas_ordenadas_2)

print(tuplas_ordenadas_soma)