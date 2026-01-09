import json

# Jsons são muito parecido com dicionários e funcionam dentro desta estrutura de chave valor e podemos criar jsons 
# a partir de dicionários. 

pessoa_1 = {"nome": "Lucas", "idade": 20, "titulos": ["Engenheiro de Deep-Learning", "Ciêntista de Dados", "Engenheiro de Sistemas Inteligentes"]}

# indent= 4, indentação padão dos arquivos json.

# sort_keys= True, ordenando alfabeticamente as chaves do dicionário. 

# Criando um json por meior de um dicionário 

json_pessoa = json.dumps(pessoa_1, indent= 4, sort_keys= True)

# print(type(json_pessoa))

# print(json_pessoa)

# Salvando o arquivo. 

# Criando um json a partir de um dicionário. 

# with open('json_a/pessoa_1.json', 'w') as file: 
#     json.dump(pessoa_1, file, indent= 4)

# Convertendo um json, novamente a um dict. 

# pessoa_dicionario = json.loads(json_pessoa)

# print(type(pessoa_dicionario))

# print(pessoa_dicionario)


# Lendo um arquivo Json em nosso diretório. 

# with open('json_a/exemplo_1.json', 'r') as file:

#     pessoa_1 = json.load(file)

# print(pessoa_1) 


# Criando jsons a partir de objetos 

class Pessoa: 

    def __init__(self, nome, idade):

        self.nome = nome 
        self.idade = idade 


pessoa = Pessoa("Mateus", 20)

def encode_pessoa(objeto_pessoa):

    if isinstance(objeto_pessoa, Pessoa):
                                                                                    # Acessamos o nome da classe
        return {"nome": objeto_pessoa.nome, "idade": objeto_pessoa.idade, objeto_pessoa.__class__.__name__: True} 


    else:
        raise TypeError("O argumento passado deve ser uma instância da classe Pessoa.")


# json_objeto_pessoa = json.dumps(encode_pessoa(pessoa), indent= 4)

json_objeto_pessoa_2 = json.dumps(pessoa, default= encode_pessoa, indent= 4)


# Criando nossa própria classe padrão de encoder. 

from json import JSONEncoder
class PessoaEncoder(JSONEncoder):

    def default(self, o): 

        if isinstance(o, Pessoa):
            return {"nome": o.nome, "idade": o.idade, o.__class__.__name__: True}

        else: 
            return JSONEncoder.default(self, o)


objeto_pessoa_json = json.dumps(pessoa, cls= PessoaEncoder, indent= 4)

json_pessoa_3 = PessoaEncoder.encode(pessoa)

print(json_pessoa_3)

print(objeto_pessoa_json)

print(json_objeto_pessoa_2)
