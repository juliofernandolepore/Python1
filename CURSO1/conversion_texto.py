# conversion de numero a texto

numero = int(input('proporciona un valor entre 1 y 4: '))

numeroTexto = ''

if numero == 1:
    numeroTexto = 'numero 1'
elif numero == 2:
    numeroTexto = 'numero 2'
elif numero == 3:
    numeroTexto = 'numero 3'
elif numero == 4:
    numeroTexto = 'numero 4'
else:
    numeroTexto = 'no corresponde a la escala solicitada'

print(f"el valor ingresado {numero} - {numeroTexto}")
