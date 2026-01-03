from collections import deque 

# O deque é uma estrutura de dados muito interessante bem parecida 
# com listas que nos permite adicionar elementos a direita e a esquerda ou removermos 
# elementos da esquerda ou da direita, do fim ou do começo da nossa lista.


deque_a = deque()

deque_a.append(1)
deque_a.append(2)


deque_a.appendleft(3)
deque_a.append(5)

deque_a.pop()

deque_a.popleft()

deque_a.clear()

deque_a.extend([1, 2, 3, 4])

deque_a.extend([10, 11, 12, 13])

# Rotacionando 

deque_a.rotate(4)

print(deque_a)
