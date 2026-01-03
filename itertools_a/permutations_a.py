from itertools import permutations 

# Nos retorna todas as ordenações possíveis de nossas entradas. 

entrada = [1, 2, 3]
permutacoes = permutations(entrada, 2)

print(list(permutacoes))