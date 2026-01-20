# Gerenciadores de contexto. 

#  Forma 1 

def teste()-> None:
    with open('lista_compras.txt', 'w') as file:

        file.write("""
    - Feijão. 
    - Macarrão.
    - Carne. 
    - Presunto. 
    - Pão. """)

def teste_2()-> None:
    file = open('coisas_a_fazer.txt', 'w')

    try: 
        file.write('-Terminar protótipo 1')

    finally:
        file.close()