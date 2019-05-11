def imc(altura, peso):
    imc = peso / (altura*altura)

    if imc < 20:
        print(f'Imc: {imc:.2f} Abaixo do peso ')
    if imc >= 20 and imc <= 24.9:
        print(f'Imc: {imc:.2f} Peso normal ')
    if imc >= 25 and imc <= 29.9:
        print(f'Imc: {imc:.2f} Obesidade Leve ')
    if imc >= 30 and imc <= 39.9:
        print(f'Imc: {imc:.2f} Obesidade Moderada ')
    if imc > 40:
        print(f'Imc: {imc:.2f} Obesidade Mórbida')

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

imc(altura,peso)