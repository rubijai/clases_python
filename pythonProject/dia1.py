# VARIABLES-PRINT-INPUT
'''
Cuando (error cometido al escribir o teclear texto : typo) queremos escribir 
un comentario con varias líneas usamos:  ''' '''
Cuando queremos escribir un comentario con una sola línea usamos:

# "when we want to write a coment with just one line"

 Variables:una variable es un contenedor que se utiliza para almacenar valores.
 Puedes pensar en una variable como una caja etiquetada con
 un nombre en la que puedes guardar diferentes TIPOS de información,
 como números, cadenas de texto, listas u otros objetos.

 Tipos de variables: type: int (integer), float (flotantes) str (cadenas de texto)

 Números enteros (integer) no tienen cifras decimales:
 - 10 , 0, y 357 son enteros (integer data).

 Números flotantes (float)  tienen cifras decimales (floating-point data):
 1.3, -3.14, y 300.345567  son flotantes.

 "a" , "arte", "Jaime" '123' son cadenas de texto (str), 
 su valor siempre va entre comillas

Los comentarios no son ejecutables.
'''

# Mi primer programa de Python: imprimir el nombre, edad y estatura de una persona


'''  
 print(values,sep=' ',end = '\n') Es una función de python que imprime los valores
 de las variables separados por ' ' (un espacio) y que termina en un salto de línea
 end = '\n' (un salto de linea)
'''
nombre = 'Jaime'
edad = 77
estatura = 1.72
print(nombre, edad, estatura, sep=' ', end='\n')  # imprime los valores de las variables,
                                                  # separados por espacios
# print es una funcion propia(built-in function) de Python

print(nombre, edad, estatura)

#  f-strings permiten incluir expresiones dentro de las cadenas literales mediante
#  el uso de llaves {}. Da una forma de 'formatear' cadenas de texto.
datos1 = 'mi nombre es {nombre} y mi edad es {edad} años y mido {estatura} metros'
print(datos1)

datos = f'mi nombre es {nombre} y mi edad es {edad} años y mido {estatura} metros'
print(datos)
# si se quiere imprimir el nombre entre comillas:

# print(f'mi nombre es '{nombre}' y mi edad es {edad} años y mido {estatura} metros')
# Es necesario usar dos tipos de comillas, si uso el mismo tipo da error
print()  # imprime un salto de linea
print('John', 3 * 5, 6 * edad)

a = 3  # a la variable a se le asigna (=) el valor 3 en este caso
print(f'a = {a} {type(a)}')
# se imprime y lo que aparece en una llave corresponde
# al valor de la variable

print('a = ', a, type(a))  # no usa f string # imprime los valores de las variables
# que van separadas por comas. type(a) es una 'built in function' que imprime
# el tipo de la variable. Observe que la primera variable es un string con cuatro caracteres.

print('a =', a, type(a), sep=' ', end='\n')  # estos valores de sep=' ' y end='\n'
# vienen por defecto y no e necesario escribirlos solo se escriben si usa otros valores
print('a =', a, type(a), sep='-->', end='!')  # como  end != '\n' el print siguiente se
                                              # imprime en la misma linea y el separador es -->
print('a =', a, type(a), end='?')
print()  # imprime un salto de linea
# Al ejecutar los cuatro 'print' anteriores solo hay saltos de línea en el
# primer print y el último.

print(a, type(a))  # imprime el valor de las variables separados por un espacio
# Las variables en Python son dinámicas, lo que significa
# que no necesitas declarar explícitamente el TIPO de
# una variable antes de usarla.
# El tipo de la variable se infiere automáticamente según el valor que
# se le asigna. Esto permite que una misma variable pueda cambiar de
# tipo durante la ejecución del programa.

# En python algunos tipos de variables son: int, float, str, bool

a = 5.123456
print(f'a = {a:9.2f} {type(a)}')  # el formato de la variable a es 8 digitos con 2 decimales
# en este caso
# da como resultado 5.12. Usa 9 espacios y redondea
# print()


b = int(a)  # a es flotante b es entero toma la parte entera del numero

print(f'b = {b} {type(b)} a = {a} {type(a)} ')  # b es tipo entero y a es tipo flotante

c = float(b)  # c es flotante aquí se convierte de entero a flotante
print(f'c = {c} {type(c)}')

d = int(-a)  # -a es flotante d es entero toma la parte entera del numero
print(f'd = {d}  {type(d)}')
print()

d = 0.000143  # 6 cifras decimales
e = 1.43e-4  # numero escrito en forma exponencial
print(d == e)  # True -> bool  == es un operador boolean
e1 = True

print(f'd = {d} e1 = {e1} {type(e1)} ')
print()
f1 = 0.01
f2 = 0.001
f3 = 0.0001
f4 = 0.00001
f5 = 0.0000999
# f4 y f5 los imprime en forma exponencial porque son < 0.0001
print(f'f1 = {f1} f2 = {f2} f3 = {f3} f4 = {f4} f5 = {f5}')

f1 = 0.00001947  # 7 cifras decimales imprime en forma exponencial si el numero es < 0.0001

g = 19.47e-6  # imprime en forma exponencial porque es < 0.0001
x = 0.0001947  # > 0.0001 imprime en forma decimal
print(f'f1 = {f1} g = {g}  x = {x}')
print()

h = 0.12345678901234567890  # 20 cifras decimales ,
print(f'h = {h}')  # imprime maximo 16 cifras decimales (64 bit) y redondea

h1 = 1.12345678901234567890  # 20 cifras decimales
print(h1)

h2 = 2.12345678901234567890  # 20 cifras decimales ,
print(h2)

h3 = 3.12345678901234567890  # 20 cifras decimales ,
print(h3)

y = 1 / 2 ** (64)
z = 1 / 10 ** (16)
print(f'y = {y}  z = {z} {y < z}')

i = 12.12345678901234567890e-6
print('h =', h, 'i = ', i)
print(f'h = {h}')
print(f'h = {h:18.14g}')  # 14 cifras significativas (g),18 espacios y  redondea
print('Si encuentra algún error por favor comuníquelo')

print(f'h = {h:15.8f}')  # 8 cifras decimales (f),15 espacios y redondea

print(f'h = {h:15.8e}')  # exponencial con 8 cifras decimales(e), 15 espacios y redondea

print(f'h = {h:15.8f}')
print(f'h = {h:15.6f}')

a = 7.32
b = a + 5  # suma un tipo float y un tipo int y resulta un tipo float
print(f'b = {b} {type(b)}')

c = 5.32
# d = c + '5'                         suma un tipo float y un tipo str ('5') y resulta  en un TypeError
# nombres de variables en python

horas = 9
minutos = 8
segundos = 1

print(f'Esta es la hora  {horas:02d}:{minutos:02d}:{segundos:02d}')
# con este formato se imprimen las horas así: 01:02:59 o 19:08:01 se usa 02 para
# que si las horas, minutos o segundos son < 10, se imprima el 0. Si usaramos 03d
# para los segundos, por ejemplo (tres dígitos completados con ceros a la izquierda)
# tendríamos 01:02:059 o 09:08:001

balance_cuenta = 3485.50  # Es importante que las variables tengan nombres apropiados
# para que se sepa a que se refieren

temperatura = 40
print(f'Temperatura externa = {temperatura}')
print('Hello world!')

var1 = 22
var1 = -35
var1 = var1 + 335  # -35+335 = 300
# 7=var1                             #SyntaxError el nombre de la variable va en el lado
# izquierdo del comando y se asigna el valor del lado derecho

print(f'var1 = {var1}')
print()
print()

string_example = 'This is the text string'  # tipo str
print(string_example)

a = 'This'
b = 'is'
c = 'the'
d = 'text'
e = 'string'
f = a + b + c + d + e  # se pueden concatenar cadenas con el operador +
print(f'f = {f} {type(f)}')  # el tipo de la variable es str y es el resultado de la concatenación de las cadenas

a = 'This '  # en este caso el espacio forma parte de la cadena
b = 'is '
c = 'the '
d = 'text '
e = 'string '
f1 = a + b + c + d + e
print(f == f1)  # == es un operador relacional, si f == f1 --> True
# si f != f1 --> False (type bool)
print(f'f1 = {f1} {type(f1)}')
print()

# con input podemos entrar el valor de una variable  desde el teclado
city = input('Enter the name of the city where you are located: ')
# en este caso el valor de la variable city es de tipo str
print(f'city : {city} --> {type(city)}')
print()

temperature_str = input('Enter the temperature: ')  # el valor de la variable es de tipo str
print(f'temperature_str = {temperature_str}  {type(temperature_str)}')
print(type(temperature_str))
print()

temperature_int = int(input('Enter the temperature: '))  # el valor de la variable es de tipo int
print(f'temperature_int = {temperature_int}  {type(temperature_int)}')
print(type(temperature_int))
print()

temperature_float = float(input('Enter the temperature: '))  # el valor de la variable es de tipo float
print(f'temperature_float = {temperature_float}  {type(temperature_float)}')

print()
name = input('Enter your name:')
print(f'Hello {name}')

print('Hello ' + 'world')  # Hello tiene un espacio que forma parte de la cadena
# New lines can be created with a backslash and n (\n).)

print(3 * 'Jaime ')  # imprime la cadena tres veces en la misma linea
print(3 * 'Jaime\n')  # imprime la cadena tres veces en diferentes lineas

a = 3.4
print(f'a = {a} {type(a)}')

b = 3
print(f'b = {b} {type(b)}')
print()
c = 'name'
print(f'c = {c} {type(c)}')

a = 3
print(f'a = {a} {type(a)}')
print()
b = str(a)  # convierte una variable tipo int en variable tipo str
print(f'b = {b} {type(b)}')
print()

a = '75'
print(f'a = {a} {type(a)}')
b = int(a)  # convierte una variable tipo str en variable tipo int
print(f'b = {b} {type(b)}')
c = float(b)  # convierte una variable tipo int en variable tipo float
print(f'c = {c} {type(c)}')

# Desarrolla tu primer proyecto en python: crear el nombre de un equipo de futbol
# Debes entrar el nombre de la ciudad donde naciste  y una de las palabras Deportivo o Atletico
# por el teclado. Con estos dos elementos genera el nombre. Por ejemplo : Atletico Marinilla
