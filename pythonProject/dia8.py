'''Las expresiones regulares en Python están disponibles a través
del módulo `re`:
import re

Usando regex, especificas las reglas para el conjunto de cadenas
posibles que deseas buscar.
Típicamente, primero definimos nuestro patrón que queremos buscar
y lo compilamos con `re.compile()`.
Por defecto, nuestro patrón distingue entre mayúsculas y minúsculas.
Nota: Se recomienda utilizar cadenas sin procesar (raw strings) para
la búsqueda:

En Python, las raw strings (cadenas sin procesar) son cadenas que tratan
las barras invertidas (\) como caracteres literales en lugar de interpretarlas
como caracteres de escape. Normalmente, en una cadena de Python, los caracteres
como \n (nueva línea) o \t (tabulación) se interpretan de manera especial,
pero en una raw string, esos caracteres se toman literalmente.

Para definir una raw string, se coloca una letra r antes de las comillas de
la cadena, como en r"texto".
'''

## Se recomienda utilizar cadenas sin procesar (raw strings)

a = 'Hello'
b = '\tHello'
c = r'\tHello'  # es una "raw string"
n = 'Jaime\nRamirez'
m = r'Jaime\nRamirez'
print(a)  # Hello
print(b)  # Hello
print(c)  # \tHello
print(n)  # Jaime
# Ramirez
print(m)  # Jaime\nRamirez

texto = r"Hola\nMundo"  # devuelve Hola\nMundo
print(texto)
texto1 = "Hola\nMundo"  # devuelve: Hola
#           Mundo
print(texto1)

'''Realización de búsquedas con objetos compilados  
Una vez que tenemos nuestro patrón, podemos buscar este patrón 
en el texto o cadena que deseamos consultar.  
- **match()**: Determina si la expresión regular coincide al principio 
               de la cadena.
- **search()**: Escanea una cadena, buscando cualquier ubicación donde 
                esta expresión regular coincida.
- **findall()**: Encuentra todas las subcadenas donde la expresión regular 
                 coincide y las devuelve como una lista.
- **finditer()**: Encuentra todas las subcadenas donde la expresión 
                regular coincide y las devuelve como un iterador.

En Python, un **iterador** es un objeto que permite recorrer una colección
 de elementos (como listas, tuplas, diccionarios o conjuntos) uno a uno. 
 Los iteradores son esenciales en la programación porque permiten procesar 
 secuencias de datos sin necesidad de cargarlas completamente en la memoria,
 lo que los hace eficientes.

### Características clave de un iterador:

1. **Protocolo de Iterador**: Para que un objeto sea un iterador, debe 
implementar dos métodos especiales:
   - `__iter__()`: Este método debe devolver el propio objeto iterador.
   - `__next__()`: Devuelve el siguiente elemento de la secuencia. Si no 
   quedan más elementos, lanza una excepción `StopIteration`.

2. **Función `iter()`**: Convierte un objeto iterable (como una lista o 
     un rango) en un iterador.

3. **Función `next()`**: Se utiliza para obtener el siguiente elemento de 
     un iterador.

'''
### Ejemplo de un iterador en Python:

# Crear una lista
mi_lista = [1, 2, 3, 4]

# Convertir la lista en un iterador
mi_iterador = iter(mi_lista)

# Usar el iterador para obtener los elementos uno a uno
print(next(mi_iterador))  # Imprime 1
print(next(mi_iterador))  # Imprime 2
print(next(mi_iterador))  # Imprime 3
print(next(mi_iterador))  # Imprime 4
# La siguiente llamada a next() lanzará StopIteration

'''
### Diferencia entre iterable e iterador:
- Un **iterable** es cualquier objeto sobre el que puedes iterar 
  (por ejemplo, listas, tuplas, cadenas).
- Un **iterador** es un objeto que representa una secuencia y puede 
  ser recorrido con el método `next()`.

### Uso en bucles:
El uso más común de los iteradores es en bucles `for`. Internamente, 
el bucle `for` llama automáticamente a `iter()` y `next()` para recorrer 
un iterable.

'''
for numero in mi_lista:
    print(numero)

'''
Este bucle usa un iterador en el fondo para recorrer los elementos de 
`mi_lista` sin que lo veas explícitamente.

Los iteradores son fundamentales para manejar grandes conjuntos de datos 
y trabajar con flujos de información, ya que permiten realizar operaciones 
sobre ellos sin necesidad de cargar todos los datos en memoria al mismo tiempo.

### Referencias:
- [Python Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
- [Real Python - Iterators](https://realpython.com/python-itertools/)



### Métodos de modificación. 
Cubriremos estos métodos más adelante:  
- **split()**: Devuelve una lista donde la cadena se ha dividido 
               en cada coincidencia.
- **sub()**: Reemplaza una o varias coincidencias con una cadena.

'''
# Estos son ejemplos de uso de finditer, search, findall y match
# para que los corras y veas las diferencias:

# finditer()
import re

'''### Métodos en un objeto Match:  
- **group()**: Devuelve la cadena que coincidió con la expresión regular.  
- **start()**: Devuelve la posición de inicio de la coincidencia.  
- **end()**: Devuelve la posición final de la coincidencia.  
- **span()**: Devuelve una tupla que contiene las posiciones de inicio 
              y fin de la coincidencia.  '''

cadena = 'abc123ABC123abc'
# cadena = 'python-engineer.com'
pat = r'123'
# pat = 'abc'
# pat = 'ABC'
# pat = r'\.'
comp_pat = re.compile(pat)
print(f'patrón compilado : {comp_pat} type:{type(comp_pat)}')
matches = comp_pat.finditer(cadena)
for match in matches:
    st = match.start()
    g = match.group()
    sp = match.span()
    e = match.end()
    print(cadena)
    print(f"{'-' * st}{g}")
print()

text = "The quick brown fox jumps over the lazy dog. The dog sleeps now."
pattern = "dog"

# Encuentra todas las ocurrencias de "dog" usando finditer()
matches = re.finditer(pattern, text)

# Itera a través del  iterador y accede a la información buscada
for match in matches:
    start_index = match.start()
    end_index = match.end()
    matched_string = text[start_index:end_index]  # generación de subcadena
    print(f"Found '{matched_string}' at index ({start_index}, {end_index})")
# findall()
fa_list = comp_pat.findall(cadena)
print(f'findall en cadena : fa_list= {fa_list}')
print()

# match
if comp_pat.match(cadena):
    print(f'match en cadena : cadena = {cadena}')
else:
    print('no match')

print()

# search
if comp_pat.search(cadena):
    print(f'search en cadena : cadena = {cadena}')
'''
Nota: Los métodos también se pueden utilizar directamente en el 
módulo re. No hace mucha diferencia, pero algunas personas 
prefieren compilar previamente y vincular explícitamente el 
patrón a una variable reutilizable.
(Ver https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile)

Modificación de cadenas¶  
- **split()**: Divide la cadena en una lista, dividiéndola donde 
               la expresión regular coincida.  
- **sub()**: Encuentra todas las subcadenas donde la expresión 
             regular coincida y reemplázalas con una cadena diferente.

'''
print(comp_pat.split(cadena))
print(comp_pat.sub('XXX', cadena))

'''
Es muy importante tener presentes el uso de estos metacaracteres:

Metacharacters
Metacharacters are characters with a special meaning:
All meta characters: . ^ $ * + ? { } [ ] \ | ( )
Meta characters need need to be escaped (with ) if we actually 
want to search for the char.
•	. Any character (except newline character) "he..o"
•	^ Starts with "^hello"
•	\$ Ends with "world\$"
•	* Zero or more occurrences "aix*"
•	+ One or more occurrences "aix+"
•	{ } Exactly the specified number of occurrences "al{2}"
•	[] A set of characters "[a-m]"
•	\ Signals a special sequence (can also be used to escape 
      special characters) "\d"
•	| Either or "falls|stays"
•	( ) Capture and group




More Metacharacters / Special Sequences¶
A special sequence is a \ followed by one of the characters 
in the list below, and has a special meaning:
•	\d : Matches any decimal digit; this is equivalent to the class [0-9].
•	\D : Matches any non-digit character; this is equivalent to the 
         class [^0-9].
•	\s : Matches any whitespace character;
•	\S : Matches any non-whitespace character;
•	\w : Matches any alphanumeric (word) character; this is equivalent
         to the class [a-zA-Z0-9_].
•	\W : Matches any non-alphanumeric character; this is equivalent 
         to the class [^a-zA-Z0-9_].
•	\b Returns a match where the specified characters are at the beginning 
       or at the end of a word r"\bain" r"ain\b"
•	\B Returns a match where the specified characters are present, 
       but NOT at the beginning 
       (or at the end) of a word r"\Bain" r"ain\B"
•	\A Returns a match if the specified characters are at the beginning 
       of the string "\AThe"
•	\Z Returns a match if the specified characters are at the end of 
       the string "Spain\Z"
'''
print()
test_string = 'hello 123_ heyho hohey'
pat = r'\d'
pattern = re.compile(pat)
matches = pattern.finditer(test_string)
for match in matches:
    print(match)
    print(match.group(), match.span())

print()
pattern = re.compile(r'\s')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\w')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\bhey')  # Returns a match where the #specified
# characters are at the beginning  of a word
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

pattern = re.compile(r'hey\b')  # Returns a match where the specified
# characters are at the end  of a word
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\Ahello')  # Returns a match if the specified
# characters are at the beginning of the string
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'123_\Z')  # Returns a match if the specified characters
# are at the end of the string
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

''' 
Sets¶
A set is a set of characters inside a pair of square brackets [] with 
a special meaning. 
    Append multiple conditions back-to back, e.g. [aA-Z].
A ^ (caret) inside a set negates the expression.
A - (dash) in a set specifies a range if it is in between, otherwise 
     the dash itself.
Examples:
- [arn] Returns a match where one of the specified characters 
  (a, r, or n) are present
- [a-n] Returns a match for any lower case character, alphabetically 
  between a and n
- [^arn] Returns a match for any character EXCEPT a, r, and n
- [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) 
  are present
- [0-9] Returns a match for any digit between 0 and 9
- [0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
- [a-zA-Z] Returns a match for any character alphabetically between a 
   and z, lower case OR upper case'''

test_string = 'hello 123_'
pattern = re.compile(r'[a-z]')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''

print('all dates with a character in between')
pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

print('only dates with - or . in between')
pattern = re.compile(r'\d\d\d\d[-.]\d\d[-.]\d\d')  # no escape for the . here
# in the set
matches = pattern.finditer(dates)
for match in matches:
    print(match)

print()
print('only dates with - or . in between in May or June')
pattern = re.compile(r'\d\d\d\d[-.]0[56][-.]\d\d')
matches = pattern.finditer(dates)
for match in matches:
    print(match)

# a dash in a character set specifies a range if it is in between,
# otherwise the dash itself
print()
print('only dates with - or . in between in May, June, July')
pattern = re.compile(r'\d\d\d\d[-.]0[5-7][-.]\d\d')  # no escape for
# the . here in the set
matches = pattern.finditer(dates)
for match in matches:
    print(match)

# all dates with a character in between
# <re.Match object; span=(13, 23), match='2020.04.01'>


# only dates with - or . in between
# <re.Match object; span=(13, 23), match='2020.04.01'>


# only dates with - or . in between in May or June
# "<re.Match object; span=(36, 46), match='2020-05-23'>


# only dates with - or . in between in May, June, July
# <re.Match object; span=(36, 46), match='2020-05-23'>

'''Quantifier¶
•	* : 0 or more
•	+ : 1 or more
•	? : 0 or 1, used when a character can be optional
•	{4} : exact number
•	{4,6} : range numbers (min, max)'''
my_string = 'hello_123'
pattern = re.compile(r'\d*')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'\d+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()
my_string = 'hello_1_2-3'
pattern = re.compile(r'_?\d')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()
my_string = '2020-04-01'
pattern = re.compile(r'\d{4}')  # or if you need a range r'\d{3,5}'
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
# <re.Match object; span=(0, 0), match=''>

dates = '''
2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''
pattern = re.compile(r'\d{4}.\d{2}.\d{2}')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
print()

pattern = re.compile(r'\d+.\d+.\d+')
matches = pattern.finditer(dates)
for match in matches:
    print(match)
# <re.Match object; span=(1, 11), match='2020.04.01'>

# Conditions¶
# Use the | for either or condition.

my_string = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""
pattern = re.compile(r'Mr\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

print()
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
# <re.Match object; span=(1, 11), match='Mr Simpson'>

# Grouping¶
# ( ) is used to group substrings in the matches.
emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""
# pattern = re.compile('[a-zA-Z1-9-]+@[a-zA-Z-]+\.[a-zA-Z]+')
# pattern = re.compile('[a-zA-Z1-9-]+@[a-zA-Z-]+\.(com|de)')
pattern = re.compile('([a-zA-Z1-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

'''
    <re.Match object; span=(1, 25), match='pythonengineer@gmail.com'>
    pythonengineer@gmail.com
    pythonengineer
    gmail
    com
    <re.Match object; span=(26, 48), match='Python-engineer@gmx.de'>
    Python-engineer@gmx.de
    Python-engineer
    gmx
    de
    <re.Match object; span=(49, 81), match='python-engineer123@my-domain.org'>
    python-engineer123@my-domain.org
    python-engineer123
    my-domain
    org'''

my_string = 'abc123ABCDEF123abc'
pattern = re.compile(r'123')  # no escape for the . here in the set
matches = pattern.split(my_string)
print(matches)

my_string = "hello world, you are the best world"
pattern = re.compile(r'world')
subbed_string = pattern.sub(r'planet', my_string)
print(subbed_string)
# ['abc', 'ABCDEF', 'abc']
# hello planet, you are the best planet
urls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
# pattern = re.compile(r'https?://(www\.)?(\w|-)+\.\w+')
pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    # print(match)
    print(match.group())  # 0
    # print(match.group(1))
    # print(match.group(2))
    print(match.group(3))

# substitute using back references to replace url + domain name
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
'''http://python-engineer.com
    .com
    https://www.python-engineer.org
    .org
    http://www.pyeng.net
    .net

    python-engineer.com
    python-engineer.org
    pyeng.net 
Compilation Flags¶
•	ASCII, A : Makes several escapes like \w, \b, \s and \d match 
    only on ASCII characters with the respective property.
•	DOTALL, S : Make . match any character, including newlines.
•	IGNORECASE, I : Do case-insensitive matches.
•	LOCALE, L : Do a locale-aware match.
•	MULTILINE, M : Multi-line matching, affecting ^ and $.
•	VERBOSE, X (for ‘extended’) : Enable verbose REs, which 
    can be organized more cleanly and understandably.'''

my_string = "Hello World"
pattern = re.compile(r'world', re.IGNORECASE)  # No match without I flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)

my_string = '''
hello
cool
Hello
'''
# line starts with ...
pattern = re.compile(r'^[a-z]', re.MULTILINE)  # No match without M flag
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
''' <re.Match object; span=(6, 11), match='World'>
    <re.Match object; span=(1, 2), match='h'>
    <re.Match object; span=(7, 8), match='c'>'''

# The re module offers a set of functions that allows us to search
# a string for a match:
txt = "The rain in Spain"
# pattern = "^The.*Spain$"
pattern = "ai"
print(re.findall(pattern, txt))  # Returns a list containing all matches
print(re.split(pattern, txt))  # Returns a list where the string has
# been split at each match
print(re.split(pattern, txt, 1))
print(re.sub(pattern, 'AI', txt))  # Replaces one or many matches with
# a string

# pattern = "ai"                    # no match
pattern = ".*ai"
x = re.match(pattern, txt)
print(x.group())
print(x.start())
print(x.end())
print(x.span())

pattern = "ai"
x = re.search(pattern, txt)
print(x.group())
print(x.start())
print(x.end())
print(x.span())

pattern = " "
print(re.findall(pattern, txt))
print(re.split(pattern, txt))
for item in re.split(pattern, txt):
    print(item)
print(re.split(pattern, txt, 2))  # the first 2 spaces
print(re.sub(pattern, '', txt))

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(f'x = {x}')

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)  # []

txt = "The rain in Spain"
x = re.search("\s", txt)
print(f' x.group() = {x.group()}')
print(x.start())
print(x.end())
print(x.span())

print(f"The first white-space character is located in position: {x.start()} ")

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(f'x.string is: {x.string}')
print(f'x.group() is: {x.group()}')

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# a file named "geek", will be opened with the reading mode.
file = open("str_data.txt", 'r')

# This will print every line one by one in the file
for line in file:
    print(line)

# Python code to illustrate read() mode
file = open("str_data.txt", "r")
print(file.read())

# Python code to illustrate with()
with open("str_data.txt") as file:
    data = file.read()
print(data)

# Python code to illustrate read() mode character wise
file = open("str_data.txt", "r")
print(file.read(6))  # print the first 6 characters

# Python code to illustrate split() function
with open("str_data.txt", "r") as file:
    data = file.readlines()
    print(f'data is: {data}')
    for line in data:
        word = line.split()
        print(f'word is : {word}')

# Python code to illustrate with() along with write()
with open("file.txt", "w") as f:
    f.write("Hello World!!!")

import os


def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
        print(f"File {filename} created successfully.")

    except IOError:
        print(f"Error: could not create file  {filename}")


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print(f"Error: could not read file {filename}")


def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print(f"Text appended to file {filename} successfully.")
    except IOError:
        print("Error: could not append to file  {filename }")


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print(f"File {filename} renamed to {new_filename} successfully.")
    except IOError:
        print(f"Error: could not rename file {filename}")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File  {filename}  deleted successfully.")
    except IOError:
        print(f"Error: could not delete file {filename}")


print(rename_file('file.txt', 'n_file.txt'))

if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)

personList = ['Julia Smith', 'Francis Drake', 'Michael Mason',
              'Jennifer Johnson', 'John Williams', 'Susanne Walker',
              'Kermit the Frog', 'Dr. Melissa Franklin', 'Papa John',
              'Walter John Miller', 'Frank Michael Robertson', 'Richard Robertson',
              'Erik D. White', 'Vincent van Gogh', 'Dr. Dr. Matthew Malone',
              'Rebecca Clark']

pattern = "John"
pattern_compiled = re.compile(pattern)  # compile es una función en re
# como lo es sin en math

print(pattern_compiled, 'John')  # <re.Match object; span=(0, 4), match='John'>
# reduce la búsqueda

for person in personList:
    if re.match(pattern, person):  # busca el patrón dado('John') en todo
        # listado de personas que
        # empieza por dicho patrón
        print(f'person is: {person}')

for person in personList:
    if pattern_compiled.match(person):
        print(f'person is: {person}')

string = 'Hola Mundo'
prog = re.compile(pattern)
result = prog.match(string)

# es equivalente a

result = re.match(pattern, string)

compiledRE = re.compile(pattern)
for person in personList:
    if compiledRE.match(person):
        print(person)
for person in personList:
    match = compiledRE.match(person)
    if match:
        print(match.group())  # The match object provides the methods
        # group() for getting the matched part as a string,
        print(match.start())  # for getting the character index of the
        # starting position of the match,
        print(match.end())  # for getting the character index of
        # the end position of the match
        print(match.span())  # to get both start and end indices as a tuple.

print('.....')

# search(...) - In contrast to match(...), search(...) tries to find
# matching locations anywhere within the string not just matches
# starting at the beginning (devuelve todos los que encuentra).

# findall(...) - In contrast to match(...) and search(...), findall(...)
# will identify all substrings in the given string that match the
# regular expression and return these matches
# as a list (devuelve el primero que encuentra)

# finditer(...) - finditer(...) works like findall(...) but returns
# the matches found not as a list but as a so-called iterator
# object(it has attributes like group, start,end, span. These two methods
# are among the most rudimentary in the re module.
# The match() method would be more applicable if there is no need to
# perform a complete search of the whole string.
# If the desired pattern is found at the beginning, then an answer can
# be returned immediately.
# The string() method is more general and will search through a string
# until the pattern is found.
# Additionally, findall() is a useful method when more than one occurrence
# of a pattern is being searched for.


# with open('myfile.bin', 'rb') as f:
# contents = f.read()


pattern = 'John'  # ".*John" '.[abco]' '.*John\S' '.{11,11}[A-Z]' '.*li?a' ".u" "..\." ".+John"
# "(Dr.\s)?M.*\s" "(Dr.\s)*M.*\s" ".*(nn|ss)" ".*John$" "(^|.*\s)John(\s|$)"
# ".*John(?!son)" '^John' '.*\s[a-z]+'


compiledRE = re.compile(pattern)
for person in personList:
    if compiledRE.match(person):
        print(person)
        print('aaa')

pattern = 'John'
compiledRE = re.compile(pattern)
for person in personList:
    if compiledRE.search(person):
        print(person)

for person in personList:
    search = compiledRE.search(person)
    if search:
        print(search.group())  # The match object provides the methods
        # group() for getting the matched part as a string,
        print(search.start())  # for getting the character index of the starting
        # position of the match,
        print(search.end())  # for getting the character index of the end
        # position of the match
        print(search.span())
print('bbbb')

pattern = 'John'
compiledRE = re.compile(pattern)
for person in personList:
    if compiledRE.findall(person):
        print(person)
print('ccccc')

pattern = 'John'
compiledRE = re.compile(pattern)
for person in personList:
    if compiledRE.finditer(person):
        print(person)
print()
print('dddddd')

slist = ['asdf', 'asbdfgdfg', 'rewtwertwert', 'adbfgjh']
pattern = '..b'
compiledRE = re.compile(pattern)
for s in slist:
    if compiledRE.match(s):
        print(s)
print()
print('eeeee')

personList = ['1 one', '2 two', '3 three', '4 four', '5 five', 'six', 'seven', 'eight', 'nine', 'ten']
pattern = '\D.*i'
for person in personList:
    if re.match(pattern, person):
        print()
        print(person)

print('fffff')
personList = ['adfac', 'babba', 'cbaca', 'fbaceeef']
pattern = 'a.*b'
for person in personList:
    if re.search(pattern, person):
        print()
        print(person)
print('ggggg')


def re_pattern(text, pattern):
    print("  '{}'".format(text))
    print(re.finditer(pattern, text))
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        substr_match = text[s:e]
        dot_prefix = '.' * s
        print("  {}'{}'".format(dot_prefix, substr_match))
    print()
    return


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

'''
 \d	                stands for any decimal digit 0…9
\D	                stands for any character that is not a digit
\s	                stands for any whitespace character (whitespace
characters include the space, tab, and newline character)
\S	                stands for any no n -whitespace character
\w	                stands for any alphanumeric character (alphanumeric
characters are all Latin letters a-z and A-Z, Arabic digits 0…9,
and the underscore character)
\W	                stands for any no n -alphanumeric character'''

# ".*John" '.[abco]' '.*John\S' '.{11,11}[A-Z]' '.*li?a' ".u" "..\." ".+John"
# "(Dr.\s)?M.*\s" "(Dr.\s)*M.*\s" ".*(nn|ss)" ".*John$" "(^|.*\s)John(\s|$)"
# ".*John(?!son)" '^John' '.*\s[a-z]+'
print(personList)
pat = 'John'
comp_pat = re.compile(pat)
for name in personList:
    if comp_pat.match(name):
        print(name)

for name in personList:
    if comp_pat.search(name):
        print(name)

for name in personList:
    print(comp_pat.findall(name))

for name in personList:
    matches = comp_pat.finditer(name)
    for match in matches:
        st = match.start()
        g = match.group()
        sp = match.span()
        e = match.end()
        print(name)
        print(f"{'.' * st}{g}")
        print(f"{'.' * st}{g}")

cadena = 'jaime ramirez a'
x = cadena.upper()
import math as m

x = m.sin(m.pi / 2)
print(x)

texto = "Hola\nMundo"
print(texto)

texto = r"Hola\nMundo"
print(texto)

import re

# Usando raw string
patron = r"\d+"  # Coincide con uno o más dígitos
texto = "Tengo 123 manzanas"
resultado = re.findall(patron, texto)
print(resultado)  # ['123']

import re

texto = "Hola mundo"
patron = r"Hola"
resultado = re.match(patron, texto)

if resultado:
    print("Coincidencia encontrada:", resultado.group())
else:
    print("No hay coincidencia.")

texto = "El perro está en el jardín"
patron = r"perro"
resultado = re.search(patron, texto)

if resultado:
    print("Palabra encontrada en la posición:", resultado.start())
else:
    print("No se encontró la palabra.")

texto = "Tengo 3 gatos, 2 perros y 1 pájaro"
patron = r"\d+"  # Coincide con uno o más dígitos
resultado = re.findall(patron, texto)
print("Números encontrados:", resultado)

texto = "La temperatura es 23 grados y la humedad es 65%"
patron = r"\d+"
iterador = re.finditer(patron, texto)

for match in iterador:
    print(f"Número encontrado: {match.group()} en la posición {match.span()}")

texto = "manzana, naranja, plátano, pera"
patron = r",\s*"  # Divide por comas y espacios en blanco
resultado = re.split(patron, texto)
print("Frutas divididas:", resultado)

texto = "La temperatura es 23 grados y la humedad es 65%"
patron = r"\d+"  # Coincide con cualquier número
nuevo_texto = re.sub(patron, "XX", texto)
print("Texto modificado:", nuevo_texto)

texto = "Mi correo es ejemplo@correo.com"
patron = r"(\w+)@(\w+)\.(\w+)"  # Captura el nombre, dominio y extensión
resultado = re.search(patron, texto)

if resultado:
    print("Usuario:", resultado.group(1))
    print("Dominio:", resultado.group(2))
    print("Extensión:", resultado.group(3))

texto = "Hola Mundo"
patron = r"hola"
resultado = re.search(patron, texto, re.IGNORECASE)

if resultado:
    print("Coincidencia encontrada:", resultado.group())
else:
    print("No hay coincidencia.")

texto = "Primera línea\nSegunda línea"
patron = r".+"
resultado = re.search(patron, texto, re.DOTALL)

print("Coincidencia encontrada:", resultado.group())

texto = "Primera línea\nSegunda línea"
patron = r"^Segunda"
resultado = re.search(patron, texto, re.MULTILINE)

if resultado:
    print("Coincidencia encontrada:", resultado.group())
else:
    print("No hay coincidencia.")

import re

texto = "El número de teléfono es 123-456-7890"
patron = r"(\d{3})-(\d{3})-(\d{4})"
resultado = re.search(patron, texto)

if resultado:
    print("Número de teléfono completo:", resultado.group())
    print("Código de área:", resultado.group(1))
    print("Primer parte:", resultado.group(2))
    print("Segunda parte:", resultado.group(3))

