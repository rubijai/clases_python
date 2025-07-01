# Python Lists

# Creando Listas
# Una lista es una estructura de datos capaz de almacenar diferentes
# tipos de datos.

a = 2
# dir(variable) da una lista de los métodos asociados a variable
print(dir(a))        #luego explicaremos el concepto de métodos en python
b = 3
alist_examp = [1, 3.4, 'asdf', 96, True, 9.6, 'zxcv', False, 2 > 5, a + b]
print(f'alist_examp = {alist_examp}, type(alist_examp) = {type(alist_examp)}')
print(f'alist_examp contiene {len(alist_examp)}  elementos')

# Observa que la lista contiene datos de tipo bool, int, str y float.
# También contiene el resultado de operaciones relacionales y aritméticas.
# Cualquier tipo de dato válido en Python puede ser colocado dentro
# de una lista.
# Los datos contenidos dentro de la lista se llaman elementos.
# La lista que has impreso contiene 10 elementos.
# Puedes contarlos manualmente para verificarlo. También existe una funcion
# llamada len que te dará esta información, como se muestra en el ejemplo.
# len es un funcion muy útil.
# Presta mucha atención a la sintaxis utilizada para construir la lista.
# El paréntesis cuadrado izquierdo/paréntesis cuadrado derecho se
# conoce como un "contenedor".
# Los elementos deben separarse por comas al construir la lista.
# Cada elemento de esta lista tiene un índice de 0 a 9, en este caso.

# diferentes formas de copiar  una  lista:

lista1 = alist_examp
lista2 = alist_examp.copy()
lista3 = alist_examp[:]

print(f'alist_examp = {alist_examp}')
print(f'lista1 =      {lista1}')
print(f'lista2 =      {lista2}')
print(f'lista3 =      {lista3}')
print(f'lista1 == alist_examp --> {lista1 == alist_examp}')
print(f'lista2 == alist_examp --> {lista2 == alist_examp}')
print(f'lista3 == alist_examp --> {lista3 == alist_examp}')

print()

# Todas las listas anteriores tienen los mismos elementos
# y son mutables, es decir, se pueden cambiar sus elementos.

lista1[2] = 'Jerry'    # cambia el elemento de la lista1 que tiene el índice 2
print(f'alist_examp = {alist_examp}')
print(f'lista1 =      {lista1}')
print(f'lista2 =      {lista2}')
print(f'lista3 =      {lista3}')

print(f'lista1 == alist_examp --> {lista1 == alist_examp}')
print(f'lista2 == alist_examp --> {lista2 == alist_examp}')
print(f'lista3 == alist_examp --> {lista3 == alist_examp}')
print()

lista2[2] = 'Jim'
print(f'alist_examp = {alist_examp}')
print(f'lista1 =      {lista1}')
print(f'lista2 =      {lista2}')
print(f'lista3 =      {lista3}')

print(f'lista1 == alist_examp --> {lista1 == alist_examp}')
print(f'lista2 == alist_examp --> {lista2 == alist_examp}')
print(f'lista3 == alist_examp --> {lista3 == alist_examp}')

print(lista2[9])         # imprime el elemento de la lista2 con el índice 8
print()


# Observa que al cambiar el elemento 2 de lista1  también
# se cambia el elemento 2 de alist_examp.
# Python considera que ambas variables ocupan el mismo espacio en memoria.
# Son nombres diferentes que se refieren a los mismos datos.
# Entonces, ¿cómo podemos asignar realmente la lista a una nueva variable
# que ocupe un lugar diferente en la memoria y se pueda modificar de forma
# independiente a la variable alist_examp?
# Para asignar la lista a una nueva
# variable independiente, puedes utilizar el método de copia.
# Python proporciona dos tipos de copia para las listas:
# copia superficial (shallow copy) y copia profunda (deep copy).
# Copia profunda:
# Utiliza el operador de rebanado [:] o el método copy() para crear
# una copia profunda de la lista.



# el comando "alist_examp.copy()" es tu primera introducción a
# la sintaxis orientada a objetos.
# La parte "copy()" de este comando es lo que se conoce como un método.
# Está conectado a la variable "alist_examp" utilizando la notación de
# punto o 'dot notation'.
# Este comando crea una copia 'profunda' de la variable "alist_examp" para
# que las modificaciones de las copias no afecten a "alist_examp".
#
# Cada tipo de variable en Python es lo que se conoce como un "objeto".
# Aprenderás una cantidad inmensa sobre objetos a medida que profundicemos
# en el curso. El punto principal a tener en cuenta es que hay varios métodos
# disponibles para usar con listas. El método de copia que acabamos de
# introducir es uno de ellos. Algunos otros métodos importantes que vale
# la pena mencionar en este punto son pop, append, remove e insert.'''

print(f'alist_examp[0] = {alist_examp[0]}')    # imprime el elemento
                                               # con el índice 0 --> 1
print(alist_examp[1])
print(alist_examp[2])
print(alist_examp[3])
print(alist_examp[4])
print(alist_examp[5])
print(alist_examp[6])
print(alist_examp[7])
print(alist_examp[8])
print(alist_examp[9])
print()


# Los elementos contenidos dentro de una lista pueden ser
# referenciados utilizando lo que se conoce como un índice.
# Observa que Python comienza los índices a partir de un valor de cero.
# Entonces, si una lista tiene 10 elementos, el primer elemento
# de la lista se referencia utilizando un índice de 0 y
# el último elemento se referencia con un valor de 9.

# Un error común al comenzar a usar listas es intentar ejecutar un
# comando como:
# print(alist_examp[10])

# Este error ocurre porque estás intentando acceder al elemento de la lista
# utilizando un índice fuera de rango. Recuerda que los índices de una
# lista comienzan desde 0, por lo que el índice máximo permitido para
# una lista con 10 elementos sería 9.

# Si intentas acceder a un índice fuera del rango válido, Python lanzará
# un error de índice fuera de rango (IndexError). Asegúrate de utilizar
# índices válidos dentro del rango de la lista para acceder a sus elementos.

# print(alist_examp[10]) produce el error de índice fuera de rango
print()

# El índice es la clave para referirse a un elemento dentro de una lista.

c = 3 + alist_examp[1]
alist_examp[1] = c + alist_examp[0]    # alist_examp[1] tiene que ser
                                       # int o float
print(c)
print(f'alist_examp = {alist_examp}')
alist_examp[1] = alist_examp[1] + alist_examp[4] + alist_examp[8]
print(f'alist_examp = {alist_examp}')
print()

# ¿Qué pasaría si tuviéramos una lista con 1000 elementos y
# quisiéramos mostrarlos todos uno por uno? ¿Tendríamos que escribir
# 1000 comandos?
#
# No, no tendrías que escribir 1000 comandos para mostrar los elementos de una
# lista uno por uno. En su lugar, puedes utilizar un bucle para iterar
# sobre los elementos de la lista y mostrarlos.
#
# Por ejemplo, puedes usar un bucle "for" para iterar sobre la lista y
# mostrar cada elemento:

for x in alist_examp:
    print(f'x = {x}')     # la variable x va tomando los valores de los
                          # elementos de la lista alist_examp

# Otra forma de imprimirlos es:

for i in range(len(alist_examp)):
    print(f'alist_examp[{i}] = {alist_examp[i]}')

print()

# Recuerda que cualquier tipo de dato válido en Python puede ser
# insertado en una lista. Las listas son un tipo de dato válido,
# por lo tanto, es posible tener una lista que contenga listas.

# Por ejemplo, puedes tener una lista que contenga sublistas de la
# siguiente manera:


lista_principal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'len(lista_principal) = {len(lista_principal)}')
# En este caso, lista_principal es una lista que contiene tres sublistas.
# Cada sublista puede contener cualquier tipo de elemento, incluyendo
# otras listas.

# Tener listas que contienen listas es útil para estructurar y organizar datos
# de forma jerárquica. Puedes acceder a los elementos de las
# sublistas utilizando índices adicionales.

# Por ejemplo, para acceder al elemento 5 en la lista lista_principal,
# puedes usar el siguiente código:


elemento = lista_principal[1][1]
print(f'elemento = {elemento}')  # Salida: 5

# Aquí, lista_principal[1] se refiere a la segunda sublista dentro
# de lista_principal, y lista_principal[1][1] se refiere al segundo
# elemento dentro de esa sublista.

# Qué impimiria con el siguiente script?
for i in range(3):
    for j in range(3):
        print(f'lista_principal[{i}][{j}] = {lista_principal[i][j]}')

x = [3, 4, 5.5, 6, 7.9]
y = [-300, 3.14]
z = [x, y, 3.45678]
print()
print(f'z = {z}, len(z) = {len(z)}')

print(f'The list z contains {len(z)}  elements : 2 lists and 1 float number')
print()
for i in range(len(z)):
    print(f'Element with index  {i} =  {z[i]}')
print()

# Después de ejecutar este código, deberías ver que la lista z
# contiene 3 elementos. Las listas x e y se consideran anidadas
# dentro de la lista z. Por lo tanto, para indexar elementos
# dentro de estas listas, se requerirá un segundo índice de la
# siguiente manera:

print(f'z[0][2] = {z[0][2]}')
print(f'z[1][0] = {z[1][0]}')

for j in range(len(x)):
    print(f'z[0][{j}] = {z[0][j]}')

print()

# Una característica muy útil de Python es su capacidad para hacer
# referencia a elementos en bucles sin la necesidad de hacer referencia
# a un índice.

for value in z:
    print(f'value = {value}')
print()

# En este ejemplo, la variable "value" itera a través de todos los
# valores en la lista "z" sin necesidad de crear un índice real.
# Esta es una característica muy poderosa en el lenguaje de
# programación Python.

# Página de Slicing

# A menudo ocurre que un programa requiere hacer referencia a un grupo de
# elementos dentro de una lista en lugar de un solo elemento utilizando un
# solo valor de índice. Esto se puede lograr mediante el uso de "slicing"
# o rebanado.
#
# El slicing es una técnica que permite extraer un subconjunto de elementos de
# una lista especificando un rango de índices. El rango de índices se
# especifica utilizando la sintaxis [inicio:fin:incremento], donde "inicio" es
# el índice del primer elemento a incluir y "fin" es el índice del
# primer elemento a excluir. El 'incremento' es el salto.
# Es importante destacar que el rango de índices se especifica como
# [inicio:fin:incremento],y tienen la misma interpretación que vimos al
# explicar la función range(inicio, fin, incremento) solo que
# la sintaxis es diferente.

# Por ejemplo, si tenemos la siguiente lista:

mi_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Podemos extraer un subconjunto de elementos utilizando el slicing
# de la siguiente manera:


subconjunto = mi_lista[2:6]  # Extrae los elementos desde el índice
# 2 hasta el índice 5 (excluyendo el indice 6)
print(f'subconjunto =       {subconjunto}')  # Imprime [30, 40, 50, 60]
print(f'mi_lista    = {mi_lista}')
# En este caso, el slicing selecciona los elementos con índices 2, 3, 4 y 5 de
# la lista mi_lista y los asigna a la variable subconjunto.

# El slicing proporciona una forma conveniente de trabajar con subconjuntos de
# elementos en una lista sin necesidad de utilizar bucles o referencias
# individuales a los elementos. Es una herramienta poderosa para manipular y
# extraer datos de manera eficiente.


x = [101, -45, 34, -300, 8, 9, -3, 22, 5]
print(f'len(x) = {len(x)}')
print(x)
print(x[0:9])        # Imprime todos los elementos del 0 al 8
print()

# El operador de dos puntos (:) se puede utilizar para indexar múltiples
# elementos dentro de una lista. El índice en el lado izquierdo del operador
# de dos puntos (:) es el índice de inicio. Según la convención de
# indexación de Python, el valor en el lado derecho del operador
# de dos puntos (:) indexa ese valor menos uno (ten cuidado con el
# índice derecho).
# Dado que la variable "x" tiene 9 elementos indexados del 0 al 8, "x[0:9]"
# hace referencia a todos los índices del 0 al 8.
print()
print(x[3:4])
print(x[3:5])
print(x[3:6])
print(x[3:7])
print(x[3:8])
print(x[3:9])
print()

print()
print(x[3:])      # imprime desde el indice 3 hasta el indice final(incluido)
print(x[:4])      # imprime desde el indice 0 hasta el indice 3
print()

# Además de especificar los índices de inicio y fin,
# también puedes especificar el "incremento" (step). Aquí tienes
# un ejemplo que cuenta de dos en dos desde el elemento 3 hasta
# el elemento 7 (cada otro elemento a partir del índice 3).
# El tamaño del paso se indica con el valor del índice después
# del segundo operador de  dos puntos (:).


print(f'x = {x}')
print(f'x[3:8:2] = {x[3:8:2]}')  # Imprime los elementos del
                                 # 3 al 7 de dos en dos
print()

# Python permite el uso de índices negativos donde, por convención,
# el índice -1 implica empezar desde el final de la lista.


print(f'x[-1] = {x[-1]}')  # Imprime el último elemento de la lista (x[-1])
print(f'x[-1:-3:-1] = {x[-1:-3:-1]}')  #
print(f'x[-1:-len(x) - 1:-1] = {x[-1:-len(x) - 1:-1]}')
print()

# Las listas son mutables, lo que significa que una vez creadas,
# como ya hemos visto, los elementos contenidos en una lista pueden
# ser cambiados y actualizados.
# Las cadenas de texto son objetos inmutables, lo que significa que
# los elementos de una cadena de texto no pueden ser cambiados.


a = 'asdf'
print(a[1])
#a[1]='3'            # Este ejemplo genera un error debido a que intenta
                     # cambiar un objeto que  no se pueden cambiar.
                     # Las cadenas son inmutables.
for letra in a:      # a es una cadena, el nombre de la variable confunde
    print(letra)
a = 'good'
b = 'morning'
c = a + b
print(f'c = {c} len(a) = {len(a)} len(c) = {len(c)}')
print(len(c))
print()

a = 'good '
b = 'morning'
c = a + b
print(f'c = {c}    len(c) = {len(c)}')

print(dir(a))
# imprime: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit',
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
# 'upper', 'zfill']
#
# Existen una serie de métodos disponibles para procesar objetos de
# cadena de texto. Puedes explorar el cambio a mayúsculas y minúsculas
# utilizando los métodos de upper() y lower(), respectivamente

a = 'good'
print(a,type(a))
c = a.upper()
d = c.lower()
print(f'c = {c}    len(c) = {len(c)}')
print(f'd = {d}    len(d) = {len(d)}')
print(f'a = {a}    len(a) = {len(a)}')


# Para unir una lista de cadenas de texto con un espacio entre ellas,
# puedes utilizar el método join() de las cadenas de texto. Aquí tienes
# un ejemplo:
# a.join(iterable) a es el elemento mediante el cual vas a unir los
# elementos del iterable

b = 'morning'
print([a, b, 'today'])
e = ' '.join([a, b, 'today'])               # el resultado es una
                                            # cadena : good morning today
print(f'e = {e}         len(e) = {len(e)}')
# a.join(iterable) a es el elemento mediante el cual vas a unir
# los elementos del iterable.

f = '-->'.join([a, b, 'today'])
print(f'f = {f}          len(f) = {len(f)}') # el resultado es una
                                             # cadena: good-->morning-->today
print()
print(' '.join(['a','b','c']))               # el resultado es una
                                             # cadena: a b c
g = ' '.join(['a','b','c'])

print(f'g = {g}')           # el resultado es una cadena: a b c
print(g.split(' '))         # el resultado es una lista: ['a', 'b', 'c']
                            # cada vez que hay un espacio entra un
                            # nuevo elemento de la lista
                            # si no encuetra espacios en la cadena,
                            # el resultado es una lista con un solo elemento

g1 = g.split('->')
print(f'g1 = {g1}')         # el resultado es una lista : ['a b c']
                            # no encontró el separador '->'
                            # el resultado es una lista: ['a', 'b', 'c']

# g1 genera una lista de cadenas cuyos elementos son cadenas obtenidas
# de la separación de la cadena g en donde se encuentre el elemento de
# separación '->'

# Encontrar una cadena dentro de otra cadena
# El método find() devuelve el primer índice donde se encontró la cadena.

x = 'una imagen vale más que mil palabras'
x1 = x.find('imagen')                        #el resultado es : 4
print(f'x1 = {x1}')                          #el resultado es : 4    x1)
x2 = x.find('vale')                          #el resultado es : 11
print(x2)
x3 = x.find('s')
print(x3)

# Probar el método replace ... remplaza 'mil' por 'un millón de'
z = x.replace('mil', 'un millón de')
print(x)
print(z)

# Dividir una cadena en una lista de cadenas más pequeñas
# Utilizamos el espacio (' ') como límite (delimitador) para dividir la cadena.
y = x.split(' ')
print(f'y = {y}    type(y) --> {type(y)}')
print(type(y))

w = f.split('-->')
print(f'w = {w}      type(w) --> {type(w)}')    # el resultado es una lista

# Hay muchas formas de crear listas. La mas sencilla es encerrando
# los elementos en paréntesis cuadrados [].

a_lista = [10, 20, 30, 40]
b_lista = ['crunchy frog', 'ram bladder', 'lark vomit']
c_lista = ['spam', 2.0, 5, [10, 20]]

# una lista que no contiene elementos es una lista vacía.
# Ud. puede  crear una lista vacía así : [].

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123, 67]
empty = []
print(cheeses, numbers, empty)

# Las listas son mutables.
# La sintaxis para acceder a los elementos de una lista es la misma que
# para acceder a los elementos de una cadena de texto.
# lista[i] la expresión dentro de corchetes especifica el índice.
# Recuerda que los índices comienzan en 0.

numbers[1] = 5
print(numbers)

# Los indices de las listas funcionan iguales que los indices de
# las cadenas de texto.
# Los indices de las listas son enteros.
# Si trata de acceder a un elemento que no existe, Python produce un
# IndexError.
# Si el índice es negativo, Python cuenta los elementos de la lista
# de atras hacia delante.
# El operador in funciona de la misma manera en listas.

print('Edam' in cheeses) #imprime True

print('Brie' in cheeses) #imprime False

# Recorriendo una lista con un for loop.
# la función len() devuelve el número de elementos de la lista.


for cheese in cheeses:
    print(cheese)

# Esto funciona bien si solo se requiere leer los elementos de la lista.
# Pero si quieres escribir o actualizar la lista, necesitas los índices.
# Una forma de hacerlo es con las funciones len y range.

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(f'numbers = {numbers}')
print()

# otra forma de hacerlo es usando list comprehensions:


#  list comprehension
#  es una forma elegante y concisa de construir listas nuevas
#  al aplicar una expresión o condición a cada elemento de una
#  lista o secuencia existente. Su objetivo es simplificar el código,
#  haciéndolo más legible y, en muchos casos, más eficiente.

# Formato de  list comprehension:

# nueva_lista = [expresión for elemento in lista (or in range) if condición]

# expresión: me permite determinar el valor del elemento.
# Ejemplo de expresión: i**2 , donde i es parte de un rango de valores
# por ejemplo: range(1,21) y ademas podemos usar una condición que el
# valor de i sea par, por ejemplo. Veamos la construcción de la lista:

a = [i**2 for i in range(1,21) if i % 2 == 0]
print(f'a = {a}')

# Esta misma lista la hubiéramos podido crear así:
a = []
for i in range(1,21):
    if i % 2 == 0:
        a.append(i**2)
print(f'a = {a}')



# También podemos construir una nueva lista a partir de una lista anterior.
# Por ejemplo: construyamos una lista 'b', a partir de la lista 'a':

b = [x for x in a if x<= 100]
print(f'b= {b}')
# o de esta forma:
b = []
for x in a:
    if x<= 100:
        b.append(x)
print(f'b= {b}')

n_numbers = [numbers[i]*2 for i in range(len(numbers))]
print(f'n_numbers = {n_numbers}')
n_numbers1 = [x*2 for x in numbers if x>20]
print(f'n_numbers1 = {n_numbers1}')

# Un bucle sobre una lista vacía no produce ninguna salida.
for x in []:
    print('This never happens.')

# Una lista puede contener otras listas. Las listas pueden ser anidadas.
# Las listas anidadas cuentan como un elemento individual.

print(len(['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]))

# Operaciones con listas.
# El operador + concatena listas.


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)       # imprime [1, 2, 3, 4, 5, 6]

# El operador * multiplica  una lista.

print([0] * 4)        # imprime [0, 0, 0, 0]

print(f'[1, 2, 3] * 3 = {[1, 2, 3] * 3} ')      # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# recortando una lista puedo crear una nueva lista:

t = ['a', 'b', 'c', 'd', 'e', 'f']
t1 = t[1:3]
print(t1)                 # imprime ['b', 'c']
print(t[3:])              # imprime ['d', 'e', 'f']
print(t[-1:])             # imprime ['f']
print(t[-1::-1])          # imprime ['f', 'e', 'd', 'c', 'b', 'a']
print(t[:])               # imprime la lista completa
print()
# Un operator de recorte en el lado izquierdo del comando de asignación
# puede actualizar multiples elementos de una lista.
t[1:3] = ['x', 'y']          # cambia los elementos 1 y 2
print(t, len(t))             # imprime ['a', 'x', 'y', 'd', 'e', 'f'] 6
t[1:3] = ['x', 'y', 'z']     # cambia los elementos 1 y 2 y agrega el elemento 'z'
print(t, len(t))             # imprime ['a', 'x', 'y', 'z', 'd', 'e', 'f'] 7
print()

# Metodos para listas en Python.
print('metodos para listas en Python')

t = ['a', 'b', 'c']
print(t)
t.append('d')           # agrega el elemento 'd' al final de la lista
print(f't = {t}')

t1 = t.append('d')      # agrega el elemento 'd' al final de la lista
print(f't1 = {t1} t = {t}')     # imprime None
print()

# extend toma una lista como argumento y la agrega al final de la lista.

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.append(t2)
print(t1)                # imprime ['a', 'b', 'c', ['d', 'e']]
t1.extend(t2)
print(t1)                # imprime ['a', 'b', 'c', ['d', 'e'], 'd', 'e']
print()

# sort ordena los elementos de la lista desde el menor hasta el mayor.

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)                # imprime ['a', 'b', 'c', 'd', 'e']



a = ['a', 'set', 'nada']
b = []
for x in a:
    b.append(x.capitalize())
print(b)                  # imprime ['A', 'Set', 'Nada']

c = ['a', 'SACK', 'nada', 'B', 'REY', 'c']
y = []
for x in c:
    if x.isupper():
        print(x)
        y.append(x)
print(f'y = {y}')            # imprime ['SACK', 'B', 'REY']



print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
# Otra operación común es seleccionar algunos de los elementos de una
# lista y retornar una sublista


# Eliminando elementos de una lista.
# Hay varios métodos incorporados para eliminar elementos de una lista.
# Si conoce el índice del elemento  que quieres borrar, puedes usar pop:


t = ['a', 'b', 'c']
x = t.pop(1)                     # elimina elemento de la lista con índice 1
print(f't = {t}')                # imprime ['a', 'c']

print(x)             # # imprime 'b'
print()
# pop modifica la lista y returna el elemento que se elimina.
# Si no proporcionas un índice, pop elimina y retorna el último elemento de la lista.
# Si no necesitas el elemento que se elimina, puedes usar del.
# En Python, del es una instrucción utilizada para eliminar objetos.

t = ['a', 'b', 'c']
del t[1]      # elimina el elemento     'b' de la lista
print(t)      # imprime ['a', 'c']

# Si conoce el elemento que quieres eliminar, puedes usar remove.
t = ['a', 'b', 'c']
t.remove('b')
print(t)     #

# el valor retornado por remove es None.
# Para eliminar mas de un elemento de una lista, puedes
# usar del y slice para borrar varios elementos .

#
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

# Listas y cadenas
# Una cadena  es una secuencia de caracteres. Y una lista es una
# secuencia de valores.
# Pero una lista de caracteres no es lo misma que una cadena.
# Para convertir una cadena en una lista de caracteres, puedes usar list.
s = 'spam'
t = list(s)      # t es una lista
print(t)         # imprime ['s', 'p', 'a', 'm']

# Evite usar list como una variable. porque es una palabra reservada.
# Tambien evite usar l porque se parece a 1.
# La función list convierte una cadena en una lista de caracteres.

s = 'pining for the fjords'
t = s.split()               # t es una lista con los elementos de la
                            # cadena separados por espacios
print(f't = {t}')           # imprime ['pining', 'for', 'the', 'fjords']

# join es el inverso de split, toma una lista de strings y
# un separador y devuelve una cadena.

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)  # genera la cadena 'pining for the fjords'
print(s)               # imprime 'pining for the fjords'

# Objects and values
# If we run these assignment statements:
a = 'banana'
b = 'banana'
'''
Sabemos que tanto a como b hacen referencia a una cadena, pero no
sabemos si se refieren a la misma cadena.
En un caso, a y b se refieren a dos objetos diferentes que tienen
el mismo valor.
En el segundo caso, se refieren al mismo objeto.
Para comprobar si dos variables hacen referencia al mismo
objeto, puedes usar el operador is.
'''

a = 'banana'
b = 'banana'
print(a is b)                 # imprime True
print('cccccccccccccccccc')
'''
En este ejemplo, Python solo creó un objeto de cadena, y tanto
a como b hacen referencia a él.
Pero cuando creas dos listas, obtienes dos objetos:
'''

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)                 # imprime False

'''
En este caso, diríamos que las dos listas son equivalentes, porque
tienen los mismos elementos,pero no idénticas, porque no son el mismo
objeto. Si dos objetos son idénticos, también son
equivalentes, pero si son equivalentes, no necesariamente son idénticos.

Hasta ahora, hemos estado utilizando "objeto" y "valor"
indistintamente, pero es más
preciso decir que un objeto tiene un valor. Si evalúas [1, 2, 3],
obtienes un objeto de lista cuyo valor es una secuencia de enteros.
Si otra lista tiene los mismos elementos,
decimos que tiene el mismo valor, pero no es el mismo objeto.

Aliasing
Si a hace referencia a un objeto y asignas b = a,
entonces ambas variables hacen referencia al mismo objeto:
'''

a = [1, 2, 3]
b = a
print(b is a)      # imprime True
'''
La asociación de una variable con un objeto se llama referencia.
En este ejemplo, hay dos referencias al mismo objeto.
Un objeto con más de una referencia tiene más de un nombre,
por lo que decimos que el objeto tiene un 'alias' (apodo).
Si el objeto apodado es mutable,
los cambios realizados con un alias afectan al otro:'''


b[0] = 42
print(a)         # imprime [42, 2, 3]
'''Aunque este comportamiento puede ser útil, es propenso a errores.
En general, es más seguro evitar el aliasing cuando estás trabajando
con objetos mutables.
Para objetos inmutables como las cadenas, el aliasing no es tan
problemático. En este ejemplo
'''

a = 'banana'
b = 'banana'

'''
Casi nunca importa si a y b hacen referencia a la misma cadena o no.

Argumentos de lista
Cuando pasas una lista a una función, la función obtiene una
referencia a la lista.
Si la función modifica la lista, el llamador ve el cambio.
Por ejemplo, delete_head elimina el primer elemento de una lista:'''



'''
Es importante distinguir entre operaciones que modifican listas
y operaciones que crean nuevas listas. Por ejemplo, el método append
modifica una lista, pero el operador + crea una nueva lista.'''

t1 = [1, 2]
t2 = t1.append(3)  # t2 es None
print(t1)
print(t2)
'''El valor de retorno de append es None.

Aquí hay un ejemplo usando el operador +:'''




t3 = t1 + [4]
print(t1)

print(t3)
'''El resultado del operador es una nueva lista y la lista
original permanece sin cambios.

Esta diferencia es importante cuando escribes funciones que se
supone que modifican listas.'''

print(dir(t3))  #dir(variable) da una lista de los métodos asociados a variable

#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__getstate__',
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort']

t_new1 = t3.copy()
t_new2 = t3[:]
print(t_new2)
t_new2.append(5)
print(t_new2)
x = t_new2.pop()          # x es el elemento eliminado de la lista
print(t_new2,x)
y = t_new2.count(4)
print(y)
t_new2.extend(t_new1)
print(t_new2)
t_new2.append(5)
print(t_new2.index(5))
t_new2.insert(4,100)
t_new2.remove(100)
t_new2.reverse()
t_new2.sort()
print(t_new2.sort())
print(t_new2)

t_new2.clear()
print(t_new2)

d = 'Manzana'
print(dir(d))

#['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill']




# Finalmente, veamos que ocurre si cambiamos el corchete [] por
# un paréntesis ( ) o llave {}:
list_a = [1,2,3]       # it is a list
print(f'list_a = {list_a} ,type(list_a) = {type(list_a)}')

tup_a = (1,2,3)        # it is a tuple
print(f'tup_a = {tup_a} ,type(tup_a) = {type(tup_a)}')

set_a = {1,2,3}        # it is a set
print(f'set_a = {set_a} ,type(set_a) = {type(set_a)}')

#Esta nuevas clases las analizaremos detalladamente mas adelante.