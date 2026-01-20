# Operador Asterísco

# Multiplicção 

resultado_a = 10 * 5 

potenciacao = 10 * 2

print(resultado_a)
print(potenciacao)


tupla_zeros = (0, 5) * 10 
print(tupla_zeros)

lista_zeros = [0] * 10 
print(lista_zeros)

string = "AB" * 15 
print(string)


def funcao_exemplo(a, b, *args, **kwargs):

    print(a, b)
    for arg in args: 
        print(arg)

    for chave, valor in kwargs.items(): 
        print(f"""chave: {chave}
valor: {valor}""")

funcao_exemplo(10, 20, 30, 40, 50, 60, setenta= 70, oitenta= 80, noventa= 90)


# Impondo argumentos de palavra chave. 

def exemplo(a, b, *, c ): # Todos os argumentos após o asterísco devem ser argumentos de palavra chave

    print(a, b, c)

exemplo(10, 20, c= 40)


# Desmembramento de argumentos.

def exemplo_2(a, b, c):

    print(a, b, c)


lista = [1, 2, 3]
exemplo_2(*lista)

# Desempacotando um dicionário. 

def exemplo_3(a, b, c):

    print(a, b, c)

dicionario = {'a': 10, 'b': 20, 'c': 30}

exemplo_2(**dicionario)

# Desempacotando de lista 

numeros = [1, 2, 3, 4, 5, 6]

*primeiros_elementos, ultimos_elementos = numeros

print(primeiros_elementos)
print(ultimos_elementos)


numeros_a = (1, 2, 3, 4, 5, 6)

*primeiros_elementos, ultimos_elementos = numeros_a

print(primeiros_elementos)
print(ultimos_elementos)

numeros_b = (1, 2, 3, 4, 5, 6, 7)

inicio, *meio, fim = numeros_b 

print(inicio)
print(meio)
print(numeros_b)


minha_lista = [1, 2, 3]
minha_tupla = (1, 2, 3)

nova_lista = [*minha_lista, *minha_tupla]

print(nova_lista)

# Mesclando dicionários. 

dicionario_a = {'a': 1, 'b': 2}
dicionario_b = {'c': 3, 'd': 4}

dicionario_c = {**dicionario_a, **dicionario_b}
print(dicionario_c)

