# TRABAJANDO CON PYTHON ejercicios con funciones

def suma(n1, n2, n3):
    return n1 + n2 + n3

resultado = suma(5,10,40)

print(f' el resultado es {resultado}')

def saludo(nombre, apellido):
    print(f'hola como estas {nombre} {apellido}')

saludo('fer','lepore')

def saludo2(nombre='juan', apellido='fernandez'):
    print(f'hola como estas {nombre} {apellido}')

#aqui le pase variables con valores por defecto en los parametros de la funcion.
saludo2()

saludo2('javi','malay')

"""funciones con parametros por defecto"""

def sumar_2(a:int = 0, b: int = 2) -> int:
    return a + b

resultado_sumar2 = sumar_2()

print(f'el resultado con parametros por defecto es: {resultado_sumar2}')

"""ARGUMENTOS VARIABLES EN FUNCIONES (se va a iterar como una tupla)"""

"""los argumentos variables se puede encontrar definido como *args"""

def lista_de_nombres(*argumentos_varios):
    for itera in argumentos_varios:
        print(itera)

lista_de_nombres('tomas','pedro','joaquin')
lista_de_nombres('mariel','vanesa','juana')

"""ejercicio sumar con argumentos variables"""
"""la indexacion es muy importante sinio provoca serios errores en las funciones"""
def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(f'la suma total de argumentos es: {resultado}')

sumar_valores(9,6,4,6,8,8,0,9)
