
#colors = {'red':'vermelho', 'verde':'green', 'blue':'azul'}
#cor =  input('Type the color in portuguese, and see yours translation: ').lower() #MÉTODO lower() TRANSFORMA TUDO EM LETRA MINUSCULA
#print(colors.get(cor,'Color not found!'))
#colors['']

#DECLARACAO DICIONARIO , É POSSÍVEL INSERIR LISTA DENTRO DO DICIONARIO
joao = {'nome': 'joao', 'sobrenome': 'silva', 'profissao': 'programador python','filhos': ['pedro','maria']}

print(joao['profissao'])
print(joao['filhos'])

#TAMANHO
print(len(joao))

#ALTERAR VALORES
joao ['profissao'] = 'aposentado'

#DELETAR ITENS DO DICIONARIO
#del joao['filhos']

#PESQUISA ITENS EXISTENTES NO DOCIONARIO
print('sobrenome' in joao)

#PERCORRER DICIONARIO
for x in joao:
    print(x+': '+joao[x])

#PESQUISA ITEM NO DICIONARIO  parâmetros do método .get (item dicionario, mensagem caso não encontre)
print(joao.get('ome','Não encontrado!'))

#ADICONAR ITEM NA LISTA DENTRO DO DICIONARIO
joao['filhos'].append('gabriel')
print(joao)

#LIMPAR VALORES DA LISTA
joao.clear()