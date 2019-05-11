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
