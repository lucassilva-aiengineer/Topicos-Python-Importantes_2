from itertools import combinations 

# Nos retorna uma lista com todas as combinações 
# possíveis que podem ser geradas apartir de uma 
# lista de valores específicados, de um comprimento
# específico. 


valores = [1, 2, 3, 4]

combinacoes = combinations(valores, 2)

print(list(combinacoes))