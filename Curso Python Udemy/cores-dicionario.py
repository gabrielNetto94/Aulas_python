colors = {'red':'vermelho', 'verde':'green', 'blue':'azul'}
cor =  input('Type the color in portuguese, and see yours translation: ').lower() #MÉTODO lower() TRANSFORMA TUDO EM LETRA MINUSCULA
print(colors.get(cor,'Color not found!'))
colors['']