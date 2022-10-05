#introducir valores en python
#alt 39 para imprimir comillas simples

nombre = input ("introduci tu nombre: ")
# f string interpolacion
print(f'hola {nombre}')

#ahora a convertir datos de entrada
numero_string = input("introduci un numero entero: ")
print(f' el numero ingresado es {numero_string} y es de tipo {type(numero_string)}')

#es necesario convertir el string a entero ya que el input recibe parametro string
numero = int(numero_string)
print(f' el numero ingresado es {numero} y es de tipo {type(numero)}')

#obtener un valor directamente entero en una sola linea
entero = int(input("introduci un numero entero nuevamente: "))
print(f' el numero ingresado es {entero} y es de tipo {type(entero)}')

#obtener un valor directamente float en una sola linea
flotante = float(input("introduci un numero flotantee: "))
print(f' el numero ingresado es {flotante} y es de tipo {type(flotante)}')