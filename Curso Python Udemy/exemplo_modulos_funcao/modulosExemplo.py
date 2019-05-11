import math
#arredonda pra cima
print(math.ceil(3.8))
#arredonda pra baixo
print(math.floor(3.7))
#somatorio
n = [1,2,3,56,12]
#fsum recebe lista como parametro
print(math.fsum(n))
print(math.sqrt(16))

import time as t
#todas as informações como , dia, hora,minuto,seg etc.
print(t.localtime())
#print exemplo
print('Hora -> ',t.localtime().tm_hour,':',t.localtime().tm_min)
#clock do processador

input('Após pressionar "ENTER" digite seu nome o mais rápido que conseguir ')
ini = t.perf_counter()
oi = input('Digite seu nome: ')
fim = t.perf_counter()
print('Seu tempo foi de :',(fim-ini))
