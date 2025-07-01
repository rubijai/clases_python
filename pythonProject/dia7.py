'''
 "Manejo de Archivos"

 "Hay tres pasos principales para hacer referencia a un archivo:"

 "1. Abrir el archivo: Esto le permite al sistema operativo conocer
 el nombre y la ubicación del archivo al que se hace referencia,
 así como se va a utilizar el archivo (como lectura o escritura)."

 "2. Realizar operaciones en los datos del archivo (como leer, escribir
 o agregar): Ahora que el sistema operativo ha abierto el archivo,
 está listo para ser utilizado para el propósito especificado en el paso 1."

 "3. Cerrar el archivo: Después de completar el conjunto deseado de
 operaciones, se debe informar al sistema operativo que ya no es
 necesario el acceso al archivo."

'''
#Crear archivo de texto examp que lo podemos almacenar en Clase_7
fhandle = open('examp.txt', 'w')      # 'w' --> write
fhandle.write('This is a write example. ')
fhandle.write('Text will be sequentially written until a newline control character occurs. \n')
fhandle.write('Then a new line will begin with \n')
fhandle.write('and another new line, etc \n')
fhandle.write('Yo soy Jaime Ramírez Arbeláez\n')
fhandle.close()

# Leer el archivo examp
f2 = open('examp.txt', 'r')         # 'r' --> read
print(f2.read())           # el  metodo 'read' lee el archivo. Al ejecutar
                           # este método no se deja espacios entre líneas.

f2.close()

print('MMMMM')
print()

# Se lee el archivo línea por línea y se deja un espacio entre líneas
f2 = open('examp.txt', 'r')
for line in f2:  # itera sobre las líneas del archivo, las imprime
                 # y deja espacio entre líneas.
    print(line)
f2.close()


# Ahora crearemos un archivo de texto que contiene números:
f3 = open('source.txt', 'w')   # es un archivo de texto, los números son 'str'
f3.write(' 5 \n ')
f3.write('1.4 \n ')
f3.write('0 \n ')
f3.write('1.6 \n ')
f3.write('-4 \n')
f3.close()

# Se lee el archivo. Por defecto se toma 'r'
f3 = open("source.txt")
for line in f3:
    print(line)
f3.close()


f3 = open("source.txt")
print(f3.read())
f3.close()

print('MMMMM')
print()
f3 = open("source.txt")
print(f'f3.readline() {f3.readline()}')  # print(readline())
                                         # imprime una sola línea            5
print(f'f3.readlines() {f3.readlines()}') # print(readlines()) imprime
                                          # todas las líneas en una sola lista
                                          # ['1.4 \n','0 \n ','1.6 \n ','-4 \n ']
f3.close()
print('MMMMM')
print()



mySource = open("source.txt")       # elige 'r' por defecto
print(mySource.read())
# prisnant(text)
mySource.close()

print('MMMMM')
mySource = open("source.txt")
for line in mySource:
    print(line)
mySource.close()

mySource = open("source.txt")
text = mySource.read()
print(text)
mySource.close()

# los archivos de texto los podemos ver en pantalla

print('VVVVVVVVVVVV')
# 'script' que suma los números del archivo 'source.txt':

mySource = open("source.txt ")
s = 0
for line in mySource:
    print(line)
    line = line.rstrip()
    print(line)
    numbers = line.split()
    print(f'numbers = {numbers}')
    for x in numbers:
        print(float(x))
        s += float(x)
mySource.close()
print("The sum of all values is", s)

h = open("source.txt ")
lx = h.readlines()
print(lx)
ly = []
for x in lx:
    y = (float(x.strip()))
    ly.append(y)
h.close()
print(f'sumas={sum(ly)}')

# suma de los números de los números del archivo 'source2.txt':

f5 = open('source2.txt', 'w')
f5.write(' 1 8 9.2 -5 \n ')
f5.write('0 12 -23 -9 1 \n ')
f5.write('1.6 2.3 -9.1 \n ')
f5.write('-10 -91 76 23 7 \n ')
f5.write('1.4 9 8 ')    # Si uso \n produce un error en la suma
                        # puesto que agrega una línea vacía
f5.close

f5 = open("source2.txt ")
# print(f5.read()) #cambia el formato
s = 0
for line in f5:
    print(line)
    line = line.rstrip()
    numbers = line.split()
    # print(numbers)
    for x in numbers:
        s += float(x)
f5.close()
print("The sum of all values is", s)

f5 = open("source2.txt ")

st = 0
print(f'Hola')
for line in f5:
    print(f'line = {line}')
    sl = 0
    lx = line.strip().split(' ')
    print(f'lx = {lx}')
    for x in lx:
        print(f'x,type(x)= {x} {type(x)}')
        y = float(x)
        print(f'y,type(y)= {y} {type(y)}')
        sl += y
    print(f'sl = {sl}')
    st += sl
print(f'st={st}')

n = 2 #int(input('Entre num ent positivo '))
if n > 0:
    fname = 'sum' #input('Entre el nombre del archivo: ')
    print(fname)
    output = open(fname + '.txt', 'w')
    for i in range(1, n + 1):
        output.write(str(i * i) + '\n')
    output.close()
    print('Done! Look for the file', fname + '.txt')
else:
    print('Se espera num ent positivo')
    open(sum.txt)

#fx = open('JRAM.txt')
fx = open('source2.txt')
print(fx.readlines())
fx.close

n = 2  #int(input('Entre num ent positivo '))
if n > 0:
    fname = 'JRA'  #input('Entre el nombre del archivo: ')
    output = open(fname + '.txt', 'w')
    for i in range(1, n + 1):
        output.write(str(i * i) + ' ' + str(i ** 3) + '\n')
    output.close()
    print('Done! Look for the file', fname + '.txt')
else:
    print('Se espera num ent positivo')
    open(sum.txt)

j1 = open('jra.txt','r')
lx = j1.readlines()
for x in lx:
    s=0
    for z in (x.strip()).split(' '):
        print(z)
        w = float(z)
        s += w
    print(s)
#print(j1.read())
j1.close()

f=open('JRAlectex.txt','w')
f.write('1,8,9.2,-5 \n')
f.write('1.4,9,8,13 \n')
f.write('0,12,-23,-9,1 \n')
f.write('1.6,2.3,-9.1,-5 \n')
f.write('-42,-91,7,23,17 \n')
f.close()

f2=open('JRAlectex.txt')
print(f2.readlines())
f2.close()

j2 = open('JRAlectex.txt')
y = j2.readlines()
print(y)
st =0
for x in y:
    z = x.strip()
    el1 = z.split(',')
    sl = 0

    for item in el1:
        sl += float(item)
    print(f'sl = {sl}')
    st += sl
    print(round(st,2))
j2.close()

f3=open('JRAlectex.txt','a')
f3.write('70.6\n')
f3.close()

f4=open('JRAlectex.txt')
print(f4.readlines())
f4.close()

print('VVVVVVVVVVVVVVV')
f5=open('JRAlectex.txt')
for line in f5:
    print(f5.readlines())
    print('xxxxxxxx')
f5.close()

f6 = open('JRAlectex.txt')
s=0
for line in f6:
    line=line.rstrip()
    numbers=line.split(',')
    print(numbers)
    for n in numbers:
        s+=float(n)
f6.close()
print('s = ',s)

fname = 'temp1'
output = open(fname + ".txt",'w')
output.write(str(5)+' ')
output.write(str(7)+' ')
output.close()

output = open(fname + ".txt",'w')
output.write(str(7)+' ')
output.close()

output = open(fname + ".txt",'r')
print(output.readlines())     #temp1 ['5 7 '] lee una linea de un archivo
                              # y retorna una cadena
output.close()


filename = 'test1'
f = open(filename + '.txt','w')
f.write('hello'+' ')
f.write('world'+' ')
f.close()

output = open('test1.txt','r')
print(output.readlines())
output.close()


filename = 'test2'
f = open(filename + '.txt','w')
f.write('hello'+' ')
f.close()

f = open(filename + '.txt','a')
f.write('world'+' ')
f.close()

output = open('test2.txt','r')
print(output.readlines())
output.close()

n = 5
fname = 'data'
output = open(fname + ".txt",'w')
output.write(str(n)+' ')
output.close()
print("Done! Look for the file", fname+'.txt')

n = 5
fname = 'data1'
output1 = open(fname + ".txt",'w')
for i in range(1,n+1):
    output1.write(str(3*i+1)+' ')
output1.close()





n = 5
fname = 'data2'
output2 = open(fname + ".txt",'w')
for i in range(1,n+1):
    output2.write(str(3*i+1)+' '+'\n')
output2.close()


a1=open('data2.txt')
print(a1.read())
a1.close()

f = open('data.txt')
sval = 0
for line in f:
    sval += float(line)
f.close()
print(sval)






list_n = [34, 23, 124, 2345, 4]
#  n_list = [new_item for item in list_n if test]
n_list = [n * n for n in list_n if n < 100]
print(f'n_list = {n_list}')

n1_list = [n for n in list_n if n % 2 == 0]
print(n1_list)

#with open('file1.txt', 'r') as f2:
'''
Esta construcción es una forma abreviada de abrir un archivo, 
realizar operaciones sobre él y cerrarlo automáticamente al 
finalizar el bloque de código. Es una forma de gestión de 
contexto (context manager) que simplifica el manejo de 
archivos y evita errores comunes como olvidar cerrar el archivo.
'''
with open('data.txt', 'r') as f2:
    n2 = f2.readlines()
    print(n2)
n2_l = [int(n) for n in n2]
print(n2_l)

#with open('file2.txt', 'r') as f1:
with open('data2.txt', 'r') as f1:
    n1 = f1.readlines()
    print(n1)
n1_l = [int(n) for n in n1 if int(n) in n2_l]
print(n1_l)

# new_dict = {new_key:new_value for item in list}   dictionary comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}



with open('sum.txt') as j3:
    numbers = j3.readlines()
    print(f'numbers = {numbers}')
    n_numbers = [float(n) for n in numbers]
    print(n_numbers)
    print(sum(n_numbers))

with open('source2.txt') as s1:

    numbers = s1.readlines()
    print(f'numbers = {numbers}')
    st = 0
    for i in range(len(numbers)):
        lista = (numbers[i].strip().split(' '))
        print(lista)
        n_lista = [float(n) for n in lista]
        sl = sum(n_lista)
        st += sl
        print(st)

with open('source2.txt') as s2:
    l = (s2.readlines())
    suma = 0
    for x in l:
        y = (x.strip()).split(' ')
        z = [float(item) for item in y]
        suma += sum(z)
    print(f'suma = {suma}')

    f = open('JRA.txt', 'w')
    f.write('1 2 3 4 \n')
    f.write('2 5 6 7 \n')
    f.write('3 8 9  \n')
    f.write('4 10 \n')
    f.write('5 \n')
    f.close()

    f2 = open('JRA.txt')
    print(f2.read())
    f2.close()
    print('jjjjjjjj')

    f3 = open('JRA.txt', 'a')
    f3.write('6 \n')
    f3.close()

    f4 = open('JRA.txt')
    print(f4.read())
    f4.close()

    print('jjjjjjjjjjjj')
    f5 = open('JRA.txt')
    for line in f5:
        print(f5.readlines())
    f5.close()

    f6 = open('JRA.txt')
    s = 0
    for line in f6:
        line = line.rstrip()
        numbers = line.split(' ')
        for n in numbers:
            s += float(n)
    f6.close()
    print('s = ', s)

    f = open('data.txt', 'w')
    f.write('1 \n')
    f.write('2 \n')
    f.write('3 \n')
    f.write('4 \n')
    f.write('5 \n')
    f.close()

    f = open('data.txt')
    sval = 0
    for line in f:
        sval += float(line)
    f.close()
    print(sval)

    f = open('JRA.txt')
    numbers = f.readline()
    numbers = numbers.rstrip('\n')
    print(numbers)
    numbers = f.readline()
    numbers = numbers.rstrip('\n')
    print(numbers)
    f.close()

    import matplotlib.pyplot as plt

    x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    f = open('data.txt', 'w')
    for val in x:
        f.write(str(val) + '\n')
    f.close()

    f = open('data.txt')
    w = []
    z = []
    for val in f:
        t = float(val)
        w.append(t)
        z.append(2 * t)
    f.close()
    plt.plot(w, z)
    plt.savefig('plot.png')

    txt = "     banana     "
    x = txt
    print("of all fruits", x, "is my favorite")
    x = txt.rstrip()  # The rstrip() method removes any trailing characters (characters at the end a string),
    # space is the default trailing character to remove.
    print(x)
    print("of all fruits", x, "is my favorite")

    txt = "banana,,,,,ssqqqww....."
    print(txt)
    x = txt.rstrip(",.qsw")
    print(x)






mySource = open("data.txt",'w')
mySource.write('0 1 2 3 4 \n')
mySource.write('1 2 3 4 0  \n')
mySource.write('2 3 4 0 1 \n')
mySource.write('3 4 0 1 2 \n')
mySource.write('4 0 1 2 3 \n')
mySource.close()
f2=open('data.txt')
print(f2.read)
f2.close()