
#print(dir(__builtins__))

print(pow(3,0)) #potÊncia

print(len("sdas")) #print tamanho da string

a= 'Gabriel '
b='3'
c=5
print(a+b) #concetenar string

print((a+'Netto\n')*5) #print * + numero de vezes que você quer printar a string

print(int(b)) #converte para int

print(a+str(c)) #converte para string
print('1 -------------------------------------------------')
name = ['Gabriel','gregorio','silveira','netto']
print(name)
print('Name',name[-1])
name.append("Computacao")
print(name)

print('2 -------------------------------------------------')

vetor = [11,23,55,12,90]
print('Vetor ->',vetor[0])

print('3 -------------------------------------------------')
name.extend(vetor) #concatena listas 
print(name[:5]) 
print(name[::2]) #printa a lista inteiro de 2 em 2

print('4 -------------------------------------------------')

a = int(input("Digite número:  "))
if a>10:
    print("maior que 10!")
else:
    print("menor que 10")

