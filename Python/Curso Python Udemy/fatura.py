
repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')

    #validação da variável preco
    while valid_preco == False:
        preco = float(input('Digite o preço do produto: '))
        try:
            preco = float(preco)
            valid_preco = True
        except:
            print("Formato de preço inválido: ")

    fatura.append([produto,preco])
    total += preco
    valid_preco = False

    repetir = input('Deseja comprar mais algum produto? (S ou N) ').lower()

for i in fatura:
    print("Produto: "+i[0],'-'+" Valor R$ ",i[1])

print('O total da fatura é:',total)
