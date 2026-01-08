import json

# Jsons são muito parecido com dicionários e funcionam dentro desta estrutura de chave valor e podemos criar jsons 
# a partir de dicionários. 

pessoa_1 = {"nome": "Lucas", "idade": 20, "titulos": ["Engenheiro de Deep-Learning", "Ciêntista de Dados", "Engenheiro de Sistemas Inteligentes"]}

# indent= 4, indentação padão dos arquivos json.

# sort_keys= True, ordenando alfabeticamente as chaves do dicionário. 

json_pessoa = json.dumps(pessoa_1, indent= 4, sort_keys= True)

# print(type(json_pessoa))

# print(json_pessoa)

# Salvando o arquivo. 

# Criando um dicionário a partir de um dicionário. 

# with open('json_a/pessoa_1.json', 'w') as file: 
#     json.dump(pessoa_1, file, indent= 4)

# Convertendo um json, novamente a um dict. 

pessoa_dicionario = json.loads(json_pessoa)

print(type(pessoa_dicionario))

print(pessoa_dicionario)


# Lendo um arquivo Json em nosso diretório. 

with open('json_a/exemplo_1.json', 'r') as file:

    pessoa_1 = json.load(file)

print(pessoa_1)