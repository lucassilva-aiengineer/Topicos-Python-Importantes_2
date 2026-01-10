import secrets 

# A geração de números aleatórios com a bíblioteca random pode não ser algo muito recomendado
# pois os números gerados com esta bíblioteca são números reproduzíveis ou seja, existe uma regra
# que permite a geração deste número, ou seja podemos repeti-los 

numero_a = secrets.randbelow(1000) # Um número aleatório, entre 0 e 10, não incluindo o 10. 

numeros_bits = secrets.randbits(10) # Gera um número aleatório que em representação binária consome 10 bits. 
# 1101000110 

lista_alfabeto = ["A", "B", "C", "D", "E"]

letra_aleatoria = secrets.choice(lista_alfabeto)

print(numero_a)
print(letra_aleatoria)

numero_aleatorios = [secrets.randbelow(100) for numero in range(0, 10)]
print(numero_aleatorios)
