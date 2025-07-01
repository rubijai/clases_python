'''

Clases y objetos
La base de la POO son los objetos.
Podéis imaginaros los objetos como un nuevo tipo de dato cuya definición viene dada en una estructura llamada clase.
Suelo hacer una metáfora y comparar las clases con moldes de galletas y los objetos con las galletas en sí mismas.
Si bien todas las galletas que se hacen con el mismo molde tienen la misma forma, cada una adquiere
atributos individuales después del horneado. Cosas como el color, la textura, el sabor... pueden
llegar a ser muy distintas.
En otras palabras, las galletas comparten un proceso de fabricación y unos atributos, pero son independientes
entre ellas y del propio molde y eso hace que cada una sea única.
Extrapolando el ejemplo, una clase es sólo un guión sobre como deben ser los objetos que se crearán con ella.

La función type()
Ya he comentado varias veces que en Python todo son clases y objetos, eso se puede comprobar fácilmente
pasando a la función type() cualquier variable o literal:
numero = 10
type(numero)
int
En el código anterior numero es una variable entera, pero si vamos más allá, en realidad es una instancia del
tipo int, una clase muy básica de dato para almacenar números enteros.
Como curiosidad, incluso las funciones en Python son instancias del tipo function:
def hola():
    pass

type(hola)
function
Con eso en mente veamos como crear nuestras propias clases.

Definición de clase

La sintaxis es muy sencilla:
'''


class Galleta:  # se acostumbra usar mayúsculas
    pass


'''
Esta es una definición muy simple de lo que es una galleta, ya que con el pass la dejo vacía. 
Luego añadiremos más información, por ahora veamos como crear galletas con este molde.

Instancias de clase

Para entender bien los objetos debemos tener claras dos cuestiones fundamentales:
¿Cuándo y dónde existen los objetos?
Puede parecer trivial, pero es importante tener claro que los objetos "existen" sólo durante 
la ejecución del programa y se almacenan en la memoria del sistema operativo.
Es decir, mientras las clases están ahí en el código haciendo su papel de instrucciones, los objetos 
no existen hasta que el programa se ejecuta y se crean en la memoria.

Este proceso de "crear" los objetos en la memoria se denomina instanciación y para realizarlo es tan 
fácil como llamar a la clase como si fuera una función:

'''
una_galleta = Galleta()
otra_galleta = Galleta()

'''
Demostrar que las galletas existen como "entes independientes" dentro de la memoria, es tan sencillo 
como imprimirlas por pantalla:
'''

print(una_galleta)
print(otra_galleta)
# <__main__.Galleta object at 0x000001433B4C2048>
# <__main__.Galleta object at 0x000001433B439FD0>
'''
Cada instancia tiene su propia referencia, demostrando que están en lugares distintos de la memoria. 
En cambio la clase no tiene una referencia porque es sólo un guión de instrucciones:

'''
print(Galleta)
# <class '__main__.Galleta'>

'''Es posible consultar la clase de un objeto con la función type(), pero también se puede consultar a 
través de su atributo especial class:'''

print(Galleta)
print(type(una_galleta))
print(una_galleta.__class__)
# <class '__main__.Galleta'>
# <class '__main__.Galleta'>
# <class '__main__.Galleta'>

'''
A su vez las clases tienen un atributo especial name que nos devuelve su nombre en forma de cadena sin adornos:
'''
print(Galleta.__name__)
print(type(una_galleta).__name__)
print(una_galleta.__class__.__name__)
# Galleta
# Galleta
# Galleta


'''
Atributos y métodos
Si hay algo que ilustre el potencial de la POO esa es la capacidad de definir variables y funciones 
dentro de las clases, aunque aquí se conocen como atributos y métodos respectivamente.

Atributos

A efectos prácticos los atributos no son muy distintos de las variables, la diferencia fundamental 
es que sólo existen dentro del objeto.

Atributos dinámicos
Dado que Python es muy flexible los atributos pueden manejarse de distintas formas, por ejemplo 
se pueden crear dinámicamente (al vuelo) en los objetos.
'''


class Galleta:
    pass


galleta = Galleta()
galleta.sabor = "salado"
galleta.color = "marrón"

print(f"El sabor de esta galleta es {galleta.sabor} "
      f"y el color {galleta.color}")

'''El sabor de esta galleta es Salado y el color Marrón
Atributos de clase
Aunque la flexibilidad de los atributos dinámicos puede llegar a ser muy útil, tener que 
definir los atributos de esa forma es tedioso. Es más práctico definir unos atributos básicos 
en la clase. De esa manera todas las galletas podrían tener unos atributos por defecto:
'''


class Galleta:
    chocolate = False


galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")
# La galleta no tiene chocolate
# Luego podemos cambiar su valor en cualquier momento:
galleta.chocolate = True

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")

'''
La galleta tiene chocolate
Por lo menos de esta forma nos aseguraremos de que el atributo chocolate existe en todas 
las galletas desde el principio. Además es posible consultar el valor por defecto que deben 
tener las galletas haciendo referencia al atributo en la definición de la clase:
'''
print(Galleta.chocolate)
# False

'''
Lo curioso es que si cambiamos ese atributo de clase (que no de objeto) a True, las siguientes 
galletas se crearán con chocolate, es decir, habremos modificado las instrucciones de creación de los objetos:
'''


class Galleta:
    chocolate = False


Galleta.chocolate = True

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")

'''La galleta tiene chocolate
Ya les gustaría a otros lenguajes ser tan flexibles. 😁😁😁

Métodos

Si por un lado tenemos las "variables" de las clases, por otro tenemos sus "funciones", que evidentemente 
nos permiten definir funcionalidades para llamarlas desde las instancias.
Definir un método es bastante simple, sólo tenemos que añadirlo en la clase y luego llamarlo desde 
el objeto con los paréntesis, como si de una función se tratase:
'''


class Galleta:
    chocolate = False

    def saludar(self):
        print("Hola, soy una galleta muy sabrosa")


galleta = Galleta()
# Galleta.saludar()

'''---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-27-74df06911b9b> in <module>()
    6 
    7 galleta = Galleta()
----> 8 galleta.saludar()

TypeError: saludar() takes 0 positional arguments but 1 was given
Sin embargo, al intentar ejecutar el código anterior desde una galleta veréis que no funciona. 
Nos indica que el método saludar() requiere 0 argumentos pero se está pasando uno.
¿Cómo puede ser? Si en ningún momento hemos enviado ninguna información a al galleta...
Lo que tenemos aquí, estimados alumnos, es la diferencia fundamental entre métodos de clase y métodos de instancia.
Probad a ejecutar el método llamando a la clase en lugar del objeto:
'''


class Galleta:
    chocolate = False

    def saludar(self):
        print("Hola, soy una galleta muy sabrosa")


# Galleta.saludar()
# Hola, soy una galleta muy sabrosa

''''¡Ahora sí ha funcionado! ¿Cómo es posible? Y más importante, ¿por qué al llamarlo desde el 
objeto dice que estamos enviando un argumento?
Primer argumento self
Los objetos tienen una característica muy importante: son conscientes de que existen. Y no, no es broma.
Cuando se ejecuta un método desde un objeto (que no desde una clase), se envía un primer argumento 
implícito que hace referencia al propio objeto. Si lo definimos en nuestro método podremos capturarlo y ver qué es:
'''


class Galleta:
    chocolate = False

    def saludar(soy_el_propio_objeto):
        print("Hola, soy una galleta muy sabrosa")
        print(soy_el_propio_objeto)


galleta = Galleta()
galleta.saludar()
# Hola, soy una galleta muy sabrosa
# <__main__.Galleta object at 0x0000028E65476748>


'''¿Curioso que haya funcionado verdad? Además ¿no os suena de algo ese resultado que muestra el parámetro 
que hemos definido? Se trata de la propia representación del objeto.'''


class Galleta:
    chocolate = False

    def saludar(soy_el_propio_objeto):
        print("Hola, soy una galleta muy sabrosa")
        print(soy_el_propio_objeto)


galleta = Galleta()
galleta.saludar()
print(galleta)
# Hola, soy una galleta muy sabrosa
# <__main__.Galleta object at 0x0000028E654769E8>
# <__main__.Galleta object at 0x0000028E654769E8>


'''Pues sí, podemos acceder al propio objeto desde el interior de sus métodos. Lo único que como 
este argumento hace referencia al objeto en sí mismo por convención se le llama self.
Poder acceder al propio objeto desde un método es muy útil, ya que nos permite acceder a sus atributos. 
Fijaros, el siguiente código no funcionaría como esperamos:
'''


class Galleta:
    chocolate = False

    def chocolatear(self):
        chocolate = True


galleta = Galleta()
galleta.chocolatear()
print(galleta.chocolate)


# False
# En cambio, si hacemos ver que self es el propio objeto...
class Galleta:
    chocolate = False

    def chocolatear(self):
        self.chocolate = True


galleta = Galleta()
galleta.chocolatear()
print(galleta.chocolate)
# True

'''
¿No es interesante? Da la sensación como os decía antes de que las instancias tienen que saber quienes 
son porque sino no pueden acceder sus atributos internos y por eso tienen que enviarse asimismas a los métodos.
Sea como sea con este ejemplo podemos entender que por defecto el valor de un atributo se busca en la clase, 
pero para modificarlo en la instancia es necesario hacer referencia al objeto.
Métodos especiales
Ahora que sabemos crear métodos y hemos aprendido para qué sirve el argumento self, es momento de introducir 
algunos métodos especiales de las clases.
Se llaman especiales porque la mayoría ya existen de forma oculta y sirven para tareas específicas.

Constructor
El constructor es un método que se llama automáticamente al crear un objeto, se define con el nombre init:

'''


class Galleta:

    def __init__(self):
        print(" Soy una galleta acabada de hornear!")


galleta = Galleta()
# Soy una galleta acabada de hornear!
nueva_galleta = Galleta()
# Soy una galleta acabada de hornear!
'''La finalidad del constructor es, como su nombre indica, construir los objetos. Por esa razón permite 
sobreescribir el método que crea los objetos, permitiéndonos enviar datos desde el principio para construirlo:'''


class Galleta:
    chocolate = False

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print(f"Se acaba de crear una galleta {self.color} y {self.sabor}.")


galleta_1 = Galleta("marrón", "amarga")
galleta_2 = Galleta("blanca", "dulce")

# Se acaba de crear una galleta marrón y amarga.
# Se acaba de crear una galleta blanca y dulce.

'''Como los métodos se comportan como funciones tienen sus mismas características, permitiéndonos definir 
valores nulos, valores por posición y nombre, argumentos indeterminadas, etc.

Destructor
Si existe un constructor también debe existir un destructor que se llame al eliminar el objeto para 
que encargue de las tareas de limpieza como vaciar la memoria. Ese es el papel del método especial del. 
Es muy raro sobreescribir este método porque se maneja automáticamente, pero es interesante saber que existe.
Todos los objetos se borran automáticamente de la memoria al finalizar el programa, aunque también podemos 
eliminarlos automáticamente pasándolos a la función del():'''


class Galleta:

    def __del__(self):
        print("La galleta se está borrando de la memoria")


galleta = Galleta()

del (galleta)
# La galleta se está borrando de la memoria

'''En este punto vale comentar algo respecto a los métodos especiales como éste, y es que pese a que tienen 
accesores en forma de función para facilitar su llamada, es totalmente posible ejecutarlos directamente 
como si fueran métodos normales:'''


class Galleta:

    def __del__(self):
        print("La galleta se está borrando de la memoria")


galleta = Galleta()

galleta.__del__()
# La galleta se está borrando de la memoria

'''Si tenéis memoria seguro que ahora mismo os estáis acordando de funciones como str() y len(), y es que 
en efecto, esas también son accesores de los métodos especiales str y len que tienen los objetos.
String
El método str es el que devuelve la representación de un objeto en forma de cadena. Un momento en que se llama 
automáticamente es cuando imprimirmos una variable por pantalla.
Por defecto los objetos imprimen su clase y una dirección de memoria, pero eso puede cambiarse 
sobreescribiendo el comportamiento:'''


class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color

    def __str__(self):
        return f"Soy una galleta {self.color} y {self.sabor}."


galleta = Galleta("dulce", "blanca")

print(galleta)
print(str(galleta))
print(galleta.__str__())
# Soy una galleta blanca y dulce.
# Soy una galleta blanca y dulce.
# Soy una galleta blanca y dulce.

'''Hay que tener en cuenta que este método debe devolver la cadena en lugar de mostrar algo por pantalla, 
ese es el funcionamiento que se espera de él.

Length
Finalmente otro método especial interesante es el que devuelve la longitud. Normalmente está ligado 
a colecciones, pero nada impide definirlo en una clase. Y sí, digo definirlo y no redefinirlo porque 
por defecto no existe en los objetos aunque sea el que se ejecuta al pasarlos a la función len().'''


class Cancion:

    def __init__(self, autor, titulo, duracion):  # en segundos
        self.duracion = duracion

    def __len__(self):
        return self.duracion


cancion = Cancion("Queen", "Don't Stop Me Now", 210)

print(len(cancion))
print(cancion.__len__())
# 210
# 210


'''Objetos dentro de objetos
Hasta ahora no lo hemos comentado, pero al ser las clases un nuevo tipo de dato resulta más que obvio 
que se pueden poner en colecciones e incluso utilizarlos dentro de otras clases. 
Os voy a dejar un pequeño código de ejemplo sobre un catálogo de películas para que lo estudiéis detenidamente:'''


class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return f'{self.titulo} ({self.lanzamiento})'


class Catalogo:
    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)


p = Pelicula("El Padrino", 175, 1972)
c = Catalogo([p])  # Añado una lista con una película desde el principio
c.mostrar()
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))  # Añadimos otra
c.mostrar()
# Se ha creado la película: El Padrino
# "El Padrino (1972)
# "Se ha creado la película: El Padrino: Parte 2
# El Padrino (1972)
# El Padrino: Parte 2 (1974)


'''Encapsulación
Finalmente para acabar la introducción vale la pena comentar esta "técnica". No es santo de mi devoción 
porque no le veo mucho sentido, pero si venís de otros lenguajes quizá os interesa conocerla.
La encapsulación consiste en denegar el acceso a los atributos y métodos internos de la clase desde 
el exterior. En Python no existe, pero se puede simular precediendo atributos y métodos 
con dos barras bajas __ como indicando que son "especiales".
En el caso de los atributos quedarían así:'''


class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."


e = Ejemplo()
# print(e.__atributo_privado)
'''
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-3-eed1a613919b> in <module>()
----> 1 print(e.__atributo_privado)

AttributeError: 'Ejemplo' object has no attribute '__atributo_privado'
Y en los métodos...'''


class Ejemplo:
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")


e = Ejemplo()
# e.__metodo_privado()
'''

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-81c514698440> in <module>()
----> 1 e.__metodo_privado()

AttributeError: 'Ejemplo' object has no attribute '__metodo_privado'
¿Qué sentido tiene esto en Python? Ninguno, porque se pierde toda la gracia de lo que en esencia es el 
lenguaje: flexibilidad y polimorfismo sin control (hablaremos de esto más adelante).
Sea como sea para acceder a esos datos se deberían crear métodos públicos que hagan de interfaz. 
En otros lenguajes les llamaríamos getters y setters y es lo que da lugar a las propiedades, que no 
son más que atributos protegidos con interfaces de acceso:'''


class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()


e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()
# Soy un atributo inalcanzable desde fuera.
# Soy un método inalcanzable desde fuera.


'''Ejercicios « Programación Orientada a Objetos
Teoría previa
En este ejercicio vas a trabajar el concepto de puntos, coordenadas y vectores sobre el plano cartesiano y 
cómo la programación Orientada a Objetos puede ser una excelente aliada para trabajar con ellos. No está pensado 
para que hagas ningún tipo de cálculo sino para que practiques la automatización de tareas.
Nota
Creo que es un ejemplo muy interesante, punto de partida en la programación de gráficos, pero si consideras que 
esto no lo tuyo puedes simplemente pasar de largo. Ahora bien, debes ser consciente de que te vas a perder uno de 
los ejercicios más interesantes del curso.
Voy a explicar brevemente los conceptos básicos por si alguien necesita un repaso.
El plano cartesiano
Representa un espacio bidimensional (en 2 dimensiones), formado por dos rectas perpendiculares, una horizontal 
y otra vertical que se cortan en un punto. La recta horizontal se denomina eje de las abscisas o eje X, 
mientras que la vertical recibe el nombre de eje de las ordenadas o simplemente eje Y. En cuanto al punto 
donde se cortan, se conoce como el punto de origen O.

Es importante remarcar que el plano se divide en 4 cuadrantes:

Puntos y coordenadas
El objetivo de todo esto es describir la posición de puntos sobre el plano en forma de coordenadas, 
que se forman asociando el valor del eje de las X (horizontal) con el valor del eje Y (vertical).
La representación de un punto es sencilla: P(X,Y) dónde X y la Y son la distancia horizontal (izquierda o derecha) 
y vertical (arriba o abajo) respectivamente, utilizando como referencia el punto de origen (0,0), 
justo en el centro del plano.

Vectores en el plano
Finalmente, un vector en el plano hace referencia a un segmento orientado, generado a partir de dos puntos distintos. 
A efectos prácticos no deja de ser una línea formada desde un punto inicial en dirección a otro punto 
final, por lo que se entiende que un vector tiene longitud y dirección/sentido.

En esta figura, podemos observar dos puntos A y B que podríamos definir de la siguiente forma:
•	A(x1, y1) => A(2, 3)
•	B(x2, y2) => B(5, 5)
Y el vector se representaría como la diferencia entre las coordendas del segundo punto respecto al primero
 (el segundo menos el primero):
•	AB = (x2-x1, y2-y1) => (5-2, 5-3) => (3,2) 
Lo que en definitiva no deja de ser: 3 a la derecha y 2 arriba.
Y con esto finalizamos este mini repaso.
Ejercicio
•	Crea una clase llamada Punto con sus dos coordenadas X e Y.
•	Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
•	Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
•	Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta 
    que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e 
    Y == 0 está sobre el origen.
•	Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
•	(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos 
y la muestre por pantalla. La fórmula es la siguiente:

Nota
La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla de la siguiente forma: 
import math
math.sqrt(9)
•	Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
•	Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos 
    puntos en el origen por defecto.
•	Añade al rectángulo un método llamado base que muestre la base.
•	Añade al rectángulo un método llamado altura que muestre la altura.
•	Añade al rectángulo un método llamado area que muestre el area.
Sugerencia
Puedes identificar fácilmente estos valores si intentas dibujar el cuadrado a partir de su diagonal. 
Si andas perdido, prueba de dibujarlo en un papel, ¡seguro que lo verás mucho más claro! Además recuerda 
que puedes utilizar la función abs() para saber el valor absolute de un número.
Experimentación
•	Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
•	Consulta a que cuadrante pertenecen el punto A, C y D.
•	Consulta los vectores AB y BA.
•	(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'. 
•	(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0). 
•	Crea un rectángulo utilizando los puntos A y B.
•	Consulta la base, altura y área del rectángulo.


Herencia
La herencia es la capacidad que tiene una clase de heredar los atributos y métodos de otra, algo que nos 
permite reutilizar código y hacer programar mucho más óptimos.
Para ver su utilidad, en esta lección vamos a desarrollar un ejemplo. Partiremos de una clase sin herencia 
con muchos atributos y la iremos descomponiendo en otras clases más simples que nos permitan trabajar 
mejor con sus datos.
Ejemplo sin herencia
Hace muchos años me vi en la necesidad de diseñar una estructura para una tienda 
que vendía tres tipos de 
productos: adornos, alimentos y libros.
Todos los productos de la tienda tenían una serie de atributos comunes, como la referencia, 
el nombre, el pvp... 
pero algunos eran específicos de cada tipo.
Si partimos de una clase que contenga todos los atributos, quedaría más o menos así:'''


class Producto:
    def __init__(self, referencia, tipo, nombre,
                 pvp, descripcion, productor=None,
                 distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor


adorno = Producto('000A', 'ADORNO', 'Vaso Adornado', 15,
                  'Vaso de porcelana con dibujos')

print(adorno)
print(adorno.tipo)
# <__main__.Producto object at 0x0000026233AD72E8>
# ADORNO

'''Obviamente esto es un despropósito, así que veamos como aproecharnos de la herencia para 
mejorar el planteamento. 
Superclases
Así pues la idea de la herencia es identificar una clase base (la superclase) con los 
atriutos comunes y luego 
crear las demás clases heredando de ella (las subclases) extendiendo sus campos específicos. 
En nuestro caso esa clase sería el Producto en sí mismo:'''


class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"


'''Subclases
Para heredar los atributos y métodos de una clase en otra sólo tenemos que pasarla entre paréntesis 
durante la definición:'''


class Adorno(Producto):
    pass


adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")
print(adorno)
'''REFERENCIA      2034
NOMBRE          Vaso adornado
PVP             15
DESCRIPCIÓN     Vaso de porcelana
Como se puede apreciar es posible utilizar el comportamiento de una superclase sin definir nada en la subclase.
Respecto a las demás subclases como se añaden algunos atributos, podríamos definirlas de esta forma:'''


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"PRODUCTOR\t\t {self.productor}\n" \
               f"DISTRIBUIDOR\t\t {self.distribuidor}\n"


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"


'''Ahora para utilizarlas simplemente tendríamos que establecer los atributos después 
de crear los objetos:'''

alimento = Alimento(2035, "Botella de Aceite de Oliva", 5, "250 ML")
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"
print(alimento)

libro = Libro(2036, "Cocina Mediterránea", 9, "Recetas sanas y buenas")
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
print(libro)
'''REFERENCIA      2035
NOMBRE          Botella de Aceite de Oliva
PVP             5
DESCRIPCIÓN     250 ML
PRODUCTOR       La Aceitera
DISTRIBUIDOR    Distribuciones SA

REFERENCIA      2036
NOMBRE          Cocina Mediterránea
PVP             9
DESCRIPCIÓN     Recetas sanas y buenas
ISBN            0-123456-78-9
AUTOR           Doña Juana
Luego en los ejercicios os mostraré como podemos sobreescribir el constructor de una forma eficiente 
para inicializar campos extra, por ahora veamos como trabajar con estos objetos de distintas clases 
de forma común.
Trabajando en conjunto
Gracias a la flexibilidad de Python podemos manejar objetos de distintas clases masivamente de una 
forma muy simple.
Vamos a empezar creando una lista con nuestros tres productos de subclases distintas:'''
productos = [adorno, alimento]
productos.append(libro)

print(productos)
##[<__main__.Adorno at 0x14c58660940>,
# <__main__.Alimento at 0x14c586608d0>,
# <__main__.Libro at 0x14c58660978>]
'''Ahora si queremos recorrer todos los productos de la lista podemos usar un bucle for:'''
for producto in productos:
    print(producto, "\n")
'''REFERENCIA      2034
NOMBRE          Vaso adornado
PVP             15
DESCRIPCIÓN     Vaso de porcelana

REFERENCIA      2035
NOMBRE          Botella de Aceite de Oliva
PVP             5
DESCRIPCIÓN     250 ML
PRODUCTOR       La Aceitera
DISTRIBUIDOR    Distribuciones SA

REFERENCIA      2036
NOMBRE          Cocina Mediterránea
PVP             9
DESCRIPCIÓN     Recetas sanas y buenas
ISBN            0-123456-78-9
AUTOR           Doña Juana
También podemos acceder a los atributos, siempre que sean compartidos entre todos los objetos:'''
for producto in productos:
    print(producto.referencia, producto.nombre)
'''2034 Vaso adornado
2035 Botella de Aceite de Oliva Extra
2036 Cocina Mediterránea
Si un objeto no tiene el atributo al que queremos acceder nos dará error:'''
for producto in productos:
    pass
    # print(producto.autor)
'''
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-8-36e9baf5c1cc> in <module>()
    1 for producto in productos:
----> 2     print(producto.autor)

AttributeError: 'Adorno' object has no attribute 'autor'
Por suerte podemos hacer una comprobación con la función isinstance() para determinar si una instancia 
es de una determinado clase y así mostrar unos atributos u otros:'''

for producto in productos:
    if (isinstance(producto, Adorno)):
        print(producto.referencia, producto.nombre)
    elif (isinstance(producto, Alimento)):
        print(producto.referencia, producto.nombre, producto.productor)
    elif (isinstance(producto, Libro)):
        print(producto.referencia, producto.nombre, 'p.isbn')

'''
2034 Vaso adornado
2035 Botella de Aceite de Oliva La Aceitera
2036 Cocina Mediterránea 0-123456-78-9
Polimorfismo
El polimorfismo es una propiedad de la herencia por la que objetos de distintas subclases pueden 
responder a una misma acción.
La polimorfia es implícita en Python, ya que todas las clases son subclases de una superclase común llamada Object. 
Por ejemplo la siguiente función aplica una rebaja al precio de un producto:'''


def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp / 100 * rebaja)


'''Gracias al polimorfismo no tenemos que comprobar si un objeto tiene o no el atributo pvp, 
simplemente intentamos acceder y si existe premio:'''

print(alimento, "\n")
rebajar_producto(alimento, 10)
print(alimento)

'''
REFERENCIA      2035
NOMBRE          Botella de Aceite de Oliva
PVP             5
DESCRIPCIÓN     250 ML
PRODUCTOR       La Aceitera
DISTRIBUIDOR    Distribuciones SA

REFERENCIA      2035
NOMBRE          Botella de Aceite de Oliva
PVP             4.5
DESCRIPCIÓN     250 ML
PRODUCTOR       La Aceitera
DISTRIBUIDOR    Distribuciones SA
Por cierto, como podéis ver en el ejemplo, cuando modificamos un atributo de un objeto dentro de una 
función éste cambia en la instancia. Esto es por aquello que os comenté del paso por valor y referencia.
________________________________________
Última edición: 29 de Septiembre de 2018

Anterior Introducción 

Siguiente Copia de objetos 


Copia de objetos
De la misma forma que las colecciones, los objetos se pasan a las funciones por referencia. Si modificamos 
sus valores dentro, éstos se verán reflejados fuera.
Esto también afecta a la hora de hacer copias, creándose en su lugar un acceso al objeto en lugar de uno 
nuevo con sus valores:'''


class Test:
    pass


test1 = Test()
test2 = test1

test1.algo = "Prueba"

print(test2 == test1)  # ¿Son el mismo objeto?

try:
    print(test2.algo)
except Exception as e:
    print(e)
# True
'''
Prueba
Para realizar una copia a partir de sus valores podemos utilizar la función copy del módulo con el mismo nombre:'''

from copy import copy


class Test:
    pass


test1 = Test()
test2 = copy(test1)

test1.algo = "Prueba"

print(test2 == test1)  # ¿Son el mismo objeto?

try:
    print(test2.algo)
except Exception as e:
    print(e)
# False
# 'Test' object has no attribute 'algo'
'''
La función copy se puede utilizar también para copiar colecciones:'''

from copy import copy

lista1 = [1, 2, 3]
lista2 = copy(lista1)
lista1 = None

print(lista1)
print(lista2)
# None
# [1, 2, 3]

'''
Herencia múltiple
Finalmente hablemos de la herencia múltiple: la capacidad de una subclase de heredar de múltiples superclases. 
Esto conlleva un problema, y es que si varias superclases tienen los mismos atributos o métodos, la subclase 
sólo podrá heredar de una de ellas.
En estos casos Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase:'''


class A:
    def __init__(self):
        print("Soy de clase A")

    def a(self):
        print("Este método lo heredo de A")


class B:
    def __init__(self):
        print("Soy de clase B")

    def b(self):
        print("Este método lo heredo de B")


class C(B, A):
    def c(self):
        print("Este método es de C")


c = C()
c.a()
c.b()
c.c()
# Soy de clase B
# Este método lo heredo de A
# Este método lo heredo de B
# Este método es de C


'''
Ejercicios « Herencia en la POO
Teoría previa
En este ejercicio vas a trabajar el concepto de herencia un poco más en profundidad, aprovechando para 
introducir un nuevo concepto muy importante que te facilitará la vida.
Hasta ahora sabemos que una clase heredada puede fácilmente extender algunas funcionalidades, simplemente 
añadiendo nuevos atributos y métodos, o sobreescribiendo los ya existentes. Como en el siguiente ejemplo:'''


class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada)


coche = Coche("azul", 150, 4, 1200)
print(coche)
# Color azul, 4 km/h, 150 ruedas, 1200 cc
'''
El inconveniente más evidente de ir sobreescribiendo es que tenemos que volver a escribir el código de la
 superclase y luego el específico de la subclase.
Para evitarnos escribir código innecesario, podemos utilizar un truco que consiste en llamar el método de la 
superclase y luego simplemente escribir el código de la clase:'''


class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)
print(c)
# Color azul, 4 ruedas, 150 km/h, 1200 cc
'''
Como tener que determinar constantemente la superclase puede ser fastidioso, Python nos permite utilizar 
un acceso directo mucho más cómodo llamado super().
Hacerlo de esta forma además nos permite llamar cómodamente los métodos o atributos de la superclase sin 
necesidad de especificar el self, pero ojo, sólo se aconseja utilizarlo cuando tenemos una única superclase:'''


class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)
print(c)
# Color azul, 4 km/h, 150 ruedas, 1200 cc
'''
Enunciado
Utilizando esta nueva técnica extiende la clase Vehiculo y realiza la siguiente implementación:

•	Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
•	Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
•	Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
Recordatorio
Puedes utilizar el atributo especial de clase name para recuperar el nombre de la clase de un objeto:
type(objeto).__name__



'''