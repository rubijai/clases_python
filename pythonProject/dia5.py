#   Unidad 5: Funciones
#   Cuando una tarea determinada se realiza muchas veces a lo largo de un
#   programa, generalmente se encapsula dentro de una función para que
#   pueda ser utilizada o "llamada" cuando sea necesario. Esta noción de
#   crear una función específica o "procedimiento" para lograr una tarea
#   determinada es parte de una metodología de programación conocida
#   como "programación por procedimientos".

#   Las funciones son útiles cuando tenemos una sección de código que
#   necesitamos usar una y otra vez. Al poner la sección de código en
#   forma de función, permitimos la reutilización del código al llamar
#   a la función. Las funciones reciben valores de entrada(parámetros),
#   luego realizan un cálculo utilizando la entrada y, finalmente,
#   devuelven valores como resultado de la función. Python tiene muchas
#   funciones incorporadas (built_in function), como print, type y len
#   (con las que ya tienes experiencia). Por ejemplo, en el caso de la
#   función len, la entrada es una lista o una cadena y la salida es
#   el número de elementos contenidos en la lista o cadena.
#   Veamos unos ejemplos:

lista_numeros = [2*x + 3 for x in range(11)]
# La expresión 2*x + 3 se usa para crear los elementos de la
# lista_numeros, donde x lo obtenemos de un rango de valores usando
# la función 'range' o recorriendo un iterable.
print(f'lista_numeros = {lista_numeros}')

# print es una función propia de Python (built-in-function)
print(len(lista_numeros), type(lista_numeros))

# 'len' y 'type' son también funciones de Python

#   Los métodos son funciones que se pueden usar con objetos. Ya has
#   utilizado varios métodos asociados con listas (como append) y con
#   cadenas (como find). Aprenderemos sobre la creación de métodos
#   cuando lleguemos a la programación orientada a objetos.
#   Pero, cabe destacar que la idea de usar un método es similar
#   a la de una función en el sentido de que los métodos tienen valores
#   de entrada y devuelven valores de salida.

lista_numeros.append(100)
print(f'lista_numeros = {lista_numeros}')

# lista_numeros es una variable global válida para todo el script.

# append es un método de las listas en Python, este método es un tipo
# de función

#   Supongamos que tienes una lista de datos numéricos y te gustaría
#   encontrar un valor promedio de los números en esa lista.
#   Supongamos además que tienes un 'script' que debe realizar este
#   cálculo en muchos puntos diferentes dentro del programa.
#   Bajo estas circunstancias, tiene sentido escribir
#   una función para resolver este problema. Veamos:


# promedio = suma_de_elementos/numero_total de elementos

a = [i**2 for i in range(1,21) if i%2 == 0]
print(f'a = {a}')

# encontrar el promedio de la lista a:
suma = 0
for x in a:
    suma += x
promedio = suma/(len(a))
print(f'promedio de lista a = {promedio}')

b = [x for x in a if x <= 250]
print(f'a = {a}')

# encontrar el promedio de la lista b:
suma = 0
for x in b:
    suma += x
promedio = suma/(len(b))
print(f'promedio de lista b = {promedio}')

# encontrar el promedio de la lista c, donde c:
c = [x**3 for x in range(1,11) ]
print(f'c = {c}')
# encontrar el promedio de la lista c:
suma = 0
for x in c:
    suma += x
promedio = suma/(len(c))
print(f'promedio de lista c = {promedio}')

#   El promedio lo podemos calcular usando el concepto de función
#   tal como lo explicamos a continuación:

'''
El **argumento de una función** en Python (y en otros lenguajes de
programación) es el **valor o dato que le pasas a una función cuando
la llamas**, para que esta lo use dentro de su ejecución.


### 🧠 Explicación simple:

- **Definición:** Cuando defines una función, puedes usar **parámetros**
    (variables que la función espera recibir).
- **Argumentos:** Son los **valores reales** que pasas a esos parámetros
    cuando llamas a la función.



### 📌 Ejemplo básico:

def saludar(nombre):  # ← "nombre" es el parámetro
    print(f"Hola, {nombre}!")

saludar("Ana")         # ← "Ana" es el argumento


**Resultado:**

Hola, Ana!


### 🔁 Diferencia entre parámetro y argumento:

| Término       | ¿Dónde aparece?             | Ejemplo              |
|---------------|-----------------------------|----------------------|
| **Parámetro** | En la definición de la función | `def saludar(nombre):` |
| **Argumento** | Al llamar a la función       | `saludar("Ana")`     |


### 🧩 Tipos de argumentos en Python:

1. **Posicionales:** Van en orden.
   ```python
   def sumar(a=3, b=4, c=23):
       return a + b + c

   print(sumar())  # → 3 y 4 son argumentos posicionales


2. **Nombrados (por clave):**

   print(sumar(a=3, b=4, c=23))


3. **Por defecto:** Le das un valor si no se pasa argumento.

   def saludar(nombre="amigo"):
       print(f"Hola, {nombre}!")


4. **Arbitrarios:** Para recibir muchos argumentos:

   def sumar_todos(*numeros):
       return sum(numeros)

   print(sumar_todos(1, 2, 3, 4))  # → *numeros es una tupla de argumentos

4. **kwargs:** Para recibir muchos argumentos en forma de diccionario:
    def  calcular(n,**calc):                  # calc es un diccionario--> {mult:10, suma:10}.
                                              # El diccionario se va actualizando en la medida
                                              # que agregue operaciones.
    res = n*calc['mult'] + calc['suma']
    return res

print(calcular(10,mult=10,suma=10))

'''

def promedio(lista_de_numeros):          # def es palabra clave para
                                         # definir una función.
    #   lista_de_numeros es la lista de entrada (parametro de entrada)
    #   Esta función devuelve (return) el valor del promedio de los
    #   numeros de la lista_de_numeros.
    suma = 0
    for item in lista_de_numeros:
        suma += item
    promedio = suma/len(lista_de_numeros)
    return promedio # Es muy importante ubicar return apropiadamente
                    # una vez se ejecuta 'return' se devuelve el
                    # resultado de la función. Cuando no aparece 'return'
                    # la función devuelve None.

print(f'promedio(a)={promedio(a)}')
print(f'promedio(b)={promedio(b)}')
print(f'promedio(c)={promedio(c)}')

prom_a = promedio(a)
print(prom_a)

prom_b = promedio(b)
print(prom_b)

prom_c = promedio(c)
print(prom_c)

# Veamos otro ejemplo: quiero saber si una letra 'x' está en una cadena.
def encontrar_letra(cadena, x):
    #   cadena es la cadena de entrada
    #   x es la letra  que se busca
    #   Esta función devuelve un valor booleano True,
    #   si se encuentra la letra
    #   y devuelve un valor booleano False si no se encuentra.
    #   Las variables cadena y x son variables locales, que solo son
    #   válidas dentro de la función (distinción muy importante)
    for letra in cadena:
        #print(letra)
        if (letra == x):
            return True
            #return False    #Es muy importante ubicar 'return' apropiadamente
        # return False
    return False


#   termina la definicion de la funcion
#   =====================

#  La palabra clave 'def' informa a Python que se está declarando
#  una función.
#  Observa los (:) y la sangría con reglas similares a las
#  sentencias condicionales y bucles.
#  Nombre de la función:
#  El nombre de la función es 'encontrar_letra'.
#  Entradas: encontrar_letra tiene dos variables de entrada, cadena y x.
#  Salidas: encontrar_letra devuelve una variable de salida de tipo bool.
#  La palabra clave return se encarga de devolver el valor de salida.


#   Aqui empieza el codigo principal ...

cad = 'Esta es una clase de python'
x = 'e'
print((f'{x} está en: {cad}? : {encontrar_letra(cad,x)}'))
print((f'"P" está en: {cad}? : {encontrar_letra(cad,'P')}'))


# Otro ejemplo: Encontrar si un número está en una lista de números:
def encontrar_numero(lista_numero, x):
    #   lista_numero es la lista de entrada
    #   x es el número que se busca
    #   Esta función devuelve un valor booleano True,
    #   si se encuentra el número
    #   y devuelve un valor booleano False si no se encuentra.
    for numero in lista_numero:
        #print(numero)
        if (numero == x):
            return True
            #return False    #Es muy importante ubicar 'return' apropiadamente
        # return False
    return False

# La función anterior se puede simplificar así:
def encontrar_numero1(lista_numero, x):
    return x in lista_numero

print(f'a = {a}')
print(encontrar_numero(a, 4))
print(encontrar_numero(a, 29))
print(encontrar_numero1(a, 4))
print(encontrar_numero1(a, 29))
b = [45, 34, 78, 89]
print(f'b = {b}')
print(encontrar_numero(b, 45))
print(encontrar_numero(b, 1470))
print('...........')


#  Por defecto, las variables utilizadas dentro de la función son locales
#  a la función y gran parte del poder de Python reside en la vasta
#  colección de paquetes, bibliotecas y módulos disponibles para casi
#  cualquier aplicación que puedas imaginar. El módulo math contiene
#  una serie de métodos orientados a las matemáticas, típicos de lo
#  que un programador necesitaría para realizar cálculos básicos.
#  No pueden ser vistos por los comandos principales que siguen.
#  Por convención, las funciones se definen al comienzo de un
#  programa de Python.
#  Es necesario definir las funciones antes de usarlas en el código


import math     # importa el modulo math que contiene las definiciones
                # de las funciones matematicas

# Operaciones básicas:

# math.floor(x): Redondea un número hacia abajo al entero más cercano.
# math.ceil(x): Redondea un número hacia arriba al entero más cercano.

# Funciones trigonométricas:
#
# math.sin(x): Calcula el seno de un ángulo en radianes.
# math.cos(x): Calcula el coseno de un ángulo en radianes.
# math.tan(x): Calcula la tangente de un ángulo en radianes.
# math.asin(x): Calcula el arcoseno de un número.
# math.acos(x): Calcula el arcocoseno de un número.
# math.atan(x): Calcula la arcotangente de un número.

# Funciones exponenciales y logarítmicas:
#
# math.exp(x): Calcula la exponencial de un número.
# math.log(x): Calcula el logaritmo natural (base e) de un número.
# math.log10(x): Calcula el logaritmo en base 10 de un número.

# Otras funciones:
#
# math.sqrt(x): Calcula la raíz cuadrada de un número.
# math.pi: Devuelve el valor de pi (π).
# math.e: Devuelve el valor de e.

a = math.exp(1) # se usa la sintaxis  de un metodo del modulo math
print(a)
b = math.pi
print(b)
x = 100
print(math.log(x, 10))
print(math.log10(x))
y = math.pi / 2
print(math.cos(y))
print(math.sin(y))
y = 8
z = 1 / 3
print(math.pow(y, z))



#  Para simplificar el código, si sabes exactamente qué métodos
#  se necesitan de una biblioteca determinada, puedes seleccionar
#  un subconjunto utilizando la palabra clave from.
#  Considera el código anterior reescrito utilizando la palabra clave from:

from math import exp, pi, log, log10, cos, sin, pow

a = exp(1)      # en este caso no es necesario usar la sintaxis a = math.exp(1)
print(a)
b = pi
print(b)
x = 100
print(log(x, 10))
print(log10(x))
y = pi / 2
print(cos(y))
print(sin(y))
y = 8
z = 1 / 3
print(pow(y, z))  # pow es un metodo del modulo math que se encarga
                  # de elevar un número  y a la potencia z

#   La capacidad de generar números pseudoaleatorios es fundamental
#   en la programación y simulación.
#   El módulo random ofrece un conjunto de métodos para hacerlo.





import random as rn     # rn es un alias random que permite usar rn
                        # en lugar de random en la sintaxis
# Generar números aleatorios:

# random.random(): Genera un número aleatorio flotante entre
# 0.0 (incluido) y 1.0 (excluido).
# random.uniform(a, b): Genera un número aleatorio flotante
# uniformemente distribuido entre a (incluido) y b (excluido).

# Generar enteros aleatorios:

# random.randint(a, b): Genera un número entero aleatorio
# uniformemente distribuido entre a (incluido) y b (incluido).

# Otras funciones:

# random.choice(secuencia): Elige un elemento aleatorio de una lista, tupla o cadena.
# random.shuffle(lista): Mezcla los elementos de una lista de forma aleatoria.
# random.seed(semilla): Inicializa el generador de números aleatorios con una semilla
# específica para obtener resultados reproducibles (opcional).
# Fija la semilla al reloj

rn.seed()         # sin alias seria random.seed()

#   prueba algunos metodos
a = rn.random()                    # numero aleatorio entre 0 y 1
print(a)
b = rn.uniform(7, 20)         # numero aleatorio entre  7  20
print(b)
c = rn.randint(100, 200)      # entero aleatorio entre 100 y 200
print(c)


#    #  Para mayor comodidad, la palabra clave 'as' junto con el comando
#    'import' acorta el nombre de la referencia del módulo de random a 'rn'.
#    La "semilla" de un generador de números aleatorios define el punto
#    de inicio. En aplicaciones reales, quieres establecer la semilla
#    en un valor aleatorio (como la hora del reloj del sistema)
#    de lo contrario, una lista pseudoaleatoria siempre comenzará
#    con el mismo valor y se repetirá.
#    Tres métodos esenciales para generar números aleatorios son:
#    random.random() - generar números de punto flotante entre 0 y 1
#    random.uniform(a, b) - generar números de punto flotante entre a y b
#    random.randint(a, b) - generar enteros entre a y b

# *args

def add(*args):  # *args se puede usar cualquier numero de argumentos
    return sum(args)    # usa la funcion sum de python
print(add(3, 5, 8, 125))  # el numero de argumentos es ilimitado
def pr(*args):
    res = 1
    for x in args:
        print(x)
        res *= x
    return res

res = pr(3, 5, 2,'j')
print(res,len(res))
def add(*args):  # *args se puede usar cualquier numero de argumentos
    # args es un tuple con cualquier numero de argumentos
    # sum = 0
    # for m in args:
    # sum += m
    return sum(args)      # usa la funcion sum de python
print(add(3, 5, 8, 125))  # el numero de argumentos es ilimitado


def add1(a=1, b=2, c=3):  # tiene 3 argumentos con valores iniciales que pueden cambiarse
    sum = a + b + c
    return sum

print(add(3, 4, 7, 10))  # 24
print(add(3, 4))  # 7
print(add1())  # a=1,b=2,c=3       sum = 6
print(add1(c=100))  # a=1,b=2,c=100  mantiene los valores a y b  sum=103

print(add1(c=7))  # a=1,b=2,c=7  sum = 10




def calculate(n,**kwargs):    # **kwargs keyworded arguments is a dictionary
    for key,value in kwargs.items():
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
    #print(n)
    return n

print(calculate(5,add=3,multiply=6))


def calculate1(n,**kwargs):
    for key,value in kwargs.items():
        print(kwargs.items(),type(kwargs.items()))    #--> [('add',3),('multiply',6)] 2 elementos
        print(key)
        print(value)
        print(kwargs[key])
        n += kwargs['add']
        print(n)
        n *= kwargs['multiply']
    return n

print(calculate1(5,add=6,multiply=9))

# *args: Argumentos Posicionales Variables
# *args permite a una función aceptar un número indefinido de argumentos posicionales.
# Estos argumentos se empaquetan en una tupla.
def suma_todos(*args):
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

# Caso Práctico: Útil cuando se quiere sumar un número desconocido de elementos
# o cuando se desean procesar todos los elementos dados sin preocuparse por cuántos son.
# **kwargs: Argumentos Nombrados Variables
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

# Caso Práctico: Útil para funciones que necesitan manejar configuraciones o
# parámetros que pueden variar, como en el caso de construir URLs dinámicas.
# Combinando *args y **kwargs
# También puedes usar *args y **kwargs juntos en la misma función para aceptar
# tanto argumentos posicionales como nombrados.
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
# Cuando llamas a una función, también puedes usar * y ** para desempaquetar
# argumentos de listas o diccionarios.
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