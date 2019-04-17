i=0; j=0

arq = open('C:/Users/18911/Google Drive/Python/teste.txt', 'r')
texto = arq.readlines()

for linha in texto:
	data_list = list(linha)
	a = linha.split(',')
	print(linha[1],linha[2])
	#print(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
	i+=1 
	arq.close()

print('Linhas contadas =',i)
print('***',*data_list)
print('while')
while(j<10):
	print(data_list[j])
	j+=1

'''
print("Lendo o documento...")
with open("C:/Users/18911/Downloads/teste.txt", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

'''