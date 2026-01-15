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
