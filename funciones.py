# TRABAJANDO CON PYTHON ejercicios con funciones

def suma(n1, n2, n3):
    return n1 + n2 + n3

print(suma(80, 2, 15))

def saludo(nombre, apellido):
    print(f'hola como estas {nombre} {apellido}')

saludo('fer','lepore')

def saludo2(nombre='juan', apellido='fernandez'):
    print(f'hola como estas {nombre} {apellido}')

#aqui le pase variables con valores por defecto en los parametros de la funcion.
saludo2()

saludo2('javi','malay')

