
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
#############################################################################

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

#############################################################################
import random
megaSena = []

numero = int(input('quantos jogos vc qeur da mega? '))

for i in range(numero):
    for j in range(6):
        numero = random.randint(1,60)
        if numero not in megaSena:
            megaSena.append(numero)

    print('Jogo ',i+1,sorted(megaSena))
    megaSena = []


#############################################################################
import random

lista = [1,2,3,4,5,6,7,8,8]

print(lista)
print('shuffle')

#"embaralha a lista"
random.shuffle(lista)
print(lista)
#escolha 1 aleatoriamente
print(random.choice(lista))  

#pega uma amostra que vc determina
print(random.sample(lista,3))