# Multiprocessamento VS Thread 

from multiprocessing import Process 
import os 
import time

# Isto é algo bem interessante. 

# Nós podemos realizar vários processos paralelamente. 

def numeros_ao_quadrado():

    for numero in range(0, 100):
        numero * numero 
        time.sleep(0.0)

processos = []
numero_processos = os.cpu_count() 

# print(os.cpu_count()) # Eu tenho do cpus funcionando. 



for cpu in range(numero_processos):
    processo = Process(target= numeros_ao_quadrado)
    processos.append(processo)


# Start 

for processo in processos: 
    processo.start()


# Junção 

for processo in processos: 
    processo.join()


print("FIM")

# for processo in processos:
#     print(processo)