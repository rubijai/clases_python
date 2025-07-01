# Captura y Manejo de Errores
# Al escribir software, pueden ocurrir errores.
# A medida que adquirimos experiencia, aprenderemos a anticipar qué
# tipos de errores pueden ocurrir durante la ejecución del programa.
# Ejemplo:

# Vemos que aparecen tres llamadas en color rojo, pero el programa no
# se detiene por estar usando excepsiones.

import math

try:
    print(math.sqrt(-4))
except ValueError:
    print('El argumento de entrada debe ser no negativo')

a = 2
b = 3
print(a / b)
print()
# Si b=0 el programa colapsa y el programador debe evitar el colapso.
#  ZeroDivisionError
# Los comandos "try" y "except" son la puerta de entrada para manejar errores.
# " try" permite intentar ejecutar el código,
# y "except" identifica el tipo de error a manejar.
# Python contiene muchas excepciones integradas que se pueden capturar
# usando el comando "except".
try:
    print(variable)
except:
    print("Variable is not defined")
print()
# Como la variable no está definida en ninguna parte del código, ocurrirá
# una excepción y, por lo tanto,
# el bloque except se ejecutará y mostrará el mensaje.

try:
    x = 7 / 4 / 'y'
    print(x)
except ValueError:  # obtendrás este error si hay un problema con el
    # contenido del objeto al que intentaste asignar el valor;
    #  'y' es una cadena de texto.
    print("Non-numeric data found")
    print()
except NameError:  # obtendrás este error si el programa encuentra un
                   # nombre que no reconoce
    print("Variable x is not defined")
    print()
except:
    print("Some error occured")
print()
# También puedes usar la palabra clave else para definir el código que
# debe ejecutarse si no se generan errores.

try:
    print('Hello World')
except ValueError:
    print("Non-numeric data found")
except NameError:
    print("Variable x is not defined")
except:
    print("Some error occured")
else:
    print("Nothing went wrong")
print()

try:
    print(4 / 3 / 'b')
except NameError:
    print("Variable is not defined")
except:
    print("Seeems like something else went wrong")
print()

try:
    variable1 = "Python Programming"
    print(variable1)
except:
    print("An exception occurred")
else:
    print("Else executes: Try block executed correctly")
print()

# También puedes usar la palabra clave finally que se ejecutará, haya
# o no un error.

try:
    print(variable)
except:
    print("An exception occurred")
finally:
    print("Always execute this block")
print()

filename = 'temp10.dat'
try:
    f = open(filename)
    data = f.readfile()
    print('File read complete')
except:
    f = open(filename, 'w')
    print('File', filename, 'was created')
f.close()

try:
    print(z)
except ValueError:
    print('ValueError occurred')
except NameError:
    print('NameError occurred')
except:
    print('Some error occured')
else:
    print('No error occurred')

try:
    print(variable1)
except:
    print("An exception occurred")
finally:
    print("Always execute this block")

eng2fr = {1: 'un', 2: 'deux', 3: 'trois', 4: 'quatre'}
numval = int(input('Input a number from 1 to 4, I will tell you your '
                   'number in French: '))

try:
    print(f'The number {numval} in French is {eng2fr[numval]}.')
except KeyError:
    print(f'{numval} is not in my dictionary')

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That number was invalid")
print()

try:
    my_value = 3.14 / 0
except ArithmeticError:  # ArithmeticError se ejecuta puesto que incluye
    # ZeroDivisionError
       print("We had a general math error")
except ZeroDivisionError:
    print("We had a divide-by-zero error")
# Tuvimos un error matemático general
print()
try:
    my_dict = {"hello": "world"}
    print(my_dict["foo"])
except KeyError:
    print("Oh no! That key doesn't exist")

    # A veces es útil capturar un error, realizar una acción y luego propagar
    # el error en lugar de ocultarlo.
    # Esto es útil cuando, por ejemplo, algo sale mal en el fondo de tu código
    # y necesitas realizar una acción especial, pero también dejar que el
    # código en otro nivel sepa que algo está mal y el programa no puede
    # continuar. Vamos a dividir un número entre otro, decrementando hasta
    # llegar a cero. Captura ese error e inmediatamente genera un RuntimeError:

'''while True:
    for divisor in range(5, -1, -1):
        try:
            quotient = 10 / divisor
            print(f"10 / {divisor} = {quotient}")
        except ZeroDivisionError:
            print("Oops! We tried to divide by zero!")
        raise RuntimeError'''

eng2fr = {1: 'un', 2: 'deux', 3: 'trois', 4:'quatre'}
numval = int(input('Input a number from 1 to 4, I will tell you your number in French: '))

try:
    print(f'The number {numval} in French is {eng2fr[numval]}.')
except KeyError:
    print(f'{numval} is not in my dictionary')

import math
def get_sqrt(n):
    try:
        return math.sqrt(n)
    except ValueError:
        print('Input argument must be nonnegative')
        return -1


print(get_sqrt(2))
print(get_sqrt(-4))
print(get_sqrt(0))


def get_log(n):
    try:
        return math.log(n)
    except ValueError:
        print('Input argument must be nonnegative')
        return float('Inf')

    except TypeError:
        print('Input argument must be a number')
        return float('Nan')

print(get_log(2))
print(get_log(-4))
print(get_log('Hello'))


def get_div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        if a == 0:
            print('Warning: attempted 0/0')
            return float('NaN')
        if a<0 :
            print('Warning: attempted division by zero')
            return float('-Inf')
        if a > 0:
            print('Warning: attempted division by zero')
            return float('+Inf')
print(get_div(3,4))
print(get_div(0,0))
print(get_div(17,-11))
print(get_div(5,0))
print(get_div(-5,0))


def list_calc(alist):
    try:
        alist[8]=alist[7]+alist[5]
    except IndexError:
        print('Index error in input list')
        return None
    else:
        alist.append(-99)
        return alist


a=[10,20,30,40,50]
print(list_calc(a))
a=[10,20,30,40,50,60,70,80,90]
print(list_calc(a))
a=[10,20,30,40,50,60,70,80]
print(list_calc(a))


def get_value(wdict,key):
    try:
        wdict[key]+=32
    except KeyError:
        print('Key Error: will update dictionary with', key,':',None)
        wdict[key] = None
    finally:
        return wdict


d={'A':65, 'B':66, 'C':67, 'D':68}
key='N'
get_value(d,key)
print(d[key])

d={'A':65, 'B':66, 'C':67, 'D':68}
key='C'
get_value(d,key)
print(d[key])

d={'A':65, 'B':66, 'C':67, 'D':68}
key=65
get_value(d,key)
print(d[key])



def list_div(alist):
  try:
    alist[5]=alist[6]/alist[7]
  except IndexError:
    print('Index error in input list')
    return None
  except ZeroDivisionError:
    print('Warning: divide by zero')
    return None
  else:
      return alist


a=[10,20,30,40,50]
print(list_div(a))
a=[10,20,0,40,50]
print(list_div(a))
a=[10,20,30,40,50,60,70,0,90]
print(list_div(a))
a=[10,20,30,40,50,60,70,80]
print(list_div(a))

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That number was invalid")

try:
    my_value = 3.14 / 0
except ArithmeticError:
    print("We had a general math error")
except ZeroDivisionError:
    print("We had a divide-by-zero error")
'''    
class MyException(Exception):
    def __init__(self, message):
        new_message = f"!!!ERROR!!! {message}"
        super().__init__(new_message)

f = open('xcxc.dat', 'w')
#f.readfile()
#f.write('Hola')
raise MyException("Something went wrong!")


class MyException(Exception):
    pass
raise MyException()

class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got an incorrect value of {value}"
        super().__init__(message)


my_value = 9999
if my_value > 100:
    raise IncorrectValueError(my_value)'''

f = open('my_file.dat', 'w')
f.write('Jra')
f.close()

try:
    f = open('my_file.dat')
    f.readfile()  # AttributeError readfile no es un atributo del objeto
    print('Loaded data')
except:
    print('Data not loaded')

filename = 'temp.dat'
try:
    f = open(filename)
    data = f.readfile()
    print('File read complete')
except:
    f = open(filename, 'w')
    print('File', filename, 'was created')
f.close()

try:
    print(z)
except ValueError:
    print('ValueError occurred')
except NameError:
    print('NameError occurred')
except:
    print('Some error occured')
else:
    print('No error occurred')

try:
    z = 2.1 / 0
except ArithmeticError:
    print('Error: general arithmetic error')
except ZeroDivisionError:
    print('Error: division by zero error')

eng2fr = {1: 'un', 2: 'deux', 3: 'trois', 4: 'quatre'}
numval = int(input('Input a number from 1 to 4, I will tell you your number in French: '))

try:
    print(f'The number {numval} in French is {eng2fr[numval]}.')
except KeyError:
    print(f'{numval} is not in my dictionary')

import math


def get_sqrt(n):
    try:
        x = math.sqrt(n)
        return x
    except ValueError:
        x = -1
        print('Input argument must be nonnegative')
        return x


n = float(input('Enter number'))
print(get_sqrt(n))


def get_log(n):
    try:
        x = math.log(n)
        return x
    except ValueError:
        print('Input argument must be nonnegative')
        return float('Inf')
    except TypeError:
        print('Input argument must be a number')
        return float('Nan')


print(get_log(n))


def get_div(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        if a == 0:
            print('Warning: attempted 0/0')
            return float('NaN')
        elif a < 0:
            print('Warning: attempted division by zero')
            return float('-Inf')
        elif a > 0:
            print('Warning: attempted division by zero')
            return float('+Inf')


a = float(input('a= '))
b = float(input('b= '))
print(get_div(a, b))


def list_calc(alist):
    try:
        alist[8] = alist[7] + alist[5]
    except IndexError:

        print('Index error in input list')
        return None
    else:
        alist.append(-99)
        return alist


alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_calc(alist))


def get_value(wdict, key):
    try:
        wdict[key] += 32
    except KeyError:
        print('Key Error: will update dictionary with', key, ':', None)
        wdict[key] = None
    finally:
        return wdict


d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
key = 'N'
get_value(d, key)
print(d[key])

d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
key = 'C'
get_value(d, key)
print(d[key])

d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
key = 65
get_value(d, key)
print(d[key])


def optest():
    try:
        x = float(input('Input a number:'))
    except ValueError:
        print('Error: input must be a number')
        x = 0
    else:
        x = 2 * x
    finally:
        return x


print(optest())


def list_div(alist):
    try:
        alist[5] = alist[6] / alist[7]
    except IndexError:
        print('Index error in input list')
        return None
    except ZeroDivisionError:
        print('Warning: divide by zero')
        return None
    else:
        return alist


a = [10, 20, 30, 40, 50]
print(list_div(a))

a = [10, 20, 0, 40, 50]
print(list_div(a))

a = [10, 20, 30, 40, 50, 60, 70, 0, 90]
print(list_div(a))

a = [10, 20, 30, 40, 50, 60, 70, 80]
print(list_div(a))

# f = open('my_file.dat', 'w')  # FileNotFoundError file.dat no existe
# data = f.readfile()

print('Data loaded')


class GitHubApiException(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

    super().__init__(message)

    try:
        file = open('my_file.dat')
        data = file.readfile()
        print('Data Loaded')
    except:
        file = open('my_file.dat', 'w')
        print('File created')
    try:
        file = open('my_file.dat')
        data = file.readfile()
        print('Data Loaded')
    except FileNotFoundError:
        file = open('my_file.dat', 'w')
        print('File created')
    file.close()

    try:
        file = open('my_file.dat')
        data = file.readfile()
        print('Data Loaded')
    except FileNotFoundError:
        print('This file doesn\'t exist')


def list_calc(alist):
    try:
        alist[8] = alist[7] + alist[5]
        print(list_calc(a))
    except IndexError:
        print('Index error in input list')
    return None


alist = [10, 20, 30, 40, 50, 60, 70, 80, 90]
alist[8] = alist[7] + alist[5]
print(alist)

try:
    print(x)
except:
    print("An error occurred")

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That number was invalid")

try:
    my_value = 3.14 / 0
except ArithmeticError:
    print("We had a general math error")
except ZeroDivisionError:
    print("We had a divide-by-zero error")
'''    
class MyException(Exception):
    def __init__(self, message):
        new_message = f"!!!ERROR!!! {message}"
        super().__init__(new_message)

f = open('xcxc.dat', 'w')
#f.readfile()
#f.write('Hola')
raise MyException("Something went wrong!")


class MyException(Exception):
    pass
raise MyException()

class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got an incorrect value of {value}"
        super().__init__(message)


my_value = 9999
if my_value > 100:
    raise IncorrectValueError(my_value)'''

f = open('my_file.dat', 'w')
f.write('Jra')
f.close()

try:
    f = open('my_file.dat')
    f.readfile()  # AttributeError readfile no es un atributo del objeto
    print('Loaded data')
except:
    print('Data not loaded')

filename = 'temp.dat'
try:
    f = open(filename)
    data = f.readfile()
    print('File read complete')
except:
    f = open(filename, 'w')
    print('File', filename, 'was created')
f.close()

try:
    print(z)
except ValueError:
    print('ValueError occurred')
except NameError:
    print('NameError occurred')
except:
    print('Some error occured')
else:
    print('No error occurred')

try:
    z = 2.1 / 0
except ArithmeticError:
    print('Error: general arithmetic error')
except ZeroDivisionError:
    print('Error: division by zero error')

eng2fr = {1: 'un', 2: 'deux', 3: 'trois', 4: 'quatre'}
numval = int(input('Input a number from 1 to 4, I will tell you your number in French: '))

try:
    print(f'The number {numval} in French is {eng2fr[numval]}.')
except KeyError:
    print(f'{numval} is not in my dictionary')

import math


def get_sqrt(n):
    try:
        x = math.sqrt(n)
        return x
    except ValueError:
        x = -1
        print('Input argument must be nonnegative')
        return x


n = float(input('Enter number'))
print(get_sqrt(n))


def get_log(n):
    try:
        x = math.log(n)
        return x
    except ValueError:
        print('Input argument must be nonnegative')
        return float('Inf')
    except TypeError:
        print('Input argument must be a number')
        return float('Nan')


print(get_log(n))


def get_div(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        if a == 0:
            print('Warning: attempted 0/0')
            return float('NaN')
        elif a < 0:
            print('Warning: attempted division by zero')
            return float('-Inf')
        elif a > 0:
            print('Warning: attempted division by zero')
            return float('+Inf')


a = float(input('a= '))
b = float(input('b= '))
print(get_div(a, b))


def list_calc(alist):
    try:
        alist[8] = alist[7] + alist[5]
    except IndexError:

        print('Index error in input list')
        return None
    else:
        alist.append(-99)
        return alist


alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_calc(alist))


def get_value(wdict, key):
    try:
        wdict[key] += 32
    except KeyError:
        print('Key Error: will update dictionary with', key, ':', None)
        wdict[key] = None
    finally:
        return wdict


d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
key = 'N'
get_value(d, key)
print(d[key])

d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
key = 'C'
get_value(d, key)
print(d[key])

d = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
key = 65
get_value(d, key)
print(d[key])


def optest():
    try:
        x = float(input('Input a number:'))
    except ValueError:
        print('Error: input must be a number')
        x = 0
    else:
        x = 2 * x
    finally:
        return x


print(optest())


def list_div(alist):
    try:
        alist[5] = alist[6] / alist[7]
    except IndexError:
        print('Index error in input list')
        return None
    except ZeroDivisionError:
        print('Warning: divide by zero')
        return None
    else:
        return alist


a = [10, 20, 30, 40, 50]
print(list_div(a))

a = [10, 20, 0, 40, 50]
print(list_div(a))

a = [10, 20, 30, 40, 50, 60, 70, 0, 90]
print(list_div(a))

a = [10, 20, 30, 40, 50, 60, 70, 80]
print(list_div(a))

# f = open('my_file.dat', 'w')  # FileNotFoundError file.dat no existe
# data = f.readfile()

print('Data loaded')


class GitHubApiException(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached. Please wait a minute and try again."
        else:
            message = f"HTTP Status Code was: {status_code}."

    super().__init__(message)

    try:
        file = open('my_file.dat')
        data = file.readfile()
        print('Data Loaded')
    except:
        file = open('my_file.dat', 'w')
        print('File created')
    try:
        file = open('my_file.dat')
        data = file.readfile()
        print('Data Loaded')
    except FileNotFoundError:
        file = open('my_file.dat', 'w')
        print('File created')
    file.close()

    try:
        file = open('my_file.dat')
        data = file.readfile()
        print('Data Loaded')
    except FileNotFoundError:
        print('This file doesn\'t exist')


def list_calc(alist):
    try:
        alist[8] = alist[7] + alist[5]
        print(list_calc(a))
    except IndexError:
        print('Index error in input list')
    return None


alist = [10, 20, 30, 40, 50, 60, 70, 80, 90]
alist[8] = alist[7] + alist[5]
print(alist)

try:
    print(x)
except:
    print("An error occurred")




