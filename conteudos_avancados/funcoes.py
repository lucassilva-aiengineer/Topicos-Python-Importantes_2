# Funções 

# Parâmetros VS argumentos. 

# Argumentos/parametros: São funções  


# Temos um parâmetro na definição da função 
def imprimir_nome(parametro):
    print(parametro)


# Temos um argumento quando chamamos a função. 
# imprimir_nome("argumento")

# Argumentos posicionais. 

def imprimir_nomes(nome_a, nome_b, nome_c):

    print(nome_a, nome_c, nome_b)

# imprimir_nomes("Mateus", "Marcos", "Levi") 

# Arumgumentos de Palavra Chave. 

def imprimir_nome_b(nome_a, nome_b, nome_c):

    print(nome_a, nome_b, nome_c)


# imprimir_nome_b(nome_a= "Nome_1", nome_c= "Nome_2", nome_b= "Nome_3") 


def calculadora(operacao, valor_a, valor_b):


    if operacao == 1:

        resultado = valor_a + valor_b 

        print("Resultado: ", resultado)

    elif operacao == 2:

        resultado = valor_a / valor_b 

        print("Resultado: ", resultado)


# calculadora(2, valor_b= 10, valor_a= 0) # Os argumentos podem ser associados a uma ordem ou a um chave. 

# Agumentos padrão 

def funcao(argumento= 4):

    print("Argumento: ", argumento)


funcao(5)
funcao()

def fator_a(*argumentos, argumento_a):

    for argumento in argumentos:
        
        if argumento == 5: 
            continue 

        print(argumento)

        if argumento == 4:
            break 

    # Entramos neste else apenas quando terminarmos os loops. 
    else: 

        print(argumento_a)

fator_a(10, 4, 5, 6, 10, argumento_a= 100)

# Desempacotamento 

def funcao_b(a, b, c):

    print(a, b, c)


lista = [1, 2, 3]

funcao_b(*lista)


meu_dicionario = {'a': [10, 12, 13, 15, 17, 18], 'b': [10, 12, 14, 17, 18, 19], 'c': [20, 13, 40, 54]}


funcao_b(**meu_dicionario)


# Escopo de um função 


numero = 10 # Variável Global 

def funcao_a()-> None: # Retornando um tipo None

    global numero # Agora declaramos que a variável que nós estamos acessando é a variável de escopo global, então conseguimos 
    # altera-la localmente. 

    global numero # Variável global 

    numero_a = 10 # Variável local. 

    numero += 1 # Nós chamamos, mas não acessamos a variável global, nós criamos uma nova variável chamada numero 
    # localmente. 

    # Acessamos localmente, pois a variável é local 
    print(numero)

# teste_1 = funcao_a()
# print(teste_1) 


funcao_a()

# print(numero) # Não foi alterada. 

print(numero) # Depois de acessarmos a variável localmente na função.  

# Objetos imutáveis não podem ser alterados

def exemplo():

    minha_lista.append(5)
    minha_lista[0] = 10
    print(minha_lista)

minha_lista = [1, 2, 3, 4, 5]

exemplo()

def exemplo_1():

    global minha_lista # Temos que declarar que a variável é gloabal para acessa-las 
    # no interior da função. 

    minha_lista = minha_lista + [10, 20, 30]    
    return minha_lista

print(exemplo_1())