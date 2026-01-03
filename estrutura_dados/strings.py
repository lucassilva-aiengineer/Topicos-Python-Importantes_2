# Strings, são um tipo de dado ordenado e imutável 
# de representação de texto. 

minha_string = """O nome dele é \
Mateus. """

minha_string_2 = "Maça"

caracter = minha_string_2[0]

# print(caracter)

# print(minha_string)

substring = minha_string_2[2:4]
substring_2 = minha_string_2[:]

substring_3 = minha_string_2[::2]

print(substring)

print(substring_2)

print(substring_3)

palavra_1 = "Olá"
palavra_2 = "Usuário"

frase = palavra_1 + " " + palavra_2

print(frase)

for letra in minha_string: 
    print(letra)


if "O" in palavra_1:
    print("Sim")

else: 
    print("Não")

minha_string_3 = "   Hello world    "
nova_string = minha_string_3.strip()

print(minha_string_3.upper())
print(nova_string)

print(minha_string_3.lower())

print(minha_string_3.startswith("H"))

print(minha_string_3.endswith("d"))

print(minha_string_3.count("o"))

print(minha_string_3.replace("world", "mundo"))


minha_string_4 = "Qual é o seu nome?"
minha_lista = minha_string_4.split()

print(minha_lista)

nova_string_a = ' '.join(minha_lista)

print(nova_string_a)

nova_lista = ["a"] * 5 

print(nova_lista)

nova_string_b = ' '.join(nova_lista)
print(nova_string_b)


# Geito não tão legal   

minha_string_5 = ""

for letra in nova_lista:
    minha_string_5 += letra 

print(f"Minha string: {minha_string_5}")


# Formatação de strings. 

string_1 = "O meu nome é Lucas"
idade = 20.0000

frase = f"{string_1}, a minha idade é {idade:.2f} anos."

print(frase)