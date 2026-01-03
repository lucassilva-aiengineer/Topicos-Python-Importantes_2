# Collections 

from collections import Counter 


a = "aaaabbbccc"

# O objeto Counter se trata de um objeto que nos permite acessar um 
# dicionário tendo como chave cada elemento único como a chave do dicionário
# e a quantidade destes elementos como valor. 

meu_counter = Counter(a)
print(meu_counter)


print(type(meu_counter))

# Todos os valores do dicionário Counter
print(meu_counter.values())


# As chaves do dicionário Counter 
print(meu_counter.keys())


# Os dois elementos mais comuns 
print(meu_counter.most_common(2)[0][0])

# Uma lista com todos os elementos 
print(list(meu_counter.elements())) 



