#Autômato finito determinístico - prefixo 01 ou 10
def afd(palavra):
    estados = ['q0', 'q1', 'q2', 'q3', 'q4']
    alfabeto = set(['0', '1'])
    transicao = {
        'q0': {'1': 'q3', '0': 'q1'},
        'q1': {'0': '-', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q2'},
        'q3': {'0': 'q4', '1': '-'},
        'q4': {'0': 'q4', '1': 'q4'}}
    estadoInicial = 'q0'
    estadoFinal = ['q2', 'q4']
    estadoAtual = estadoInicial

    palavra += '#'
    for char in palavra:

        # teste se é fim de palavra
        if char == '#':
            # if estadoAtual == estadoFinal[0] or estadoAtual == estadoFinal[1]:
            if estadoAtual in estadoFinal:
                # if estadoAtual == estadoFinal:
                print('ACEITA', palavra[0:-1])
                break

        # testa se palavra é do alfabeto
        if char not in alfabeto and char != '#':
            print('REJEITA', palavra[0:-1], 'NÃO CONTÉM NO ALFABETO A LETRA: ', char)
            break

        # se estado for '-', rejeita pq não tem transição
        if estadoAtual == '-':
            print('REJEITA', palavra[0:-1])
            break
        temp = estadoAtual
        estadoAtual = transicao[estadoAtual][char]
        print(temp, ' com', char, 'vai para', estadoAtual)

while True:
    palavra = input("Digite palavra: ")
    afd(palavra)