#Exercício 1

nome = 'gabriel'
sobrenome_mae = 'silveira'
sobrenome_pai = 'netto'

iniciais = nome[0] + sobrenome_mae [0] + sobrenome_pai [0]
print(iniciais)

#Exercício 2

empresa = 'ufn'
nome = 'gabriel'
sobrenome_pai = 'netto'

email = nome+'.'+sobrenome_pai+'@'+empresa+'.com'
print(email)

idade = 9

if idade > 10:
    print("MAIOR QUE 10")
else:
    print("MENOR!!")

import math

print("Raiz quadrada de 9: ",math.sqrt(9))

num = int(input('Digite um numero:'))
print(type(num))
print("Fatorial de ",num,"é", math.factorial(num))


