# Dicionarios 

meu_dicionario = {"nome": "Levi", "Cidade": "Atlanta", "idade": 30, "carro": "SW4"}

print(meu_dicionario)

meu_dicionario_1 = dict(nome="Roberto", idade= "20", cidade= "Goiânia")
print(meu_dicionario_1)

# Acessando valores 

valor = meu_dicionario["nome"]
print(valor)

# Adicionando chaves 

meu_dicionario_1["pais"] = "Brazil"

print(meu_dicionario_1)

# del meu_dicionario_1["Cidade"]
# print(meu_dicionario)


# meu_dicionario.pop("idade")

# print(meu_dicionario)

# meu_dicionario.popitem()

# print(meu_dicionario)

if "nome" in meu_dicionario:

    print(meu_dicionario["nome"])

try:
    print(meu_dicionario["cpf"])

except Exception as a:
    print("Notificação: ", a)
    print("Não temos cpf")



for chave in meu_dicionario_1:
    print(chave)


# Imprimindo chave junto do valor 

for chave, valor in meu_dicionario_1.items():
    print("Chave: ", chave)
    print("Valor: ", valor)


dicionario_copia = meu_dicionario_1.copy()
dicionario_copia_1 = dict(meu_dicionario_1)

print(dicionario_copia)

print(dicionario_copia_1)

meu_dicionario_1.update(meu_dicionario)

print(meu_dicionario)
print(meu_dicionario_1)


# Chaves aceitas. 
# As chaves aceitas são apenas tipo de dados imutáveis

chaves_demonstracao = {1: 10, 2: 30}
print(chaves_demonstracao)  

minha_tupla = (1, 2)

meu_dicionario_2 = {minha_tupla: 5}

print(meu_dicionario_2)
