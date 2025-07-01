class Tiempo:
    '''Atributos : horas,minutos segundos'''
    def __init__(self,horas=0,minutos=0,segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def time_to_seconds(self):
        seconds = self.segundos + self.minutos*60 + self.horas*3600
        return seconds


    def add_time(self, t2):
        if isinstance(t2,Tiempo):
            seconds = self.time_to_seconds() + t2.time_to_seconds()
            t = sec_to_time(seconds)
        else:
            seconds = self.time_to_seconds() + t2
            t = sec_to_time(seconds)
        return t
    def is_after(self,other):
        return self.time_to_seconds() > other.time_to_seconds()
#El "operator overloading" en Python se refiere a la capacidad de definir
# cómo funcionarán los operadores incorporados (como +, -, *, /, ==, <, >, etc.)
# en tus propias clases personalizadas.
    def __add__(self, other):
        if isinstance(other,Tiempo):
            seconds = self.time_to_seconds() + other.time_to_seconds()
            return sec_to_time(seconds)
        else:
            seconds = self.time_to_seconds() + other
            return sec_to_time(seconds)

    #If other is a Time object, __add__ invokes add_time. Otherwise. it assumes
    # that the parameter is a number and invokes increment. This operation
    # is called a type-based dispatch because it dispatches the computation
    # to different methods based on the type of the arguments.

    def __radd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        return self.time_to_seconds() < other.time_to_seconds()

def sec_to_time(seconds):
    t = Tiempo(0,0,0)
    (minutos,t.segundos) = divmod(seconds,60)
    (t.horas,t.minutos)= divmod(minutos,60)
    return t

t1 = sec_to_time(3694)
t= Tiempo(2,30,30)
t2=t.add_time(t1)
t3=t.add_time(3600)
print(t1,t,t2,t3)
print(t3.is_after(t))
print(t+t1)
print(t + 3600)
print(3600+t)
print(t<t1)

print(vars(t1))    # imprime atributos de t1   {'horas': 1, 'minutos': 1, 'segundos': 34}
print(hasattr('horas'))
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    return d
#This function also works for lists, tuples, and even dictionaries,
# as long as the elements of s are hashable, so they can be used as keys in d

t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
print(histogram(t))

#Functions that work with several types are called polymorphic.
total = sum([t1,t2,t3])
print(total)