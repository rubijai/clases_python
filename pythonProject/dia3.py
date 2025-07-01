# Usando Declaraciones Condicionales
# Las declaraciones condicionales son necesarias para
# que un programa tome decisiones basadas en un conjunto
# de condiciones lógicas.
# Existen tres construcciones principales en Python para esto:
# la declaración if, las declaraciones if-else y la declaración if-elif.

x_val = int(input('Enter an integer less than 5: ')) #variable entera entrada por teclado
if x_val < 5:                 # si x_val es mayor a 5 se ejecutan los comandos con sangría                                                  # la parte indentada
    print('Hello, Mr. User')
    new_x_val = x_val + 3 * 7
    print('This is your new_x_val: ', new_x_val)
print('Hello, I am James')                          # si no se cumple la condición
                                                    # no ejecuta la parte con sangría
x_val = int(input('Enter an integer greater than 10: '))
# variable entera entrada por teclado
if x_val > 10:                                       # si x_val es mayor a 10 se ejecuta
                                                     # la parte con sangría siguiente:
    print('Hello, Mr. User')
    new_x_val = x_val + 3 * 7
    print('This is your new_x_val: ', new_x_val)
else:                                                # si x_val es menor o igual a 10                                                 # se ejecuta la parte indentada siguiente:
    print('x_value <= 10')
print('Hello, I am James')

# Observa la sintaxis requerida para que la declaración "if" funcione:
# La expresión lógica que sigue a "if" debe terminar con dos puntos (:)
# El código que se ejecutará si la condición lógica es verdadera debe tener sangría.
# La sangría es la forma en que Python sabe que tienes un grupo de comandos
# dentro de la declaración if.

x_val = int(input('Enter an integer greater than 10: '))
if x_val > 10:
    print('Thank you')
    x_val = x_val / 2
    print('This is your value divided by 2: ', x_val)
else:                                              #si no se cumple la condición se
                                                   # ejecuta esta otra parte
    x_val = x_val / 5
    print('This is your value divided by 5: ', x_val)
    print('Which code group executed?')
print()

x_val = int(input('Enter an integer less than 5: ')) #variable entera entrada por teclado
if x_val == 3:                                        # si x_val es mayor a 10 se ejecuta
                                                     # la parte indentada

    print('Hello, Mr. User')
    new_x_val = x_val + 3 * 7
    print('This is your new_x_val: ', new_x_val)
else:
    print('x_value != 3')
print('Hello, I am James')

x_val = int(input('Enter an integer greater than 10: '))  # elif se usa cuando hay
                                                          # diversas posobilidades
if x_val >= 10:
    print('Thank you')
    x_val = x_val / 2
    print('This is your value divided by 2: ', x_val)
elif (x_val < 10) and (x_val > 4):
    x_val = x_val / 5
    print('This is your value divided by 5: ', x_val)
else:
    x_val = x_val * 100
    print('This is your value times 100: ', x_val)
print('Which code group executed?')
print()

# Bucles e Iteraciones
# Usando bucles "while"

# Los bucles son necesarios cuando necesitamos realizar un conjunto de operaciones
# varias veces. El primer tipo de bucle del que hablaremos se llama bucle while.
# El bucle while verifica una condición lógica al igual que la declaración if.
# Si la condición es verdadera, el código dentro del bucle while se ejecutará
# hasta que la condición que se está verificando se vuelva falsa.


x_val = int(input('Please enter the number 10: '))
while (x_val != 10):                                # mientras el valor de x_val sea
                                                    # diferente de 10
    print('Your input value is not equal to 10')
    print('Please try again: ')
    x_val = int(input('Enter the number 10: '))     # si entramos un valor diferente de
                                                    # 10 se repite el proceso
print('Thank you')
print('You entered a value of 10')

# Las reglas de sintaxis son similares a las de las declaraciones "if":
# La expresión lógica que sigue a "while" debe terminar con dos puntos (:)
# El código que se ejecutará si la condición lógica se cumple debe tener sangría.
# La sangría es la forma en que Python sabe que tienes un grupo de comandos dentro
# de la declaración while.


# Usando el bucle "for"
# El bucle for es útil cuando sabemos cuántas veces se debe ejecutar un bucle.
# En lugar de basar el número de iteraciones en una condición lógica, el bucle
# for controla la cantidad de veces que se iterará un bucle contando
# o avanzando a través de una serie de valores.

#Para explicar la función range tomemos una lista de números
# enteros que empiecen en -5 y termine en mas 11:
# (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# la función range requiere 3 argumentos: range(inicio,fin,incremento)
# por defecto inicio = 0 , incremento = 1 por ejemplo si:
for i in range(11):  # fin = 11
    print(i)         # inicio = 0
                     # incremento = 1
                     # imprime desde el 0 hasta el 10 --> anterior
                     # al 11 en la lista

# Se obtiene el mismo resultado usando el siguiente for loop:
for i in range(0,11,1):  # fin = 11
    print(i)             # imprime : (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                         # inicio = 0
                         # incremento = 1
                         # imprime desde el 0 hasta el 10 igual que el
                         # anterior ejemplo. Cuando el incremento es
                         # positivo se recorre la lista
                         # de izquierda a derecha.
                         # Cuando el imcremento es negativo se recorre de
                         # derecha a izquierda

# Ejemplos:
# inicio = -5 fin = 6
for i in range(-5,6):  # por defecto incremento = 1 (recorrido izquierda a derecha)
    print(i)           # empieza en -5 y termina en 5 anterior a fin = 6
# imprime (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5)

# inicio = -5 fin = 6 incremento = 2
for i in range(-5,6,2):
    print(i)
# imprime(-5, -3, -1, 1, 3, 5)

# inicio = -5 fin = 6 incremento = 3
for i in range(-5,6,3):
    print(i)
#  de (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) empieza en -5
#  e incrementa de 3 en 3 --> -5+3=-2, -2+3=1, 1+3=4, 4+3=7 que supera
#  a fin = 6 luego imprime: (-5, -2, 1, 4)

# inicio = 10 fin = 6 incremento = -1
for i in range(10,6,-1):  # incremento = -1 (recorrido derecha a izquierda)
    print(i)              # empieza 10 y termina en el anterior a 6 en el
                          # recorrido,luego imprime: (10, 9, 8, 7)

for i in range(10,-11,-4):  # incremento = -4 (recorrido izquierda a derecha)
    print(i)                # imprime (10, 6, 2, -2, -6, -10)

for i in range(10,-11,-6):  # incremento = -4 (recorrido izquierda a derecha)
    print(i)                # imprime (10, 4, -2, -6, -8)


for i in range(0,11,-1):
    print(i)                # no imprime nada!!!!!!!!!! inicio y fin no
                            # tiene los valores apropiados. Debido a que
                            # incremento = -1,el recorrido es de derecha
                            # a izquierda, luego inicio debe ser mayor que fin
                            # y en este caso no lo es.



n = 8
sumval = 0
for i in range(1,n+1):
    sumval = sumval + i  # Esta sentencia tambien se puede escribir: sumval +=  i
    print('Adding ', i, 'to the previous sum = ', sumval)
print()

n = 8
sumval = 0
for i in range(n):
    sumval += i
    print('Adding ', i, 'to the previous sum = ', sumval)
# Este bucle cuenta desde 0 hasta n-1, donde n ha sido
# establecido con un valor de 8.
# el valor inicial de suma se establece en cero y luego
# se van sumando los valores sucesivos de la variable i a
# la suma cada vez que se realiza una iteración del bucle.
print()

# si quiero imprimir todos los elementos de una cadena:

strval = 'benefactora'
print(len(strval))
for letra in strval:           # recorre los elementos de la cadena
    print(letra)

# Cuenta las veces que está la letra 'a' en la cadena:
a_count = 0
strval = 'benefactora'
for letra in strval:
    if letra == 'a':
        a_count += 1
print(f' a_count = {a_count}')

# Observa cómo la declaración "if" está "anidada" (y, por lo tanto,
# tiene sangría) dentro del bucle "for".
# La variable letra  recorre cada carácter en la cadena strval,
# que ha sido inicializada como la cadena "benefactora". Si se encuentra
# una "a" mientras se itera a través de la cadena,
# la variable a_count se incrementa. Cuando el bucle termina,
# el número de ocurrencias se muestra en pantalla.

# También es posible anidar bucles dentro de bucles


m = 4
n = 3
for i in range(m):
    for j in range(n):
        print('i=', i, ' j=', j)
print()
# Esto se llama bucle "for" anidado porque el bucle "for" interno,
# dependiendo de la variable j, está anidado dentro del bucle "for"
# externo, que depende de la variable i.
# Esto debería ser claro por la sangría del bucle interno con respecto
# al bucle externo. Para cada iteración de la variable i, la variable j
# recorre todos sus valores posibles que dependen de range(m).
# Para que se actualice a su próximo valor, el bucle interno debe
# iterar a través de todos sus valores.

# A veces es necesario salir abruptamente de un bucle cuando se cumple
# una cierta condición.
# La declaración "break" es a veces útil para tal aplicación.

strval = 'benefactora'
for letra in strval:
    print(letra)
    if letra == 'a':
        print('No siga iterando. Pare aquí')
        print('la letra "a" ha sido encontrada')
        break
print('Hola')
# Cuando encuentra la letra 'a' rompe ('break') el bucle for y
# no lo sigue ejecutando.

for letra in strval:
    if letra == 'a':
        print('No imprima la letra "a"')
        continue
    print(letra)

print('Hola')
# Cuando encuentra la letra 'a' continúa ('continue') el bucle for y
# salta a la siguiente letra.

for letra in strval:
    if letra == 'a':
        pass
        print('Hola, que pasó????')
    print(letra)

print('Hola')
# Cuando encuentra la letra 'a' el comando 'pass' no hace nada....

for letra in strval:
    pass                # si elimino el comando 'pass' se genera un error

# Encuentra si la letra 'a' aparece en la cadena 'benefactora'



# en este ejemplo, la variable letra recorre cada carácter
# en la cadena y se detiene cuando se encuentra el carácter "a".

# De otro modo, encontrar una condición en un bucle puede requerir
# que se salte un conjunto de comandos y efectivamente se avance
# más rápido a la siguiente iteración.
# La función continue puede ser usada para esta aplicación.

for letra in strval:
    if letra != 'a':
        continue
        print('La letra "a" ha sido encontrada')
print()
# Finalmente, la función pass dentro de un bucle es una función
# nula que no hace nada.
# A veces es útil cuando se coloca en un programa donde se
# pretende continuar con código  que aun no ha sido escrito.


aval = 4
for i in range(9):
    print('i = ', i)
    if i >= aval:                 # si el valor de i es mayor que 4 se para el bucle
        print('stopping here ...')
        break
print('Program terminating')
print()
aval = 4
for i in range(9):
    if i == aval:
        continue # si el valor de i es igual a 4 se continua el bucle sin imprimir i = 4
    print('i=', i)
print()
aval = 4
for i in range(9):
    if i == aval:
        pass        # si el valor de i es igual a 4 pass no hace nada
        print('What does the pass instruction do?')
    print('i=', i)



print('ASCII-art example')




#x_val = int(input('Enter an integer less than 5: ')) #variable entera entrada por teclado
x_val = 6
if x_val < 5:                 # si x_val es mayor a 5 se ejecuta                                                  # la parte indentada
    print('Hello, Mr. User')
    new_x_val = x_val*10
    print('This is your new_x_val: ', new_x_val)
print('Hello, I am James')  # si no se cumple la condición no ejecuta la parte indentada

if x_val < 5:                 # si x_val es mayor a 5 se ejecuta                                                  # la parte indentada
    print('Hello, Mr. User')
    new_x_val = x_val*10
    print('This is your new_x_val: ', new_x_val)

else:
    new_x_val = x_val*20
    print('This is your new_x_val: ', new_x_val)


if x_val < 5:                 # si x_val es mayor a 5 se ejecuta                                                  # la parte indentada
    print('Hello, Mr. User')
    new_x_val = x_val*10
    print('This is your new_x_val: ', new_x_val)
elif x_val>= 5 and x_val<=15:
    new_x_val = x_val * 30
    print('This is your new_x_val: ', new_x_val)


else:
    new_x_val = x_val*100
    print('This is your new_x_val: ', new_x_val)


x_val = int(input('Please enter the number 10: '))

while (x_val != 10):                    # mientras el valor de x_val sea
                                        # diferente de 10
    print('Your input value is not equal to 10')
    print('Please try again: ')
    x_val = int(input('Enter the number 10: '))     # si entramos un valor diferente de
                                                    # 10 se repite el proceso
print('Thank you')
print('You entered a value of 10')
# imprimir los números del 1 al 100 usando diferentes métodos:
# uso de 'while' :
is_on = True
i=0
while is_on:
    i +=1
    print(f'i = {i}')
    if i == 100:
        is_on = False

# Uso de 'for' y 'range':
for i in range(101):
    print(f'i = {i}')

# si quiero imprimir todos los elementos de una cadena:

strval = 'forever'
for letra in strval:
    print(letra)

e_count = 0
for letter in strval:
    if letter == 'e':
        e_count = e_count + 1
print('The letter e occurred ', e_count, 'times')
print()
print('ASCII-art example')