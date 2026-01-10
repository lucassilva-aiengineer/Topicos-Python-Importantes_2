# Decoradores. 


# @meu_decorador 
# def minha_funcao():
#     pass


def start_end_decorator(func):

    def wrapper():

        print('Início!')
        func()
        print('Final!')

    return wrapper 


@start_end_decorator
def imprimir_nome():
    print("Mateus")


# imprimir_nome = start_end_decorator(imprimir_nome)


# imprimir_nome() 


# Trabalhando com argumentos 


def meu_decorador(funcao):

    def wrapper(*args, **kwargs):

        print("Inicio da função...")
        resultado = funcao(*args, **kwargs)
        print("Final da função...")

        return resultado 

    return wrapper 

@meu_decorador 
def adicao(numero_a, numero_b):
    return numero_a + numero_b 



resultado = adicao(10, 20)
# print(resultado)

# print(help(adicao))

# print(adicao.__name__)

import functools 

def meu_decorador(funcao):

    """ Um função que altera o comportamento interno
        de outras funções. """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        print("Inicio da função...")
        resultado = funcao(*args, **kwargs)
        print("Final da função...")

        return resultado 

    return wrapper

# print(help(meu_decorador))

# print(help(meu_decorador.__name__))

# Um decorador que repete uma string um número determinado de vezes. 

def repeticao(vezes):
    def decorador_repeticao(funcao):

        @functools.wraps(funcao)
        def wrapper(*args, **kwargs):
            for numero in range(vezes):

                resultado = funcao(*args, **kwargs)

            return resultado 
        return wrapper 
    return decorador_repeticao 


@repeticao(10)
def imprimir_nome():
    print("Marcos")


imprimir_nome()