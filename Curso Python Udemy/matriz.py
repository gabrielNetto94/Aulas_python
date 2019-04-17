import random

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = random.randint(0, 10) #int(input("Digite valores"))

print('-='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'{matriz[l][c]}  ', end='')
        '''
        end=''
        usar com o comando "print"  para não quebrar linha
        
        '''
    print()