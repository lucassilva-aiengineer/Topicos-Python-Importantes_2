from itertools import accumulate 
import operator 


valores = [1, 2,5, 3, 4]

lista_acumulativa = accumulate(valores)

print(valores)

# Nós teremos a lista dos termos da lista somados uns aos 
# outros. 


print(list(lista_acumulativa))


# Podemos fazer com que a acumulação seja multiplicada. 

acumulacao_multiplicada = accumulate(valores, func= operator.mul)

# Tendo a lista multiplicada.
print(list(acumulacao_multiplicada))

acumulacao_max = accumulate(valores, func= max)


# Acumulação máxima.

print(list(acumulacao_max))