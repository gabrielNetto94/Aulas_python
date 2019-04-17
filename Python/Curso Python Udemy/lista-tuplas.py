
#DECLARAÇÃO E INSERÇÃO TUPLAS E LISTAS

#tupla começa com (
meses = ('janeiro','fevereiro','março','abril','maio','junho','julho')
print(type(meses))
print(meses)

#lista começa com [
alunos = ['joao','maria','pedro','gabriel','fulano']
alunos1 = ['marta','thales','rafael','ana','andressa']

print('Tipo de dado: ',type(alunos))
print("Tamanho Lista:",len(alunos))
print('Lista Original',alunos)


#ALTERAR PELO ÍNDICE
alunos[3] = 'joao pedro'
print(alunos)

#ADICIONAR AO FINAL DA LISTA
alunos.append('amanda')
print(alunos)

#ADICIONA PELA ÍNDICE
alunos.insert(0,'novo nome')
print(alunos)

#ORDENAR LISTA
print(alunos.sort())

#REMOVE POR ÍNDICE
alunos.pop(3)

#CONCATENAR
print(alunos+alunos1)