import random 

numero = random.random() # Um número float aleatório entre 0 e 1 


numero_b = random.uniform(2, 100) # Um número float entre um intervalo definido

numero_c = random.randint(2, 10) # Um número inteiro entre um intervalo específico, incluíndo o primeiro e o último valor definido. 

numero_d = random.randrange(1, 10) # Um número inteiro aleatório sem incluir o último valor do intervalo, um intervalo fechado em a e em b. 


# Selecionando um elemento aleatório na lista 

minha_Lista = list("ABCDEFGHIJKLMNO") 

print(random.choice(minha_Lista))


# Uma mostra aleatória de elementos em nossa lista. 

quantidade_especificada = 2 

amostra = random.sample(minha_Lista, quantidade_especificada)


print(amostra)

print(f"{numero_b:.2f}")

print(numero)

print(numero_c)

print(numero_d)

# Selecionando elementos aleatórios mais de uma vêz. 

minha_lista_a = ["A", "B", "C", "D", "E"]

quantidade_elementos_lista = 2
amostra_a = random.choices(minha_lista_a, k= quantidade_elementos_lista)

print(amostra_a)

# Embaralhando a lista 

random.shuffle(minha_lista_a)

print(quantidade_elementos_lista)