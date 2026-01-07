# Exceptions 

# Criando nossas próprias excessões 

def error_a():
    numeros = 10 

    if numeros % 10 == 0:
        raise Exception('O número não pode ser divísivel por 10.')



# Declarações assert 
# Caso a declaração seja verdadeira então a declaração será executada. 


def assert_a():

    numero = 300

    assert (numero >= 200), "O número deve ser maior ou igual a 200."


assert_a()


# try except. 

# try: 
#     a = 10 / 0 

# except:
#     print("Um erro foi detectado.")


# try:
#     a = 10 / 0

# except Exception as message:
#     print(message)



try: 

    a = 10 / 1
    b = 10 + "a"

except ZeroDivisionError as a:
    print(a)

except TypeError as a:
    print(a)

else: 

    print("O código foi finalizado com sucesso!")

finally: 
    print("O código foi finalizado.")


# Criando nossa própria classe de erro. 

class ValorMuitoAltoError(Exception):
    pass 



class ValorMuitoPequenoError(Exception):

    def __init__(self, message, value):
        self.message = message 
        self.value = value 


def testando_class(numero):

    if numero > 10 :
        raise ValorMuitoAltoError('Valor muito Alto.')

    if numero < 5:
        raise ValorMuitoPequenoError('Valor muito pequeno.', numero)



try: 
    testando_class(1)

except ValorMuitoAltoError as message: 
    print(message)

except ValorMuitoPequenoError as message:
    print(message.message, "valor", message.value)


numero = 10 
print(f"{numero = } ")