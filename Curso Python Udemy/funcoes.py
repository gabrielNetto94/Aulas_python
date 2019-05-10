def imc(altura, peso):
    imc = peso / (altura*altura)
    return imc


def classificaImc(imc):
    if imc < 19.1:
        print('Abaixo do peso')
    if imc >= 19.1 and imc <= 25.8:
        print('Peso normal')


def validaDado(dado):


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


altura = float(input('Digite altura: '))

imc = imc(altura, peso)
print('seu imc é: ', imc)
classificaImc(imc)
