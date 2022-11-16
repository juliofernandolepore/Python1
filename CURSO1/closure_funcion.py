# funciones closure: son funciones que encapsulan otras funciones, son funciones que
# definen otras.
# las funciones closure mantienen un estado. la funcion anidada o interna puede acceder a las variables
# locales de la funcion mas externa(principal).

def operacion(a, b):
    #definir una funcion interna o anidada( reutiliza variables locales externas a y b).
    def sumar():
        return a + b
    # utiliza las variables de los argumentos de la funcion externa a y b.
    #retorna la funcion.
    return sumar

mi_closure = operacion (5, 3)

print(f' resultado de la funcion mi_closure: {mi_closure()}')

# llamar la funcion al vuelo (llamando a la funcion mas externa).

print(f' resultado de la funcion mi_closure: {operacion(2,3)()}')