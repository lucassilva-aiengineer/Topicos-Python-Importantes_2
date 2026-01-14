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


calculadora(2, valor_b= 10, valor_a= 0) # Os argumentos podem ser associados a uma ordem ou a um chave. 
