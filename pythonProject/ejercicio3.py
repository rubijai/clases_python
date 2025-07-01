
# Creo una estructura para los clientes
class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaré ambas estructuras

# Creo un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)

'''
==LISTADO DE CLIENTES==
[<__main__.Cliente object at 0x0000023F567B42E8>,
<__main__.Cliente object at 0x0000023F567B4320>]

==MOSTRAR CLIENTES POR DNI==
Hector Costa Guzman
Cliente no encontrado

==BORRAR CLIENTES POR DNI==
Cliente no encontrado
Juan Gonzalez Marquez > BORRADO

==LISTADO DE CLIENTES==
[<__main__.Cliente object at 0x0000023F567B42E8>]
'''

def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return




'''
En Python, enumerate es una función incorporada que se utiliza para iterar 
sobre una secuencia (como una lista, tupla o cadena) y obtener tanto el 
índice como el valor de cada elemento de la secuencia en cada iteración. 
La función enumerate devuelve un objeto enumerado que contiene 
pares de (índice, valor) para cada elemento en la secuencia.

Sintaxis:

python
Copy code
enumerate(iterable, start=0)
Parámetros:

iterable: La secuencia sobre la que se va a iterar.
start: El valor inicial del índice. Por defecto es 0.
Ejemplo de código:

python
Copy code
# Ejemplo 1: Iterar sobre una lista con enumerate
frutas = ['manzana', 'naranja', 'plátano', 'pera']

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

# Salida:
# Índice: 0, Fruta: manzana
# Índice: 1, Fruta: naranja
# Índice: 2, Fruta: plátano
# Índice: 3, Fruta: pera

# Ejemplo 2: Especificar un valor inicial para el índice
colores = ['rojo', 'verde', 'azul']

for indice, color in enumerate(colores, start=1):
    print(f"Índice: {indice}, Color: {color}")

# Salida:
# Índice: 1, Color: rojo
# Índice: 2, Color: verde
# Índice: 3, Color: azul

# Ejemplo 3: Usar enumerate con cadenas de texto
mensaje = "Hola, mundo!"

for indice, caracter in enumerate(mensaje):
    print(f"Índice: {indice}, Caracter: {caracter}")

# Salida:
# Índice: 0, Caracter: H
# Índice: 1, Caracter: o
# Índice: 2, Caracter: l
# Índice: 3, Caracter: a
# Índice: 4, Caracter: ,
# Índice: 5, Caracter:  
# Índice: 6, Caracter: m
# Índice: 7, Caracter: u
# Índice: 8, Caracter: n
# Índice: 9, Caracter: d
# Índice: 10, Caracter: o
# Índice: 11, Caracter: !

Como puedes ver en los ejemplos anteriores, enumerate es útil cuando necesitas tanto el valor como el 
índice de los elementos mientras recorres una secuencia

dni = '22222222B'
print(c[dni])
n_clist = [clientes.remove(clientes[1]) for i,c in enumerate(clientes) if dni == c['dni']]
print(f'n_clist={n_clist}')
for i, c in enumerate(clientes):
    print(i,c)

'''
l = [1,2,3,4,5,6]
n_l = [n*n for n in l if n>2]
print(n_l)