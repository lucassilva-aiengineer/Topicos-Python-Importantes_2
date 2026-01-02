meu_conjunto = {1, 2, 3, 1, 2}
print(meu_conjunto)

meu_conjunto_1 = set([1, 2, 3, 4, 5])
print(meu_conjunto_1)


# Os conjuntos são 

meu_conjunto_2 = set("Olá")
print(meu_conjunto_2)

meu_conjunto_3 = set([2])
meu_conjunto_3.add(1)

print(meu_conjunto_3)

# meu_conjunto_3.remove(2)

# meu_conjunto.discard(10)


print(meu_conjunto_3)

for elemento in meu_conjunto_3:
    print(elemento)

if 1 in meu_conjunto_3:
    print("Sim")


# Uniões e intersseções 

impares = {1, 3, 5, 7}
pares = {2, 4, 6, 8, 10}
primos = {2, 3, 5, 7, 11}

uniao = impares.union(pares)

# Temos sem duplicação os números que aperecem ou no primeiro conjunto ou 
# no segundo conjunto. 

print(uniao)

# Temos os números que aparecem no primeiro e no segundo conjunto ao mesmo tempo. 
intercessao = impares.intersection(impares)

print(intercessao)

# Diferença entre conjuntos. 

conjunto_a = {1, 2, 3, 4, 5, 6, 7, 8, 15}
conjunto_b = {1, 2, 3, 4, 5, 6, 8, 9, 10, 11}

# Só fica o que a no conjunto a que não há no conjunto b
diferenca = conjunto_a.difference(conjunto_b)

print(diferenca)

# Diferença simétrica. 
# A diferença simétrica retorna todos os elementos que não aparecem nos dois comparados 

diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)

print(diferenca_simetrica)

# Atualizando os conjuntos 
# Fazendo com que o segundo conjunto tenha também os elementos do primeiro. 

conjunto_a.update(conjunto_b)

print(conjunto_a)


# Atualiza o conjunto mantendo os elementos que aparecem apenas em ambos os conjuntos. 
conjunto_a.intersection_update(conjunto_b)

print(conjunto_a)


# Este método mantém apenas os elementos encontrados no conjunto a e no conjunto b, 
# mas não em ambos. 
conjunto_a.symmetric_difference_update(conjunto_b)
print(conjunto_b)


# issubset()
# Esta função verifica se o conjunto b é um subconjunto do conjunto a. 

print(conjunto_a.issubset(conjunto_b))


# Disjunção de conjuntos 

print(conjunto_a.isdisjoint(conjunto_b))

# Cópia de conjuntos 

copia = set(conjunto_b)
copia_1 = conjunto_b.copy()

print(copia)


