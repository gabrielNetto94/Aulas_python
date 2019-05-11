import funcaoImc as f
#importa o arquivo func.py e atribui a variavel 'f' para ele

validaDado = False
while validaDado == False:
    peso = input('Digite seu peso: ')
    try:
        peso = float(peso)
        if peso <= 0:
            print('Número deve maior que 0')
        else:
            validaDado = True
    except:
        print('Digite somento número!')

validaDado = False
while validaDado == False:
    altura = input('Digite altura: ')
    try:
        altura = float(altura)
        if altura <= 0:
            print('Número deve maior que 0')
        else:
            validaDado = True
    except:
        print('Digite somento número!')

f.imc(altura,peso)