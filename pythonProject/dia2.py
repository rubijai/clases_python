# Operandos y operadores con variables numericas ( +, -, *, /, **) :
print( f'3 + 4 = {3 +4}')
print( f'3 - 4 = {3 -4}')
print( f'3 * 4 = {3 *4}')
print( f'3 / 4 = {3 / 4}')
print( f'3 ** 4 = {3 ** 4}')

print('3 + 4 =',3+4)
print( f'2 * 2 = {2 * 2}')
print( f'2 ** 3 = {2 ** 3}')
print( f'2 ** -3 = {2 ** -3}')

print( f'16 ** (1/2) = {16 ** (1/2)}')
print( f'8 ** (1/3) = {8 ** (1/3)}')
print( f'8 ** (2/3) = {8 ** (2/3)}')
res = round(8 ** (2/3),1)             # round (built-in function) redondea la
                                       # resultado res a 10 decimales
print(res)
res1 = 8 ** (2/3)
print(res == res1)
# Mientras que los operadores aritmeticos ( +, -, *, /) son útiles
# para realizar operaciones con números la programación requiere su
# uso con variables:

a = 3
print(f'a = {a} {type(a)} ')
b = 4
print(f'b = {b} {type(b)} ')

c = a * b
print(a, '*', b, ' = ', c)
print(f' {a} * {b}  = {c}  type(c) --> {type(c)}')

c = a / b
print(a, '/', b, ' = ', c)
print(f'{a} / {b}  = {c}  type(c) --> {type(c)}')  #python convierte el resultado a tipo float
c = a ** b
print(a, ' to the power ', b, ' = ', c)
print(type(c))
print('Fíjese bien en el tipo de variable.')


a = 2
b = 5
c = a ** b
print(a, ' to the power ', b, ' = ', c, type(c))
print('el tipo de c es entera o flotante?')

# Otros dos operadores son: % y //.
# % da el residuo de la division (a/b)
# (por ejemplo, a%b).
# // da por resultado un entero despues de tomar el 'piso' del cociente (a/b)
#el piso es el numero entero mas pequeño que es menor o igual a a/b.

x = 19          #19/7  --> 19 = 7 * 2 (divisor) + 5 (residuo)
y = 7
z1 = x % y
print('el residuo de  ', x, '/', y, ' = ', z1)
z2 = x // y
print('la division entera de ', x, ' y ', y, ' = ', z2)
x = -33
y = 8             # -33 = 8 *(-5) + 7
z1 = x % y
print(f'el residuo de  {x} / {y}  = {z1}')
z2 = x // y
print(f'la division entera de {x} % {y}  = {z2}')  #-33/8 = -4.25 y el piso es -5(entero)  < -4.25
print('tiene que tener claro este concepto.')


# Jerarquia de operadores y uso de parentesis:

# Jerarquía: () , ** , * / // %, + -
# relacionales (== != > < >= <=) ,
# bool( not , and , or)
# Las operaciones se realizan de izquierda a derecha teniendo
# en cuenta jerarquía de operadores (1.Aritméticos 2.Relacionales
# y 3.Boolean)
'''
1==2!=3>4>5>=6<=7
El operador != y los operadores de comparación como >, >=, <, <= 
se evalúan secuencialmente, y la cadena de comparaciones en Python 
funciona de manera que cada comparación se evalúa de manera que toda 
la expresión se evalúe como un todo. Sin embargo, dado que 
la primera comparación 1 == 2 ya es falsa, toda la cadena de 
comparaciones se evalúa como falsa, porque en una cadena de 
comparaciones, si alguna es falsa, toda la expresión se considera falsa.

'''

print(f'8 ** 1 / 3 = {8 ** 1 / 3}') # el operador ** es el que tiene mayor
                                    # jerarquía y se ejecuta primero

print(8 ** (1 / 3))                 # el operador () es el que tiene mayor
                                    # jerarquía y se ejecuta primero

a = 3
b = 4
c = 1
d = 5
e = 3
f = a + b - c * d + e / d
g = a + b - c * (d + e) / d
h = a + (b - c) * d + e / d
i = (a + b - c) * d + e / d
print('Antes de correr el programa, haga las operacioes sin el uso del computador. ')
print(f'f = {f}, g = {g}, h = {h}, i = {i}')


v = 2
w = 3
x = 4
y = 19
z = 23
d = v ** v // x % x + y % w * z // x
a = v ** v // x % x
b = y % w * z // x
c = a + b
print(d, a, b, c)
print()

e = v ** (v // x) % x + y % (w * z) // x
f = v ** (v // x) % x
g = y % (w * z) // x
h = f + g
print(e, f, g, h)
print()

# Operadores logicos y relacionales:
# relacionales (== != > < >= <=)
# #logicos ( not , and , or)•

# not x: complemento lógico : si x es True, not x es False.
# If x es False, not x es True

# x and z: solo es True si x es True y z es True. De otra forma, es False.

# x or z: Solo es False si x es False y z es False. De otra forma, es True.

# == Equals
# != Not Equals
# > Greater Than
# < Less Than
# <= Less Than or Equal To
# >= Greater Than or Equal To

a = True             # a es una variable booleana, pero puede tomar
                     # los valores 1(True) y 0(False)

print(a)
print(type(a))

b = False
print(b)
print(type(b))

a = 2
b = 3
print(a == b)  # Sea muy cuidadoso :Nunca confunda
               # el operador == (operador relacional)
               # con el operador = (operador aritmético).
print('Estos son ejercicios con operadores  relacionales')
print(a != b)
print(a >= b)
print(a >= a)
print(a <= a)
print(a > b)
print(a < b)

print()

a = 2
b = 5
a = b
print(a, type(a))
a = 2
b = 5
print(a == b)  #el resultado es False, ya que a no es igual a b.
print('Cuidado no confundir el operador = con el operador == (relacional)')
print()

a = 3
b = 9
c = 5
d = (a < b) and (a < c)

print(f'3<9 and 3<5  --> {3<9 and 3<5}')
e = (a < b) and (b < c)
print(e)
print(not a < b)
f = (b < c) or (c < a)
print(f)
g = (b < c) or (c >= a)
print(g)
h = b > c or c >= a
print(f'g = {g} h = {h}')

a = 3
b = 9
c = 5
d = (a < b) and (a < c)     #jerarquia 1.Aritméticos 2.Relacionales y 3.Boolean
print(f'd = {d}')           # el resultado es True, ya que (a < b) es True
                            # y (a < c) es True   y   el resultado es True

e = a < b and a < c              #jerarquia 1.Aritméticos 2.Relacionales y 3.Boolean
print(e)
print(f'e = {e}')               # el resultado es True
f = b < c and b < a or a < c    # jerarquia relacionales, logico and , logico or
print(f'b < c and b < a or a < c = {f}')               # el resultado es False, ya que (b < c) es False
                                # y (b < a) es True o (a < c) es True.f)
                                # el resultado es True

g = b < c and (b < a or a < c)
print(f'g = {g}')               # el resultado es False, ya que (b < c) es False
                                # y (b < a) es True o (a < c) es True,
                                # el resultado es True

h = not b < c and not b < a
print(f'h = {h}')               # el resultado es True, ya que (not b < c) es True
                                # y (not b < a) es True y el resultado es True


i = not (b < c or b < a)
print(f'i = {i}')               # el resultado es True, ya que (not b < c) es True
                                # o (not b < a) es True y el resultado es True

print(True == True != False)    #True se ejecuta de izquierda a derecha
print('a'*3+'/*'*5+2*'abc'+'+')


print('Haga muchos ejercicios con operadores lógicos y relacionales')



