# trabajando con funciones lambda.
# es una funcion anonima y pequeña.
# son declaradas en una sola linea de codigo.
#no se requieren parentesis para los parametros y no se requiere la palabra return.

def sumar1(a , b):
    return a + b

print(f'el resultado de la suma es: {sumar1(10,5)}')

sumar_lambda = lambda b, c: b + c

resultado = sumar_lambda(10,60)

print(f'el resultado de sumar con funcion lambda es: {resultado}')

# funcion lambda sin argumentos

lambda_2 = lambda: 'funcion lambda sin argumentos, sintaxis muy simplificada'

print(f'mi funcion lambda sin argumentos contiene el string: {lambda_2()}')

# Parametros por default en una funcion lambda

lambda_3 = lambda a=20, b=30: a + b

print(f'los argumentos por defecto de la funcion lambda es {lambda_3()}')

print(f'los argumentos por defecto de la funcion lambda modificado {lambda_3(3,9)}')

# funcion lambda con argumentos variables (sumando los largos)
# **kwargs es un diccionario (sintaxis)

args_en_lambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(f'resultado de argumentos variables {args_en_lambda(1,2,3, llave1=5, llave2=8 )}')

# funciones lambda con argumentos variables y argumentos por defecto

mixta_lambda = lambda a, b, c=9, *tupla, **diccionario: a+b+c+len(tupla)+len(diccionario)

print(f'el resultado funcion lambda mista es: {mixta_lambda(2,3,4, 5,6,7 ,llave1=8, llave2=8)}')

# 2+3+4+(3)+(2) de esta forma se realiza la suma dentro de la funcion