from collections import defaultdict

# Defaultdict são como dicionários padrão porém 
# que possuem chaves padrão que servem para buscas 
# em momentos em que estas chaves ainda não foram adicionadas. 

dicionario_padrao = defaultdict(float)

dicionario_padrao['a'] = 1
dicionario_padrao['b'] = 2
dicionario_padrao['c'] = 3 


print(dicionario_padrao['a'])
print(dicionario_padrao['A'])