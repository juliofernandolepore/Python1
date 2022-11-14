# Aprendiendo a crear clases en python.

# estructura de una clase (plantilla o template).
# def __init__(self): es el constructor

class Persona:
    nombre = '',
    apellido = '',
    edad = 0

    def __int__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludo(self):  # este def es un metodo de la clase
        print(f'hola como estas {self.nombre} {self.apellido}')
        print(f'{self.nombre} {self.apellido} tu edad es: {self.edad}')


# el uso del self se equipara al uso del this. en js


instancia = Persona()
instancia.nombre = 'fernando'
instancia.apellido = 'lepore'
instancia.edad = 39
print(instancia)

instancia.saludo()


# ahora defino otra clase EMPLEADOS que recibira la HERENCIA de la clase anterior(PERSONA)

class Empleados(Persona):
    sueldo = 0


    def salario(self, sueldo):
        print('tu salario es', self.sueldo)


empleado = Empleados()

empleado.nombre = 'francisco'
empleado.apellido = 'jimenez'
empleado.edad = 45
empleado.sueldo = 200000

empleado.saludo()
empleado.salario(5000)
