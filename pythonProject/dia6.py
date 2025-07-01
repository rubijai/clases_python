# Listas, Tuplas y Conjuntos:

a = [23.7, 45, 78] # lista mutable
b = 'asdfasdf' # cadena inmutable
l1 = list(b)   # convierte una cadena en una lista de caracteres
t1 = tuple(a)  # convierte una lista en una tupla
s1 = set(b)
print(f'a={a} type(a) = {type(a)}')
print(f'b={b} type(b) = {type(b)}')
print(f'l1={l1} type(l1) = {type(l1)}')
print(f't1={t1} type(t1) = {type(t1)}')
print(f's1={s1} type(s1) = {type(s1)}')

t2 = (4, 9, a, b,'zxcv') # la tupla es una lista inmutable entre ().

# Un uso obvio de las tuplas es para almacenar datos que deben estar
# protegidos contra escritura

print(f't1 es una: {type(t1)}')

# las listas son mutables
# las tuplas y las cadenas de caracteres son inmutables
# se aplica la indexación y el segmentado(slicing) a las tuplas

a[1] = 2.0
print(f'a={a}')

# b[0] = 'b' es un error las cadenas de caracteres son inmutables
# t1[1] = 5 es un error las tuplas  son inmutables

# conjuntos
# Los conjuntos se pueden usar para realizar operaciones típicas de
# conjuntos, como unión, intersección, diferencias de conjuntos, etc.

sx = set()          # crea un conjunto vacío
print(f'sx = {sx}')
s1 = {3, 4, 5, 6, 7, 9} # el conjunto es inmutable
print(f's1={s1}',f'type(s1)= {type(s1)}')
#s1[0] = 300     #se genera un TypeError pues s1 es inmutable
#print(f's1 = {s1}')
# No se permiten valores duplicados dentro de un conjunto
s2 = {3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8}
print(f's2={s2}',f'len(s2)={len(s2)}', f'type(s2)={type(s2)}')
print()

# Conjuntos : son inmutables. No aceptan asignación de elementos

s3 = {3, 4, 5}
s4 = {4, 5, 6, 7, 8, 9}

# Métodos usados con conjuntos:

s5 = s3.intersection(s4)  # elementos comunes en s3 y s4
                          # s3.intersection(s4)=s4.intersection(s3): {4, 5}

print(f's5 = s3.intersection(s4) = {s5}')
s6 = s4.intersection(s3)
print(f's6 = s4.intersection(s3) = {s6}')
print()

s7 = s1.union(s2)
print(f's7 = s1.union(s2) = {s1.union(s2)}')
s8 = s2.union(s1)       # todos los elementos de a y b sin repetición
                        # s1.union(s2) = s2.union(s1)
print(f's1={s1}',f's2={s2}')
print(f's7 = s1.union(s2) = {s1.union(s2) }')
print(f's8 = s2.union(s1) = {s2.union(s1) }')


e = 8
print(e in s2)
print(e in s1)
s9 = s2.difference(s1)  # a s2 le quitamos los elementos comunes con s1
                        # : s1.difference(s2) != s2.difference(s1)
s10 = s1.difference(s2)
print(f's1={s1}',f's2={s2}')
print(f' s9 = s2.difference(s1) = {s9}')
print(f' s10 = s1.difference(s2) = {s10}')

print(f's9.pop()={s9.pop()}')
print(f's9={s9}')


print(f's5 = {s5}',f's2 = {s2}')
print(s5.issubset(s2))
s10.add(e)                       # agrega el valor e al conjunto s10
print(f's10={s10}')
s1.remove(3)                     # remueve el valor 3 del conjunto s1
print(f's1={s1}')
print(f's2={s2}')

s2.pop()                      # elimina un elemento arbitrario de s2
print(f's1 = {s1}  s2 = {s2}')
s1.clear()                    # deja vacío el conjunto s1
print(f's1 = {s1}')
print()

# TUPLES
#Tuples son un tipo de secuencias que son inmutables.
t = 'a', 'b', 'c', 'd', 'e'    #una tupla es una lista de valores
                               # separados por comas (,).Aunque no
                               # es necesario, es común encerrar
                               # tuplas en parentesis:
t = ('a', 'b', 'c', 'd', 'e')

#Para crear una tupla con un solo elemento,
# tienes que incluir una coma final:


t1 = 'a',
print(f'type(t1) = {type(t1)}')      #  <class 'tuple'>

# Un valor en parentesis no es una tupla:
t2 = ('a')
print(f'type(t2) = {type(t2)}')      # type(t2) = <class 'str'>
# Otra manera de crear una tupla es el operador de tupla:

t = tuple()
print(t)       #() ES UNA TUPLE VACÍA
# Si el argumento es una secuencia (string, lista o tupla),
# el resultado es una tupla con los elementos de la secuencia:
t = tuple('lupins')           # convierte la secuencia en una tuple
print(f't = {t}')             #('l', 'u', 'p', 'i', 'n', 's')
lx = list('lupins')           # convierte la secuencia en una lista
print(f'lx = {lx}')
t1 =tuple([x for x in range(1,11)]) # convierte la lista creada en tuple
print(f't1 = {t1}')

# la mayoria de los operadores de listas funciona en tuplas.
# Los paréntesis[] indexan un elemento:
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])        #'a'
list1 = [1,2,3,4,5,6]
tup1 = tuple(list1)            # convierte en tuple la lista --> list1
print(f'tup1 = {tup1}')        #(1, 2, 3, 4, 5, 6)

#el operador de segmentación funciona en tuplas.

print(t[1:3])        # ('b', 'c')
# Pero si tratas de modificar uno de los elementos de la tupla,
# obtienes un error:
# t[0] = 'A'
#TypeError: el objeto no permite la asignación.

#Debido a que las tuplas son inmutables, no se puede modificar una tupla.
# Pero puede reemplazar una tupla con otra:

t = ('A',) + t[1:]    # puedo concatenar las tuplas
print(f't = {t}')     #('A', 'b', 'c', 'd', 'e')

# Los operadores relacionales funcionan en tuplas y en otras secuencias.
# Va comparando uno a uno los elementos.
print((0, 1, 2) < (0, 3, 4))         #True
print((0, 1, 2000000) < (0, 3, 4))   #True
# intercambio de valores:
a = 1
b = 2
temp = a
a = b
b = temp
print(a,b)

# intercambio de valores con el uso de tuple:
a, b = b, a    # uso de tuple
print(a,b)
# a, b = 1, 2, 3       #ValueError: muchos valores

#el lado derecho puede ser cualquier secuencia (string, lista o tupla).
c,d = [1,2,3],'JAIME'
print(c,d)     # [1, 2, 3] 'JAIME'
e,f,g = (4,5,6)
print(e,f,g)
addr = 'monty@python.org'
print(addr.split('@'))          #['monty', 'python.org']
uname, domain = addr.split('@')
print(f'uname,domain: {uname}, {domain}')     #

#el valor de retorno de split es una lista con dos elementos;
# el primero es asignado a uname, el segundo a domain.

t2 = divmod(7, 3)   # divmode es una built_in_function para la división entera
print(f't2={t2}')         # 7 // 3 = 2 --> quot y 7 % 3 = 1 --> rem
quot, rem = divmod(7, 3)

# Este es un ejemplo de una función que retorna una tupla:

def min_max(t):              # min, max son built_in_functions
    return min(t), max(t)
t = [23,45,67,25,12,87,19]
print(min_max(t))           #(12, 87)


t = (7, 3)
#divmod(t)          #TypeError: se esperan 2 argumentos, pero hay uno solo.

# Pero se pueden separar usando *
quot, rem = divmod(*t)    #(2, 1) *args --> *t
print(quot)
print(rem)

# zip es una función de Python que toma dos o más secuencias y las entrelaza,


# El nombre de la función se refiere a la funcionalidad de
# un cierre que entrelaza dos filas de dientes
# Este ejemplo entrelaza la cadena 'abc' con una lista [0, 1, 2].
st = 'abc'
lt = [0, 1, 2]
print(f'zip(st, lt)={zip(st, lt)}')  #<zip object at 0x000002137883FEC0>
print(f'zip(lt, st)={zip(lt, st)}')  # genera un iterador

#El resultado de zip es una secuencia de tuplas.

# el mas común uso de zip es en for loops.
for pair in zip(st, lt):
    print(pair)          # imprime los pares: ('a', 0) ('b', 1) ('c', 2)

for pair in zip(lt, st):
    print(pair)          #(0, 'a') (1, 'b') (2, 'c')

# Un objeto zip es un iterador.


#Si queremos usar operadores de listas y metodos, podemos hacerlo
# con un objeto zip.

list(zip(st, lt))               #[('a', 0), ('b', 1), ('c', 2)]
print(f'list(zip(st, lt))={list(zip(st, lt))}')


#Si las secuencias son de diferente longitud, el resultado tiene la
# longitud de la secuencia más corta.
print(zip('Anne', 'Elk'))          #[('A', 'E'), ('n', 'l'), ('n', 'k')]

#se puede usar tuplas en el for loop para recorrer una lista de tuplas.
lt1 = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in lt1:
    print(number, letter)



# Si se combinan zip, for y tupla asignación, se tiene una
# forma de recorrer (dos o más) secuencias a la vez.
# Esto es has_match toma   dos secuencias t1 y t2 y
# devuelve True si hay un indice i tal que t1[i] == t2[i].

def has_match(t1, t2):
    for x, y in zip(t1, t2):   #
        if x == y:
            return True
    return False
t1 = 'a', 'b', 'c', 'd', 'e'
t2 = 'f', 'b', 'c', 'd', 'e'
for x, y in zip(t1, t2):
    print(x, y)
print(zip(t1, t2))           # imprime un objeto zip
print(has_match(t1, t2))      # True
#If you need to traverse the elements of a sequence
# and their indices,
# you can use the built-in function enumerate:
for index, element in enumerate('abc'):
    print(index, element)

for index, element in enumerate(t1):
    print(index, element)

for index, element in enumerate(t1):
    print(index, element)
# El resultado es un objeto enumerate que itera una
# secuencia de tuplas.
# Cada tupla contiene un indice (iniciando en 0) y
# un elemento de la secuencia.
print([(i, e) for i, e in enumerate('abc')])   #[(0, 'a'), (1, 'b'), (2, 'c')]



'''
Secuencias de secuencias

Me he enfocado en listas de tuplas, pero casi todos los
ejemplos en este capítulo también funcionan con listas
de listas, tuplas de tuplas y tuplas de listas. Para evitar
enumerar las posibles combinaciones, a veces es más fácil
hablar sobre secuencias de secuencias.

En muchos contextos, los diferentes tipos de secuencias
(cadenas de caracteres, listas y tuplas)
pueden usarse indistintamente. Entonces, ¿cómo deberías
elegir uno sobre los demás?
Para empezar con lo obvio, las cadenas de caracteres son
más limitadas que otras secuencias porque
los elementos tienen que ser caracteres. También son
inmutables. Si necesitas
la capacidad de cambiar los caracteres en una cadena
(en lugar de crear
una nueva cadena), es posible que desees usar una lista
de caracteres en su lugar.
#Las listas son más comunes que las tuplas, principalmente
porque son mutables.

Pero hay algunos casos donde podrías preferir tuplas:
#1. En algunos contextos, como en una declaración de retorno,
es sintácticamente más simple crear una tupla que una lista.

#2. Si deseas usar una secuencia como clave de un diccionario,
debes usar un tipo inmutable como una tupla o cadena de caracteres.

#3. Si estás pasando una secuencia como argumento a una función,
usar tuplas reduce el potencial de comportamiento inesperado
debido al aliasing.

Debido a que las tuplas son inmutables, no proporcionan métodos
como sort y reverse, que modifican listas existentes.
Pero Python proporciona la función incorporada sorted,
que toma cualquier secuencia y devuelve una nueva lista
con los mismos elementos en orden ,
y reversed, que toma una secuencia y devuelve un
iterador que recorre la lista en orden inverso.'''

ltx =([(i, e) for i, e in enumerate('aefbc')])
print(f'ltx = {ltx}')
lty = []
for x,y in ltx:
    x,y = y,x
    lty.append((x,y))
    lty.sort()
print(f'lty = {lty}')
lty.reverse()
print(f'lty = {lty}')

# invertir la cadena Hola Mundo:
print(f"Hola Mundo invertido: {''.join('Hola Mundo')[-1::-1]}")


#  Uso de *args: permite que el número de argumentos sea ilimitado.
#  '*args' es interpretado por python como una tupla. En lugar de args
#  se puede usar cualquier nombre, p.e '*tup'

def printall(*args):
    print(args)

def printall1(*tup):
    print(tup)
#printall() y printall1() dan el mismo resultado
#El parámetro args puede ser cualquier nombre que quieras
# y al colocarle antes el símbolo '*' se indica que es una 'tuple'
# args se usa por convención.

printall(1, 2.0, '3')                # (1, 2.0, '3')
printall(1, 'jaime', '3','ramirez')  # (1, 'jaime', '3','ramirez')

printall1(1, 2.0, '3')                # (1, 2.0, '3')
printall1(1, 'jaime', '3','ramirez')  # (1, 'jaime', '3','ramirez')


def producto(*tup):
    res = 1
    for x in tup:
        print(x)
        res *= x
    return res

res = producto( 'j',3, 2,4)
print(res,len(res))


def suma_todos(*args):      # *args se puede usar cualquier numero de argumentos
    # args es un tuple con cualquier numero de argumentos
    # sum = 0
    # for m in args:
    # sum += m
    return sum(args)

print(suma_todos(1, 2, 3))        # Salida: 6
print(suma_todos(4, 5, 6, 7, 8))  # Salida: 30

def imprimir_valores(*args):
    for arg in args:
        print(arg)

imprimir_valores(1, 'a', True, [1, 2, 3])
# Salida:
# 1
# a
# True
# [1, 2, 3]

# Caso Práctico: Útil cuando se quiere sumar un número desconocido
# de elementos o cuando se desean procesar todos los elementos dados
# sin preocuparse por cuántos son.


def add1(a=1, b=2, c=3):  # tiene 3 argumentos con valores iniciales (por defecto)
                          # que pueden cambiarse
    sum = a + b + c
    return sum

print(suma_todos(3, 4, 7, 10))  # 24
print(suma_todos(3, 4))  # 7
print(add1())  # a=1,b=2,c=3       sum = 6
print(add1(c=100))  # a=1,b=2,c=100  mantiene los valores a y b  sum=103

print(add1(c=7))  # a=1,b=2,c=7  sum = 10




### Diferencia entre un Generador y una Tupla

generador = (1 for letra in "banana" if letra == 'a')
print(f'generador = {generador} {type(generador)}')  # Salida: <generator object <genexpr> at 0x7fd018ab6c80>

# Convierte el generador a una tupla (se evalúa y almacena todos los valores)
tupla = tuple(1 for letra in "banana" if letra == 'a')
print(tupla)  # Salida: (1, 1, 1)

'''1. **Generador**:
   - La expresión `(1 for letra in palabra if letra == 'a')` crea un generador,
   que es un **objeto iterable** que genera los valores uno a uno, bajo demanda.
   - No almacena todos los valores en memoria; en lugar de eso, los produce a
   medida que se necesitan.
   - Es más eficiente en términos de memoria cuando se necesita procesar una gran
   cantidad de datos de manera secuencial.

2. **Tupla**:
   - Una tupla almacena **todos los elementos en memoria** y los permite acceder
   de inmediato. Para crear una tupla, se usa una comprensión de tuplas (siempre
   rodeada de paréntesis, pero con todos los elementos separados por comas), por
   ejemplo: `(1, 2, 3)`.
   - Una expresión de generador, en cambio, no se evalúa inmediatamente y, por lo
   tanto, no tiene los valores almacenados como una tupla.

### Ejemplo de Diferencia

```python
# Generador (se evalúa bajo demanda)
generador = (1 for letra in "banana" if letra == 'a')
print(generador)  # Salida: <generator object <genexpr> at 0x7fd018ab6c80>

# Convierte el generador a una tupla (se evalúa y almacena todos los valores)
tupla = tuple(1 for letra in "banana" if letra == 'a')
print(tupla)  # Salida: (1, 1, 1)
```

En el ejemplo anterior:
- `generador` es un objeto de tipo generador, y no contiene todos los valores al
   mismo tiempo. Los genera cuando se recorre en un bucle, por ejemplo.
- `tupla` es una tupla que contiene todos los `1` generados por el generador,
evaluados y almacenados en memoria.

### Ventajas de Usar Generadores

- Los generadores son útiles cuando necesitas trabajar con secuencias de valores
grandes, ya que no ocupan memoria adicional.
- Permiten procesar datos de manera eficiente, generando cada elemento "al vuelo"
sin necesidad de almacenar todos los valores a la vez.

Para resumir, aunque `(1 for letra in palabra if letra == 'a')` se parece a una
tupla, en realidad es una expresión de generador y se comporta de manera diferente
a una tupla en Python.'''
                  #[] (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

gen1 = (i for i in range(1,11))
l1 = list(gen1)
t1 = tuple(gen1)
print(l1,t1)

gen1 = (i for i in range(1,11))   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ()
t1 = tuple(gen1)
l1 = list(gen1)
print(l1,t1)                      #[] (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

gen2 = (1 for letra in "banana" if letra == 'a')
l2 = list(gen2)
t2 = tuple(gen2)
print(l2,t2)               # [1, 1, 1] ()

gen2 = (1 for letra in "banana" if letra == 'a')
t2 = tuple(gen2)
l2 = list(gen2)
print(l2,t2)               # [] (1, 1, 1)

## Ejercicio
'''
Escribir un programa que almacene las matrices en una tupla
y muestre por pantalla su producto.
Nota: Para representar matrices mediante tuplas usar tuplas
anidadas, representando cada vector fila en una tupla.
'''
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])

'''
La función `enumerate()` en Python se usa para **iterar sobre
un iterable** (como una lista, tupla, o cadena) y obtener tanto
el **índice** de cada elemento como el **valor** del elemento
en cada iteración. Esto es especialmente útil cuando necesitas
saber la posición de cada elemento mientras recorres el iterable,
sin tener que mantener un contador manual.
'''
# Obtener una lista de tuplas (indice, valor) de una cadena:
cadena = 'caravana'
lista_i_v = []
for i in range(len(cadena)):
    lista_i_v.append((i,cadena[i]))
print(f'resultado1 = {lista_i_v}')

# Este mismo resultado lo podemos lograr usando enumerate :
lista_i_v = [(i,v) for i,v in enumerate(cadena)]
print(f'resultado2 = {lista_i_v}')

### Sintaxis de `enumerate()`  enumerate(iterable, start=0)
iterable = list('caravana')       # convierte 'str' en una lista de caracteres
print(iterable)                   # ['c', 'a', 'r', 'a', 'v', 'a', 'n', 'a']
for i,x in enumerate(iterable, start=0):
    # se puede cambiar start( que por defecto es 0)
    print(i,x)

'''

- **`iterable`**: Es la colección de datos que deseas iterar, como una lista, una tupla,
 una cadena, o cualquier objeto iterable.
- **`start`** *(opcional)*: Especifica el valor inicial del índice (por defecto es 0).

`enumerate()` devuelve un **objeto enumerado**, que puede ser convertido en una
lista de tuplas si es necesario, o utilizado directamente en un bucle `for`.'''

### Ejemplo Básico de `enumerate()` con una Lista

colores = ["rojo", "verde", "azul", "amarillo"]
for indice, color in enumerate(colores):
    print(f"Índice: {indice}, Color: {color}")

# Salida:
# Índice: 0, Color: rojo
# Índice: 1, Color: verde
# Índice: 2, Color: azul
# Índice: 3, Color: amarillo

# Crear una lista de tuplas:
l_t = [(index,value) for (index,value) in enumerate(colores)]
print(f'l_t = {l_t}')

#En este caso, `enumerate(colores)` devuelve pares de
# (índice, elemento), que se descomponen
#en `indice` y `color` en cada iteración.

### Ejemplo con el Parámetro `start`

#Puedes cambiar el índice inicial usando el parámetro `start`:


for indice, color in enumerate(colores, start=1):
    print(f"Índice: {indice}, Color: {color}")
# Salida:
# Índice: 1, Color: rojo
# Índice: 2, Color: verde
# Índice: 3, Color: azul
# Índice: 4, Color: amarillo


#Aquí, `start=1` hace que la numeración comience desde 1 en lugar de 0.

### Conversión de `enumerate()` a una Lista de Tuplas

#`enumerate()` devuelve un objeto enumerado que se puede convertir en una lista
# de tuplas con `list()`:


colores_enumerados = list(enumerate(colores)) # convierte el objeto enumerate(colores) en lista
print(colores_enumerados)
# Salida: [(0, 'rojo'), (1, 'verde'), (2, 'azul'), (3, 'amarillo')]

### Resumen

'''

### Sintaxis de `enumerate()`

enumerate(iterable, start=0)

- **`iterable`**: Es la colección de datos que deseas iterar, como una lista,
una tupla, una cadena, o cualquier objeto iterable.
- **`start`** *(opcional)*: Especifica el valor inicial del índice (por defecto es 0).

`enumerate()` devuelve un **objeto enumerado**, que puede ser convertido en
una lista de tuplas si es necesario, o utilizado directamente en un bucle `for`.

La función `enumerate()` es muy útil cuando necesitas trabajar con
los índices y valores de un iterable al mismo tiempo. Su uso es
frecuente en situaciones en las que necesitas manipular datos en
función de su posición en una colección o cuando quieres mejorar
la legibilidad del código al evitar contadores manuales.'''


'''
La función `enumerate()` en Python se usa para **iterar sobre
un iterable** (como una lista, tupla, o cadena) y obtener tanto
el **índice** de cada elemento como el **valor** del elemento
en cada iteración. Esto es especialmente útil cuando necesitas
saber la posición de cada elemento mientras recorres el iterable,
sin tener que mantener un contador manual.
'''
# Obtener una lista de tuplas (indice, valor) de una cadena:
cadena = 'caravana'
lista_i_v = []
for i in range(len(cadena)):
    lista_i_v.append((i,cadena[i]))
print(f'resultado1 = {lista_i_v}')

# Este mismo resultado lo podemos lograr usando enumerate :
lista_i_v = [(i,v) for i,v in enumerate(cadena)]
print(f'resultado2 = {lista_i_v}')

### Sintaxis de `enumerate()`  enumerate(iterable, start=0)
iterable = list('caravana')       # convierte 'str' en una lista de caracteres
print(iterable)                   # ['c', 'a', 'r', 'a', 'v', 'a', 'n', 'a']
for i,x in enumerate(iterable, start=0):
    # se puede cambiar start( que por defecto es 0)
    print(i,x)

'''

- **`iterable`**: Es la colección de datos que deseas iterar, como una lista, una tupla,
 una cadena, o cualquier objeto iterable.
- **`start`** *(opcional)*: Especifica el valor inicial del índice (por defecto es 0).

`enumerate()` devuelve un **objeto enumerado**, que puede ser convertido en una 
lista de tuplas si es necesario, o utilizado directamente en un bucle `for`.'''

### Ejemplo Básico de `enumerate()` con una Lista

colores = ["rojo", "verde", "azul", "amarillo"]
for indice, color in enumerate(colores):
    print(f"Índice: {indice}, Color: {color}")

# Salida:
# Índice: 0, Color: rojo
# Índice: 1, Color: verde
# Índice: 2, Color: azul
# Índice: 3, Color: amarillo

# Crear una lista de tuplas:
l_t = [(index,value) for (index,value) in enumerate(colores)]
print(f'l_t = {l_t}')

#En este caso, `enumerate(colores)` devuelve pares de
# (índice, elemento), que se descomponen
#en `indice` y `color` en cada iteración.

### Ejemplo con el Parámetro `start`

#Puedes cambiar el índice inicial usando el parámetro `start`:


for indice, color in enumerate(colores, start=1):
    print(f"Índice: {indice}, Color: {color}")
# Salida:
# Índice: 1, Color: rojo
# Índice: 2, Color: verde
# Índice: 3, Color: azul
# Índice: 4, Color: amarillo


#Aquí, `start=1` hace que la numeración comience desde 1 en lugar de 0.

### Conversión de `enumerate()` a una Lista de Tuplas

#`enumerate()` devuelve un objeto enumerado que se puede convertir en una lista
# de tuplas con `list()`:


colores_enumerados = list(enumerate(colores)) # convierte el objeto enumerate(colores) en lista
print(colores_enumerados)
# Salida: [(0, 'rojo'), (1, 'verde'), (2, 'azul'), (3, 'amarillo')]

### Resumen

'''

### Sintaxis de `enumerate()`

enumerate(iterable, start=0)

- **`iterable`**: Es la colección de datos que deseas iterar, como una lista, 
una tupla, una cadena, o cualquier objeto iterable.
- **`start`** *(opcional)*: Especifica el valor inicial del índice (por defecto es 0).

`enumerate()` devuelve un **objeto enumerado**, que puede ser convertido en 
una lista de tuplas si es necesario, o utilizado directamente en un bucle `for`.

La función `enumerate()` es muy útil cuando necesitas trabajar con 
los índices y valores de un iterable al mismo tiempo. Su uso es 
frecuente en situaciones en las que necesitas manipular datos en 
función de su posición en una colección o cuando quieres mejorar 
la legibilidad del código al evitar contadores manuales.'''




#   La función lambda

#   Las funciones lambda en Python son funciones anónimas, es decir,
#   funciones sin nombre que se crean con la palabra clave lambda.
#   Se utilizan para definir funciones pequeñas y de una sola línea
#   de manera rápida y en el lugar donde se necesitan, sin necesidad
#   de declararlas con def.

#   Sintaxis de una función lambda
#   lambda x: expresión            equivale a f(x) = expresion

''' Las funciones `map`, `filter` y `sorted` en Python son
    funciones de orden superior que permiten aplicar operaciones
    sobre colecciones como listas y tuplas de forma
    concisa y funcional. Son muy útiles para procesar datos
    en una sola línea de código.

### Función `map`

La función `map` aplica una función a cada elemento de un
iterable (como una lista o tupla)
y devuelve un nuevo iterable con los resultados.

**Sintaxis:**
map(funcion, iterable)

- **funcion**: Es una función que toma un elemento del iterable
como argumento y devuelve un valor transformado.
- **iterable**: La colección (lista, tupla, etc.) cuyos elementos serán
  procesados por la función.

**Ejemplo: Elevar al cuadrado cada elemento de una lista**


Las funciones como `**map**`, `**filter**` y `**sorted**` en Python
se llaman **funciones de orden superior** porque **reciben otras
funciones como argumento** o **devuelven funciones**.
Este es un concepto clave en programación funcional.

---

### 🔍 ¿Qué es una función de orden superior?

Una función es de **orden superior** si cumple al menos una
de estas dos condiciones:

1. **Recibe una función como argumento**
2. **Devuelve una función como resultado**



### ✅ ¿Por qué `map`, `filter` y `sorted` son de orden superior?

#### `map(función, iterable)`
- Toma una **función** y un **iterable**.
- Aplica la función a cada elemento del iterable.


# Ejemplo
numeros = [1, 2, 3]
resultado = map(lambda x: x * 2, numeros)
print(list(resultado))  # [2, 4, 6]
```

> `lambda x: x * 2` es una función pasada como argumento ⇒ orden superior.


#### `filter(función, iterable)`
- Toma una **función** que devuelve `True` o `False`, y un iterable.
- Retorna los elementos que **cumplen la condición**.


numeros = [1, 2, 3, 4]
resultado = filter(lambda x: x % 2 == 0, numeros)
print(list(resultado))  # [2, 4]


> También recibe una función ⇒ orden superior.


#### `sorted(iterable, key=función)`
- Ordena elementos, y puede usar una función como **clave de ordenamiento**.

palabras = ["banana", "kiwi", "manzana"]
ordenadas = sorted(palabras, key=len)
print(ordenadas)  # ['kiwi', 'banana', 'manzana']
```

> `key=len` es una función que decide cómo ordenar ⇒ función pasada
como argumento ⇒ orden superior.



### 🧠 Conclusión:
Estas funciones son de **orden superior** porque **usan funciones
como datos**, lo cual te permite hacer código más limpio, expresivo
y modular. Es una base poderosa en programación funcional y
muy usada en Python.

'''

numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f'cuadrados = {cuadrados}')  # Salida: [1, 4, 9, 16]

# Tambien se puede ingresar una función lambda así:
f_l = lambda n: n**3 #se puede definir una función usando la función lambda
print(f'f_l(2) = {f_l(2)}')
cubos = [f_l(n) for n in range(5)]
print(f'cubos={cubos}')

# Esto se puede también lograr también con list comprehension:
cuadrados = [x**2 for x in numeros]

'''En este caso, usamos `lambda x: x ** 2` como función, que toma 
cada elemento de `numeros`, lo eleva al cuadrado, y con 'list' (también
se puede usar tuple) y `map` devuelve una lista (o tuple) de los resultados.
Hace las veces de de la expresión x**2 en list comprehension.


### Función `filter`

La función `filter` selecciona elementos de un iterable que cumplen con 
una condición dada en una función, devolviendo solo los elementos para los 
cuales la función devuelve `True`.

**Sintaxis:**

filter(funcion, iterable)


- **funcion**: Es una función que toma un elemento del iterable y devuelve 
un valor booleano (`True` o `False`).
- **iterable**: La colección de datos que será filtrada.

**Ejemplo: Filtrar los números pares de una lista**'''

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))       #expresion: condicion sin 'if'
print(f'pares = {pares}')  # Salida: [2, 4, 6]

# Con list comprehension:
pares = [x for x in numeros if x % 2 == 0]


'''En este caso, `lambda x: x % 2 == 0` es la función que devuelve `True` 
si `x` es par y `False` si no lo es. `filter` devuelve solo los números 
pares de la lista. Hace las veces de 'if x % 2 == 0' en list comprehension

### Función `sorted`

La función `sorted` devuelve una nueva lista ordenada de los elementos 
de un iterable. No modifica la lista original, y permite usar una función 
de clave (`key`) para definir cómo ordenar los elementos.

**Sintaxis:**

sorted(iterable, key=None, reverse=False)

- **iterable**: La colección de elementos a ordenar.
- **key**: (Opcional) Una función que determina el criterio de ordenación. 
- **reverse**: (Opcional) Si es `True`, se ordena en orden descendente.'''
import random as rn
l1 = [i for i in range(11)]
print(f'l1 = {l1}')
lx = [i**2 for i in l1]
print(f'lx = {lx}')
l2 = list(map(lambda i:i**2,l1))
print(f'l2 = {l2}')
rn.shuffle(l2)
print(f'l2 = {l2}')
ly = [(index,value) for index,value in enumerate(l2)]
print(f'ly = {ly}')
l3 = sorted(ly)
print(f'l3 = {l3}')
l4 = sorted(ly,key=lambda z: z[1])
print(f'l4 = {l4}')
l5 = sorted(ly,key=lambda z: z[1],reverse=True)
print(f'l5 = {l5}')

#**Ejemplo 1: Ordenar una lista de números**


numeros = [4, 2, 8, 1, 7]
ordenados = sorted(numeros)
print(f'ordenados = {ordenados}')  # Salida: [1, 2, 4, 7, 8]
                                   # en orden ascendente por defecto

# Otros ejemplos:
#Escribe una lambda que sume dos números.
f_l = lambda a,b:a+b
print(f_l(8,7))

f_lambda = lambda x:x**3
ly = [f_lambda(i) for i in range(1,11)]
print(ly)

#Crea una función lambda que devuelva la longitud de una cadena
f_l1= lambda cad: len(cad)
print(f_l1('Juan'))

#Dada la lista [(1, 3), (2, 1), (4, 2)], ordénala por el segundo elemento de cada
# tupla usando sorted y lambda.
lx = [(1, 3), (2, 1), (4, 2)]
lxn = list(sorted(lx,key=lambda x:x[1],reverse=True))
print(lxn)

#Usa filter y lambda para quedarte solo con los números pares de una lista
print(list(filter(lambda x: x%2==0,ly)))

#Usa map y lambda para obtener los cuadrados de los números [1, 2, 3, 4]
lz = [1, 2, 3, 4]
lzn = list(map(lambda x:x**2,lz ))
print(lzn)

#Dada una lista de diccionarios con nombres y edades, ordénala por edad:
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Marta", "edad": 35}
]
ordenado = list(sorted(personas,key= lambda personas: personas['edad'],reverse=True))
print(ordenado)

#Filtra los impares y multiplícalos por 3 con filter y map.
print(ly)
#lyimp = filter(lambda x: x%2 != 0,ly)
#print(lyimp)
lyf = list(map(lambda x:3*x,filter(lambda x: x%2 != 0,ly)))
print(lyf)

# Escribe una lambda que devuelva "Par" si el número es par
# y "Impar" si es impar.
par_impar = lambda x: "Par" if x % 2 == 0 else "Impar"

# diccionarios:

'''Los **diccionarios** en Python son estructuras de datos que permiten
 almacenar **pares de clave-valor**. Permiten un acceso rápido a los
 valores mediante sus claves, y se utilizan para almacenar datos en
 una estructura que permite buscar, agregar, actualizar y eliminar
 elementos de manera eficiente.
 Puedes crear diccionarios usando `{}`, con la función `dict()`,
o utilizando pares clave-valor.'''

mi_diccionario = {}  # Diccionario vacío

su_diccionario = dict()  # diccionario vacío

# Diccionario con valores iniciales:
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Bogotá"}

# Cada elemento del diccionario es un par clave:valor. los elementos
# son separados por comas. En el ejemplo anterior las claves son de 'type str'

print(mi_diccionario, type(mi_diccionario), len(mi_diccionario))

# dictionary comprehension:
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}


# Uso de enumerate y diccionary comprehension para crear un diccionario:
name = 'Jaime'  # len(name) --> 5
dic1 = {clave: valor for (clave, valor) in enumerate(name)}
print(f'dic1 = {dic1}')  # las claves son los índices de 'Jaime'

# dic1 = {0: 'J', 1: 'a', 2: 'i', 3: 'm', 4: 'e'}

# Uso de zip y diccionary comprehension para crear un diccionario:

l = [0, 1, 2, 3, 4]  # len(l) --> 5
dic2 = {x: y for (x, y) in zip(l, name)}
print(f'dic2 = {dic2}')

# dic2 = {0: 'J', 1: 'a', 2: 'i', 3: 'm', 4: 'e'}

# Otra forma:
dic3 = {x: y for (x, y) in zip(range(len(name)), name)}
print(f'dic3 = {dic2}', range(len(name)))

# Uso de zip:
d = dict(zip('abc', range(3)))
print(f'd = {d}')

# d = {'a': 0, 'b': 1, 'c': 2}
'''
### Características de los Diccionarios

- **Pares Clave-Valor**: Cada elemento de un diccionario tiene 
    una **clave** única (es inmutable) y un **valor** asociado (es mutable).

- **Acceso Rápido**: Los diccionarios están optimizados para acceder 
    a valores a partir de sus claves de manera rápida.
    Para acceder a un valor, usa la clave entre corchetes (`[]`), 
   o el método `get()`:      

- **Claves Únicas**: Las claves en un diccionario deben ser únicas (son inmutables); 
    si se asigna un valor a una clave que ya existe, el valor anterior 
    se sobrescribe (los valores son mutables).'''
lista_meses = [
    (1, "enero"), (2, "febrero"), (3, "marzo"),
    (4, "abril"), (5, "mayo"), (6, "junio"),
    (7, "julio"), (8, "agosto"), (9, "septiembre"),
    (10, "octubre"), (11, "noviembre"), (12, "diciembre")
]
# Creemos el diccionario_meses:
diccionario_meses = {n: mes for n, mes in lista_meses}
print(f'diccionario_meses = {diccionario_meses}')

empleado = {'nombre': 'Ana', 'edad': 28, 'cargo': "Administradora"}
print(empleado, len(empleado))  # len --> 3 elementos clave:valor

# Acceder usando corchetes
#
print(f'diccionario_meses[12] = {diccionario_meses[12]}')
print(f"empleado['nombre']) = {empleado['nombre']}")
# 12 y 'nombre' son claves (no son índices) en sus
# respectivos diccionarios : diccionario_meses y empleado

# Recuerde que en las listas se accede al valor con el respectivo índice.

empleado['nombre'] = 'Juana'  # el valor se puede cambiar (es mutable)
print(f"empleado['nombre']) = {empleado['nombre']}")  # devuelve el valor asociado a 'nombre'
print(f'empleado: {empleado}')  # imprime el diccionario llamado : empleado

# Acceder usando el método get() (devuelve None o un comentario
# o inclusive un número, si la clave no existe)

print(empleado.get("edad"))  # Salida: 30  accede con la clave
print(empleado.get("pais", "No especificado"))  # Salida: 'No especificado'.
# En el diccionario no existe la clave : 'pais'
# y por lo tanto devuelve el
# comentario : 'No especificado'

print(empleado.get("peso"))  # Imprime None , no se agregó comentario o valor
print(empleado.get("peso", 0))  # Imprime 0, no existe la clave: 'peso'
'''
- **Mutables**: Puedes modificar, agregar y eliminar pares clave-valor 
    después de haber creado el diccionario.'''

empleado['pais'] = 'Colombia'  # Agrega un par clave:valor --> 'pais' : 'Colombia'
print(f'empleado = {empleado}')
empleado['ciudad'] = 'Bogotá'
# Modificar un valor
empleado["edad"] = 31

print(f'empleado = {empleado}')  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Bogotá', 'pais': 'Colombia'}

### Eliminación de Elementos

# Para eliminar elementos, usa `del`o los métodos: `pop()`, o `popitem()`:

# Usando del
del empleado["ciudad"]  # elimina 'ciudad':'Bogotá'
print(f'empleado = {empleado}')

# Usando pop() (elimina y devuelve el valor del elemento eliminado)
edad = empleado.pop("edad")  # elimina 'edad': 31 y devuelve el valor 31
print(f'edad = {edad}')
print(f'empleado = {empleado}')

# Usando popitem() (elimina y devuelve el último elemento como una tupla)
ultimo = empleado.popitem()  # elimina último y devuelve el item  ('pais','Colombia')
print(f'ultimo = {ultimo}')
print(f'empleado = {empleado}')

### Métodos Útiles de Diccionarios

# **`keys()`**: Devuelve una vista con todas las claves del diccionario.
# **`values()`**: Devuelve una vista con todos los valores del diccionario.
# **`items()`**: Devuelve una vista con todos los pares clave-valor
#                del diccionario como tuplas.

empleado = {"nombre": "Juan", "edad": 30, "ciudad": "Bogotá"}
print(f'empleado = {empleado}')
print(empleado.keys())  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])
print(empleado.values())  # Salida: dict_values(['Juan', 30, 'Bogotá'])
print(empleado.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Bogotá')])

# Estos métodos se pueden usar para iterar a través de ellos:
for key in empleado.keys():
    print(f'key = {key}')
for value in empleado.values():
    print(f'value = {value}')
for item in empleado.items():
    print(f'item = {item}')
### Ejemplos Avanzados
colores = ["rojo", "verde", "azul", "amarillo"]
dic_1 = {}
for index, color in enumerate(colores, 1):
    dic_1[index] = color
print(f'dic_1 = {dic_1}')

'''

El operador `in` utiliza diferentes algoritmos para listas y diccionarios.  
Para las listas, busca los elementos de la lista en orden, como se 
menciona en la Sección.  
A medida que la lista se hace más larga, el tiempo de búsqueda aumenta 
en proporción directa.

Los diccionarios en Python usan una estructura de datos llamada tabla 
hash (hashtable) que tiene una propiedad notable:  
el operador `in` tarda aproximadamente la misma cantidad de tiempo, 
sin importar cuántos  elementos tenga el diccionario.

Una implementación es una forma de realizar una computación; algunas 
implementaciones son mejores  que otras.  
Por ejemplo, una ventaja de la implementación del diccionario es 
que no necesitamos saber de antemano qué letras aparecen en la cadena, 
y solo tenemos que hacer espacio  para las letras que realmente aparecen.

'''
# 1. **Iterar sobre un Diccionario**:

for clave, valor in empleado.items():
    print(f"{clave}: {valor}")

# 2. **Contar la frecuencia de palabras en un texto**:

texto = "hola mundo hola"

frecuencias = {}
for palabra in texto.split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
print(f'frecuencias = {frecuencias}')  # Salida: {'hola': 2, 'mundo': 1}
# También así:
l1 = texto.split(' ')
d3 = {item: l1.count(item) for item in l1}
print(f'frecuencias = {d3}')

# 3. **Diccionario de Listas** (Agrupar elementos):


datos = [("manzana", 5), ("banana", 3), ("manzana", 2)]
inventario = {}

inventario = {}
for f, n in datos:
    if f not in inventario:
        inventario[f] = n
    else:
        inventario[f] += n
print(f'inventario = {inventario}')

# Otra forma mas compacta:
datos = [("manzana", 5), ("banana", 3), ("manzana", 2)]
inventario = {}
for fruta, cantidad in datos:
    inventario[fruta] = inventario.get(fruta, 0) + cantidad
print(f'inventario = {inventario}')  # Salida: {'manzana': 7, 'banana': 3}

'''
Un diccionario es como una lista, pero más general. En una lista, 
los índices tienen que ser enteros; en un diccionario pueden ser
(casi) de cualquier tipo.  
La asociación de una clave y un valor se llama un par clave-valor o, 
a veces, un ítem.  
Un diccionario representa una asignación de claves a valores.  
La función `dict` crea un nuevo diccionario sin elementos. Debido 
a que `dict` es el nombre de  una función incorporada, debes evitar 
usarlo como nombre de variable.
'''

eng2sp = dict()  # crea dict vacío
eng2sp['one'] = 'uno'  # crea un item en el dict el orden es impredecible
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['two'])  # da el valor de la llave
# print(eng2sp['four'])  KeyError: 'four' no existe esta llave.
print(len(eng2sp))  # Da el número de items
print('one' in eng2sp)  # True es key
print('uno' in eng2sp)  # False es value (pregunta si uno es una llave)
vals = eng2sp.values()  # el método values retorna los valores del dict
print('uno' in vals)  # True porque es un valor
print()

'''

El operador `in` utiliza diferentes algoritmos para listas y diccionarios.  
Para las listas, busca los elementos de la lista en orden, como se 
menciona en la Sección.  
A medida que la lista se hace más larga, el tiempo de búsqueda aumenta 
en proporción directa.

Las llaves `{}` representan un diccionario vacío.  
Para añadir elementos al diccionario, puedes usar corchetes `[]`.  
El orden de los pares clave-valor puede no ser el mismo. Si escribes 
el mismo ejemplo  en tu computadora, podrías obtener un resultado diferente.  
En general, el orden de los elementos en un diccionario es impredecible.

Los diccionarios en Python usan una estructura de datos llamada tabla 
hash (hashtable) que tiene una propiedad notable:  
el operador `in` tarda aproximadamente la misma cantidad de tiempo, 
sin importar cuántos  elementos tenga el diccionario.

Una implementación es una forma de realizar una computación; algunas 
implementaciones son mejores  que otras.  
Por ejemplo, una ventaja de la implementación del diccionario es 
que no necesitamos saber de antemano qué letras aparecen en la cadena, 
y solo tenemos que hacer espacio  para las letras que realmente aparecen.

'''
# Combining dict with zip yields a concise way to create a dictionary:
d = dict(zip('abc', range(3)))
print(d)  # {'a': 0, 'c': 2, 'b': 1}
dict33 = {}


def mas_frecuente(cadena):
    cad1 = sorted(list(cadena.lower()))
    diccionario = {}

    for item in cad1:
        if item in diccionario.keys():
            diccionario[item] += 1
        else:
            diccionario[item] = 1
    return diccionario


cadena = 'JaimeRamirezArbelaez'
print(f'mas_frecuente(cadena) = {mas_frecuente(cadena)}')
# Otra solución:
cadena = 'brontosaurio'
lx = sorted(cadena.lower())
print(f'lx = {lx}')
d = {letra: lx.count(letra) for letra in lx}  # cuenta las letras n veces
print(f'd = {d}')


def histograma(cadena):
    dic_h = dict()
    for letra in cadena:
        if letra not in dic_h:
            dic_h[letra] = 1
        else:
            dic_h[letra] += 1
    return dic_h


s = 'brontosaurio'
h = histograma(s)
print(f'h = {h}')

print(h.get('o', 0), h['o'])  # generan (3, 3), pero si usamos
# una 'key' que no existe
# genera 0  h['x'] produce un KeyError
print('o' in h)


def histograma1(cadena):
    dic_h = dict()
    for letra in cadena:
        dic_h[letra] = dic_h.get(letra, 0) + 1
    return dic_h


s = 'brontosaurio'
h1 = histograma1(s)
print(f'h1 = {h1}')
'''

`get` es un método que retorna el valor de la llave, si existe.

Los diccionarios tienen un método llamado `get` que toma una 
clave y un valor por defecto. Si la clave  
aparece en el diccionario, `get` devuelve el valor correspondiente;
de lo contrario, devuelve  
el valor por defecto.


'''

print()

'''
Ciclos y diccionarios  
Si utilizas un diccionario en una instrucción `for`, recorre las claves  
del diccionario.  
Por ejemplo, `print_hist` imprime cada clave y el valor correspondiente:
'''


def print_hist(h):
    for c in h:
        print(c, h[c])


print_hist(h)
print()
'''

Para recorrer las claves en orden , puedes usar la
función incorporada sorted.:
'''
for key in sorted(h):
    print(key, h[key])

print()
'''

Búsqueda inversa  
Dado un diccionario `d` y una clave `k`, es fácil encontrar 
el valor correspondiente `v = d[k]`.  
Esta operación se llama una búsqueda.

Pero, ¿qué sucede si tienes `v` y quieres encontrar `k`? 
Tienes dos problemas: primero,  
puede haber más de una clave que esté asociada al valor `v`.  
Dependiendo de la aplicación, podrías elegir una, o podrías tener que  
hacer una lista que contenga todas ellas.  
Segundo, no existe una sintaxis simple para hacer una 
búsqueda inversa; tienes que buscar manualmente.

Aquí tienes una función que toma un valor y devuelve 
la primera clave que se asocia a ese valor:

'''


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


'''

Esta función es otro ejemplo del patrón de búsqueda, pero utiliza 
una característica  que no hemos visto antes: `raise`.  
La instrucción `raise` provoca una excepción; en este caso, provoca 
un `LookupError`, que  es una excepción incorporada utilizada para indicar  
que una operación de búsqueda falló.
'''

print(reverse_lookup(h, 3))
print()
h = histograma('parrot')
key = reverse_lookup(h, 1)
print(key)
print()

'''
Diccionarios y listas
Las listas pueden aparecer como valores en un diccionario. Por ejemplo, 
si se te da un diccionario que asigna letras a frecuencias, podrías 
querer invertirlo; es decir, crear un diccionario que asigne frecuencias 
a letras. Dado que puede haber varias letras con la misma frecuencia, 
cada valor en el diccionario invertido debería ser una lista de
letras.
'''


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


hist = histograma('parrot')
print(hist)
# {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
inverse = invert_dict(hist)
print(inverse)
# {1: ['a', 'p', 't', 'o'], 2: ['r']}
'''
Las listas pueden ser valores en un diccionario, como muestra este
ejemplo, pero no pueden ser claves.

Una tabla hash es una función que toma un valor (de cualquier tipo) 
y devuelve un número entero.
Los diccionarios usan estos enteros, llamados valores hash,
 para almacenar y buscar pares clave-valor.
'''

dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
print(dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print(dict['a'])  ## Simple lookup, returns 'alpha'
dict['a'] = 6  ## Put new key/value into dict
print('a' in dict)  ## True
## print dict['z']                  ## Throws KeyError
if 'z' in dict: print(dict['z'])  ## Avoid KeyError
print(dict.get('z'))  ## None (instead of KeyError)

'''


Un bucle for en un diccionario itera sobre sus claves por defecto.
Las claves aparecerán en un orden arbitrario.
Los métodos dict.keys() y dict.values() devuelven listas de las 
claves o valores explícitamente.

También existe items(), que devuelve una lista de tuplas (clave, valor),
lo cual es la forma más eficiente de examinar todos los datos clave-valor 
en el diccionario.
Todas estas listas pueden pasarse a la función sorted().
Por defecto, iterar sobre un diccionario itera sobre sus claves.
Ten en cuenta que las claves están en un orden aleatorio.
dict['a'] = 'alpha'
'''
for key in dict: print(key)
## prints a g o

## Exactly the same as above
for key in dict.keys(): print(key)

## Get the .keys() list:
print(dict.keys())  ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print(dict.values())  ## ['alpha', 'omega', 'gamma']

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
    print(key, dict[key])

## .items() is the dict expressed as (key, value) tuples
print(dict.items())  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print(k, '>', v)
## a > alpha    o > omega     g > gamma

'''
Formato de diccionarios
El operador % funciona convenientemente para sustituir 
valores de un diccionario en una cadena por nombre:
'''
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'Quiero %(count)d copias de %(word)s' % hash
print(s)
# %d para entero, %s para cadena
# 'Quiero 42 copias de garfield'

'''
Dict Formatting
The % operator works conveniently to substitute values 
 from a dict into a stringby name: 
 hash = {} 
 hash['word'] = 'garfield' 
 hash['count'] = 42 
 s = 'I want %(count)d
# copies of %(word)s'
# % hash # %d for int, %s for string 
# 'I want 42 copies of garfield'
'''
var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]  ## Delete first element
del list[-2:]  ## Delete last two elements
print(list)  ## ['b']

dict = {'a': 1, 'b': 2, 'c': 3}
del dict['b']  ## Delete 'b' entry
print(dict)  ## {'a':1, 'c':3}


# Uso de kwargs:
def calculate(n, **kwargs):  # **kwargs keyworded arguments is a dictionary
    for key, value in kwargs.items():
        print(kwargs.items(), type(kwargs.items()))  # --> [('add',3),('multiply',6)] 2 elementos
        print(key)
        print(value)
        print(kwargs[key])
    n = (n + kwargs['add']) * kwargs['multiply']
    print(n)
    n *= kwargs['multiply']
    print(n)
    # kwargs = {'add':3,'multiply':6}
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    # print(n)
    return n


print(calculate(5, add=3, multiply=6))


# **kwargs

def calculate1(n, **kwargs):
    for key, value in kwargs.items():
        print(kwargs.items(), type(kwargs.items()))  # --> [('add',3),('multiply',6)] 2 elementos
        print(key)
        print(value)
        print(kwargs[key])
        n += kwargs['add']
        print(n)
        n *= kwargs['multiply']
    return n


print(calculate1(5, add=3, multiply=6))

# dictionary comprehension:
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# {key: value_if_true if condition else value_if_false for item in iterable}
numeros = [1, 2, 3, 4, 5]
resultado = {num: "par" if num % 2 == 0 else "impar" for num in numeros}

print(resultado)
# {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}
# invertir y agrupar:
res_inv = {}
for c, v in resultado.items():
    if v not in res_inv:
        res_inv[v] = [c]
    else:
        res_inv[v].append(c)
print(res_inv)
import random as rn

names = ['Alex', 'Bob', 'Caro', 'Jim', 'Joe', 'Tim', 'Tom']

new_dict = {name: rn.randint(0, 100) for name in names}
stud_ap = {name: new_dict[name] for name in names if new_dict[name] >= 60}
stud_ap1 = {name: score for (name, score) in new_dict.items() if score >= 60}
print(stud_ap, stud_ap1)
print(f'new_dict={new_dict}')
str1 = 'Hola soy Jaime'
l1 = str1.split(' ')
l2 = str1.split()
print(l1, l2)

ndict = {l1[i]: len(l1[i]) for i in range(len(str1.split(' ')))}
ndict1 = {word: len(word) for word in str1.split()}
ndict3 = {word: 2 * (len(word)) for word in ndict1}
print(ndict, ndict1, ndict3)
student_dict = {'students': ['Jim', 'Tim', 'Jack', 'Tom'],
                'scores': [70, 80, 90, 85]}

# looping through dictionary
for (key, value) in student_dict.items():
    print(key)
    print(value)


# **kwargs permite a una función aceptar un número indefinido de argumentos
# con nombre, los cuales se empaquetan en un diccionario.
#
# Ejemplos de **kwargs:

def mostrar_informacion(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


mostrar_informacion(nombre="Juan", edad=30, ciudad="Madrid")


# Salida:
# nombre: Juan
# edad: 30
# ciudad: Madrid

def construir_url(base_url, **kwargs):
    url = base_url + "?"
    for key, value in kwargs.items():
        url += f"{key}={value}&"
    return url.rstrip('&')


url = construir_url("https://api.example.com/data", search="python", page=2, limit=10)
print(url)


# Salida: https://api.example.com/data?search=python&page=2&limit=10

# Caso Práctico: Útil para funciones que necesitan manejar
# configuraciones o parámetros que pueden variar, como en el
# caso de construir URLs dinámicas.

# Combinando *args y **kwargs
# También puedes usar *args y **kwargs juntos en la misma función
# para aceptar tanto argumentos posicionales como nombrados.
#
# Ejemplo Combinado:

def combinar_args_kwargs(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print("args:", args)
    print("kwargs:", kwargs)


combinar_args_kwargs(1, 2, 3, 4, 5, clave1="valor1", clave2="valor2")


# Salida:
# arg1: 1
# arg2: 2
# args: (3, 4, 5)
# kwargs: {'clave1': 'valor1', 'clave2': 'valor2'}

# Orden en la Declaración de los Argumentos
# Cuando se usan *args y **kwargs en la definición de una función,
# deben seguir este orden:
#
# Argumentos posicionales estándar.
# *args para argumentos posicionales variables.
# Argumentos con nombre estándar.
# **kwargs para argumentos con nombre variables.
# Ejemplo Completo:
def ejemplo_completo(arg1, arg2, *args, kwarg1=None, kwarg2=None, **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print("args:", args)
    print(f"kwarg1: {kwarg1}")
    print(f"kwarg2: {kwarg2}")
    print("kwargs:", kwargs)


ejemplo_completo(10, 20, 30, 40, 50, kwarg1="A", kwarg2="B", extra1="X", extra2="Y")


# Salida:
# arg1: 10
# arg2: 20
# args: (30, 40, 50)
# kwarg1: A
# kwarg2: B
# kwargs: {'extra1': 'X', 'extra2': 'Y'}

# Desempaquetado de Argumentos con * y **
# Cuando llamas a una función, también puedes usar * y **
# para desempaquetar argumentos de listas o diccionarios.
#
# Ejemplo de Desempaquetado con * y **:

def sumar(a, b, c):
    return a + b + c


# Usando una lista
args = [1, 2, 3]
print(sumar(*args))  # Salida: 6

# Usando un diccionario
kwargs = {'a': 4, 'b': 5, 'c': 6}
print(sumar(**kwargs))  # Salida: 15

# Resumen:
# *args: Recoge múltiples argumentos posicionales en una tupla.
# **kwargs: Recoge múltiples argumentos nombrados en un diccionario.
# Combinación y Desempaquetado: Se pueden usar juntos en la misma
# función y se puede desempaquetar argumentos al llamar a la función.
# Este enfoque flexible es muy útil en situaciones donde la cantidad
# de entradas puede variar o no es fija.


'''

df = pd.DataFrame(student_dict)
print(df)
#looping through a dataframe
for (key,value) in df.items():
    print(key)
    print(value)
#looping through rows of a dataframe
for (index,row) in df.iterrows():
    print(index)
    print(row)



data = pd.read_csv('nato_phonetic_alphabet.csv')
print(data.letter,data.code)
for (index,row) in data.iterrows():
    newdict={}

    for i in range(26):
        d={data.letter[i]:data.code[i]}

        newdict.update(d)
print(newdict)
#data_dict = {data.letter:data.code for (index,row) in data.iterrows() }
for (index,row) in data.iterrows():
    newdict1 = {data.letter[i]:data.code[i] for i in range(26)}
#print(newdict1)

name = input('nombre =  ')
NAME =name.upper()
print(NAME)
listlet= []
for letter in NAME:
    print(letter)
    if letter in newdict1.keys():
        listlet.append(newdict1[letter])
print(listlet)
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)
listlet= []
for letter in NAME:
    #print(letter)
    if letter in newdict1.keys():
        listlet.append(newdict1[letter])
print(listlet)
n_l = [phonetic_dict[letter] for letter in NAME]
print(n_l)

# La secuencia de Fibonacci es una serie de números en la cual 
cada número es la suma de los dos números anteriores.
# Comienza con los números 0 y 1, y a partir de ahí, cada número 
se obtiene sumando los dos números anteriores.
# La secuencia comienza como sigue: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# to keep track of values that have already been computed by storing 
them in a dictionary.
# A previously computed value that is stored for later use is called a MEMO.
# Ejemplo de uso de la función fibonacci





known = {0:0, 1:1}  #memo

def fibonacci1(n):
    if n in known:
        return known[n]

    res = fibonacci1(n-1) + fibonacci1(n-2)
    print(res)
    known[n] = res
    return res

n = 9
print(f"El número Fibonacci en la posición {n} es: {fibonacci1(n)}")

'''


# **kwargs: Argumentos Nombrados Variables
def calculate(n, **kwargs):  # **kwargs es un diccionario
    for key, value in kwargs.items():
        print(kwargs.items(), type(kwargs.items()))  # --> [('add',3),('multiply',6)] 2 elementos
        print(key)
        print(value)
        print(kwargs[key])
    n = (n + kwargs['add']) * kwargs['multiply']
    print(n)
    n *= kwargs['multiply']
    print(n)
    # kwargs = {'add':3,'multiply':6}
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    # print(n)
    return n


# En este caso el diccionario debe ser: {'add':valor1,multiply:valor2}
print(calculate(5, add=3, multiply=6))


# para usar la función hay que  entrar
# los valores ' de 'add' y 'multiply' del diccionario
# y el valor de n que no forma parte del diccionario.


def calculate1(n, **kwargs):
    for key, value in kwargs.items():
        print(kwargs.items(), type(kwargs.items()))
        # --> [('add',3),('multiply',6)] 2 elementos
        print(key)
        print(value)
        print(kwargs[key])
        n += kwargs['add']
        print(n)
        n *= kwargs['multiply']
    return n


print(calculate1(5, add=6, multiply=9))

# *args: Argumentos Posicionales Variables
# *args permite a una función aceptar un número indefinido de
# argumentos posicionales.
# Estos argumentos se empaquetan en una tupla.

productos = [
    {"nombre": "laptop", "precio": 1000},
    {"nombre": "tablet", "precio": 500},
    {"nombre": "smartphone", "precio": 800}
]
ordenados_por_precio = sorted(productos, key=lambda x: x["precio"])
print(ordenados_por_precio)
# Salida: [{'nombre': 'tablet', 'precio': 500}, {'nombre': 'smartphone', 'precio': 800}, {'nombre': 'laptop', 'precio': 1000}]

'''Aquí usamos `lambda x: x["precio"]` para ordenar los diccionarios 
   por el valor de `"precio"`.'''
print(texto.split(' '))




#Crea un diccionario que contenga información sobre una
# persona: nombre, edad y ciudad.
persona = {
    'nombre':'Juan',
    'edad':15,
    'ciudad':'Tarso'
}
print(persona, type(persona))
print(dir(persona))

#['__class__', '__class_getitem__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getstate__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__ior__',
# '__iter__', '__le__', '__len__', '__lt__', '__ne__',
# '__new__', '__or__', '__reduce__', '__reduce_ex__',
# '__repr__', '__reversed__', '__ror__', '__setattr__',
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values']

#Imprime el valor asociado a la clave "edad" del diccionario anterior.
print(persona['edad'])         # 15

#Agrega la clave "profesión" con el valor "Ingeniero" al diccionario.
persona['profesión'] = 'Ingeniero'
print(persona)         # {'nombre': 'Juan', 'edad': 15,
                       # 'ciudad': 'Tarso', 'profesión': 'Ingeniero'}

# Imprime cada clave y su valor en líneas separadas.
for clave in persona.keys():
    print(clave)

'''
nombre
edad
ciudad
profesión
'''

# Dada una lista de palabras, crea un diccionario con la cantidad
# de veces que aparece cada una.
cuenta_pal = {}
palabras = ["sol", "luna", "sol", "estrella", "luna", "sol"]
for palabra in palabras:
    if palabra not in cuenta_pal:
        cuenta_pal[palabra] = 1
    else:
        cuenta_pal[palabra] += 1
print(cuenta_pal)

#Elimina la clave "ciudad" del diccionario persona.
del persona['ciudad']
print(persona)

#Crea un diccionario donde cada clave sea el nombre de un
# estudiante y el valor sea una lista de sus notas. Luego
# imprime el promedio de cada estudiante.
estudiantes = {
    "Ana": [10, 9, 8],
    "Luis": [7, 8, 7],
    "Marta": [9, 10, 10]
}

for nombre, notas in estudiantes.items():
    promedio = round((sum(notas) / len(notas)),2)
    print(nombre, "→ Promedio:", promedio)


# Diccionario de estudiantes con materias y notas
estudiantes = {
    "Ana": {"Matemáticas": 8, "Historia": 9, "Biología": 10},
    "Luis": {"Matemáticas": 6, "Historia": 7, "Biología": 8},
    "Marta": {"Matemáticas": 9, "Historia": 10, "Biología": 9}
}
for name,notas in estudiantes.items():
    suma = 0
    for nota in notas.values():
        suma += nota
    print(f' promedio de {name} = {suma/len(notas)}')

# Calcular e imprimir el promedio de cada estudiante
for nombre, materias in estudiantes.items():
    total = sum(materias.values())
    cantidad = len(materias)
    promedio = total / cantidad
    print(f"{nombre} → Promedio: {promedio:.2f}")

#Invierte un diccionario, es decir, que las claves pasen a ser
# valores y viceversa.
notas = {"Matemáticas": 8, "Historia": 9, "Biología": 10}
nota_inv = {}
for mat,nota in notas.items():
    nota_inv[nota] = mat
print(nota_inv)

# Diccionario de estudiantes con materias y notas
estudiantes = {
    "Ana": {"Matemáticas": 8, "Historia": 9, "Biología": 10},
    "Luis": {"Matemáticas": 6, "Historia": 7, "Biología": 8},
    "Marta": {"Matemáticas": 9, "Historia": 10, "Biología": 9}
}

# Calcular promedio y mejores/peores materias
for nombre, materias in estudiantes.items():
    total = sum(materias.values())
    cantidad = len(materias)
    promedio = total / cantidad

    # Buscar mejor y peor materia
    mejor_materia = max(materias, key=materias.get)
    peor_materia = min(materias, key=materias.get)

    print(f"\nEstudiante: {nombre}")
    print(f"Promedio: {promedio:.2f}")
    print(f"📚 Mejor materia: {mejor_materia} ({materias[mejor_materia]})")
    print(f"📉 Peor materia: {peor_materia} ({materias[peor_materia]})")


#imprima el nombre de la materia con mejor o peor nota de cada estudiante


#Crea un diccionario a partir de dos listas: una con claves y
# otra con valores.
claves = list(notas.keys())
valores = list(notas.values())
print(claves,valores)
dic1 = {clave:valor for clave,valor  in zip(claves,valores)}
print(dic1)

#otra solucion:
print(dict(zip(claves,valores)))

#Dado un diccionario con productos y precios, crea uno nuevo
#solo con los productos que cuesten más de 100.

productos = {
    "laptop": 1200,
    "mouse": 25,
    "teclado": 80,
    "monitor": 200
}
dic2 = {clave:valor for clave,valor in productos.items() if productos[clave]>100}
print(dic2)

#
name = 'Gloria'
dic3 = {i:v for (i,v) in enumerate(name)}
print(dic3)

lista_meses = [
    (1, "enero"), (2, "febrero"), (3, "marzo"),
    (4, "abril"), (5, "mayo"), (6, "junio"),
    (7, "julio"), (8, "agosto"), (9, "septiembre"),
    (10, "octubre"), (11, "noviembre"), (12, "diciembre")
]
dic4 = {x:y for (x,y) in lista_meses}
print(dic4)

print(dic4.get(15))

'''

## 🟢 **Nivel Básico**

1. **Crear diccionario de país y capital:**  
   Crea un diccionario con 3 países y sus capitales. Luego imprime 
   la capital de un país.
'''
capitales = {
    'Colombia': 'Bogotá',
    'Perú':'Lima',
    'Venezuela':'Caracas'
}
print(capitales['Venezuela'])
'''
2. **Agregar clave y valor:**  
   Crea un diccionario de persona (`nombre`, `edad`) y añade una 
   nueva clave `ocupación`.

'''
personas = {
    'nombre':'Frank',
    'edad':45,
}
personas['profesión']= 'ingeniero'
personas['ciudad']='Medellin'
print(personas)
'''
3. **Verificar si una clave existe:**  
   Dado un diccionario, verifica si existe la clave `"email"`.

'''
print('ciudad' in personas)
print(personas.get('ciudad','no existe'))
'''
4. **Eliminar una clave:**  
   Quita la clave `"ciudad"` de un diccionario.

'''
del personas['ciudad']
print(personas)
print(personas.get('ciudad','no existe'))

'''
5. **Recorrer claves y valores:**  
   Usa un bucle `for` para imprimir todos los pares clave:valor 
   de un diccionario.'''

for clave,valor in personas.items():
    print(clave,valor)



'''
## 🟡 **Nivel Intermedio**

6. **Contador de palabras:**  
   Dada una lista de palabras, crea un diccionario con la frecuencia de cada una.'''

palabras = ["sol", "luna", "sol", "estrella", "luna", "sol","luna"]
frecuencia = {}
for palabra in palabras:
    if palabra not in frecuencia:
        frecuencia[palabra] = 1
    else:
        frecuencia[palabra] += 1
print(frecuencia)


'''
7. **Diccionario de listas:**  
   Crea un diccionario donde las claves sean estudiantes y los valores 
   una lista de sus notas. Calcula el promedio de cada uno.
'''
notas ={
    'Alf':[9,10,7],
    'Bert':[7,10,10],
    'Carl':[8,9,10]
}
print(notas)

'''
8. **Invertir diccionario:**  
   Dado un diccionario `{"a": 1, "b": 2}`, invierte las claves 
   por los valores → `{1: "a", 2: "b"}`.'''

d1 = {"a": 1, "b": 2}
dinv = {}
for c,v in d1.items():
    dinv[v] = c
print(dinv)

'''
9. **Combinar dos listas en un diccionario:**  
   Une `["nombre", "edad"]` y `["Ana", 25]` en un diccionario.'''

l1 = ["nombre", "edad"]
l2 = ["Ana", 25]

d2 = {c:v for c,v in zip(l1,l2)}
print(d2)

'''
10. **Filtrar elementos según valor:**  
    Dado un diccionario de productos y precios, crea uno nuevo 
    con los productos que cuesten más de 100.'''
productos = {
    "laptop": 1200,
    "mouse": 25,
    "teclado": 80,
    "monitor": 200
}
d3 = {prod:prec for (prod,prec) in productos.items() if prec > 100}
print(d3)

'''
## 🔴 **Nivel Avanzado**

11. **Diccionario anidado de estudiantes y materias:**  
    Crea un diccionario donde cada estudiante tenga otro diccionario 
    con sus materias y notas. Calcula promedios.'''

notas1 = {
    'Alf': {
        'Mat': 9,
        'Hist' : 10,
        'Fisica': 7
    },
    'Bert' : {
        'Mat': 9,
        'Hist' : 10,
        'Fisica': 9
    },
    'Carl' : {
        'Mat': 9,
        'Hist' : 10,
        'Fisica': 9
    }
}
print(notas1)

'''
12. **Agrupar elementos por categoría:**  
    Dada una lista de tuplas `(producto, categoría)`, agrúpalos 
    en un diccionario por categoría.'''
datos = [("lápiz", "útiles"), ("manzana", "fruta"), ("cuaderno", "útiles")]
d4 = {}

for prod,cat in datos:
    if cat not in d4:
        d4[cat] = [prod]
    else:
        d4[cat].append(prod)
print(d4)
#Otra solución:
'''
El método setdefault() es muy útil cuando trabajas con diccionarios, 
especialmente cuando quieres agregar una clave con un valor por 
defecto solo si la clave no existe aún.

🔹 Sintaxis básica:
diccionario.setdefault(clave, valor_por_defecto)
Si la clave ya existe en el diccionario, no la cambia y simplemente 
devuelve su valor actual.

Si la clave no existe, la agrega al diccionario con el 
valor_por_defecto y devuelve ese valor.
'''
d5 = {}
for prod,cat in datos:
    d5.setdefault(cat,[]).append(prod)
print(d5)

'''
13. **Contar letras de una frase:**
    Dada una cadena, crea un diccionario que cuente cuántas veces 
    aparece cada letra (ignora espacios).'''

cad = 'Carlos Antonio Pizarro'
cad1 = cad.lower()
d6 = {}
for letra in cad1:
    print(letra)
    if letra == ' ':
        continue
    elif letra not in d6:
        d6[letra] = 1
    else:
        d6[letra] += 1
print(d6)

#Otra solución:
frase = "hola mundo"
contador = {}
for letra in frase.replace(" ", ""):
    contador[letra] = contador.get(letra, 0) + 1
print(contador)

'''
14. **Ordenar diccionario por valor:**  
    Dado un diccionario, ordénalo de menor a mayor según los valores.'''

print(d6)
ordenado = dict(sorted(d6.items(),key=lambda x:x[1]))
print(ordenado)
'''
15. **Diccionario de contactos:**  
    Crea un programa que permita agregar, buscar, y eliminar contactos 
    usando un diccionario (clave: nombre, valor: teléfono).'''
agenda = {}
agenda["Ana"] = "555-1234"
agenda["Luis"] = "555-5678"
print(agenda)
print(agenda["Ana"])
del agenda["Luis"]
print(agenda)





'''
16. **Análisis de texto:**  
    Dado un texto largo, cuenta cuántas veces aparece cada palabra. 
    Devuelve las 3 palabras más comunes.'''

texto = "uno dos dos tres tres tres"
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
top = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]
print(top)

'''
17. **Diccionario con listas anidadas:**  
    Cada clave es un proyecto, y su valor es una lista de 
    participantes. Imprime cuántos proyectos tiene cada persona.'''
proyectos = {
    "Proyecto A": ["Ana", "Luis"],
    "Proyecto B": ["Luis", "Marta"],
    "Proyecto C": ["Ana"]
}
personas = set(proyectos["Proyecto A"] + proyectos["Proyecto B"] + proyectos["Proyecto C"])
print(personas)

for persona in personas:
    pass

print('Ana' in proyectos['Proyecto A'] )

# +set(proyectos["Proyecto B"])+set(proyectos["Proyecto C"]))

#print(f'personas = {personas}')
#for proyecto in proyectos:
    #pass
'''
18. **Crear índice de palabras:**  
    Dada una lista de oraciones, crea un diccionario que diga
    en qué líneas aparece cada palabra.

19. **Actualizar stock de productos:**  
    Tienes un diccionario de productos y cantidades.
    Permite aumentar o disminuir stock según ventas.

20. **Histograma simple:**  
    Dado un diccionario con letras y cantidades,
    dibuja un histograma en consola.

---

¿Te gustaría que te dé la **solución** de alguno de estos ahora?
¿O prefieres que los arme todos juntos como una guía con soluciones?
'''