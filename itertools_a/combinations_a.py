from itertools import combinations, combinations_with_replacement 

# Nos retorna uma lista com todas as combinações 
# possíveis que podem ser geradas apartir de uma 
# lista de valores específicados, de um comprimento
# específico. 


valores = [1, 2, 3, 4]

combinacoes = combinations(valores, 2)

print(list(combinacoes))


# Agora podemos ter o mesmo termo no primeiro e segundo índices. 
combinacoes_com_substitutos = combinations_with_replacement(valores, 2)

print(list(combinacoes_com_substitutos))