from itertools import groupby 


def menor_que(parametro):

    return parametro < 3


menor_que_f = lambda numero: numero < 3

valores = [1, 2, 3, 4]


grupo_objetos = groupby(valores, key= menor_que_f)


# Agrupamos valores que seguem a um critério. 

for chave, valor in grupo_objetos: 
    print(chave, list(valor))


# print(list(grupo_objetos)) 


pessoas = [{"nome" : "Mateus", "idade" : 25}, {"nome" : "Marcos", "idade" : 25},
            {"nome" : "João", "idade" : 30}, {"nome" : "Lucas", "idade" : 15}]


idade_maior_que = lambda pessoas: pessoas["idade"] > 20

def idade_maior_que_20(dicionario):
    return dicionario["idade"] > 20 



objetos_grupos = groupby(pessoas, key= idade_maior_que)

for chave, valores in objetos_grupos: 
    print(chave, list(valores))


grupo_objetos_idade = groupby(pessoas, key= lambda dicionario: dicionario["idade"])

for chave, valores in grupo_objetos_idade:
    print(chave, list(valores))