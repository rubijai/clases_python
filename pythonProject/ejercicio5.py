import math as m
from turtle import Turtle, Screen
class Punto:
    '''coordenadas x,y'''
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'

    def cuadrante(self):
        if self.x>0 and self.y>0:
            return f'cuadrante 1'
        if self.x<0 and self.y>0:
            return f'cuadrante 2'
        if self.x<0 and self.y<0:
            return f'cuadrante 3'
        if self.x>0 and self.y<0:
            return f'cuadrante 4'
        else:
            return f'el punto esta sobre uno de los ejes'

    def vector(self,p2):
        return f'({p2.x-self.x},{p2.y-self.y})'

    def distancia(self,p):
        return f'{m.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)}'

class Rectangulo:
    '''p1 y p2 son los dos extremos de la diagonal
    y el rect tiene los lados paralelos a los ejes'''
    def __init__(self,punto1,punto2):
        self.punto1 = punto1
        self.punto2 = punto2
    def __str__(self):
        return f'rectangulo con p1: ({self.punto1.x},{self.punto1.y}) y p2 : ({self.punto2.x},{self.punto2.y})'
    def base(self):
        base = (m.fabs( self.punto1.x - self.punto2.x))
        return base

    def altura(self):
        altura = (m.fabs( self.punto1.y - self.punto2.y))
        return altura

    def Area(self):
        Area = self.base() * self.altura()
        return Area

print()
p1 = Punto(3,4)
print(p1)

print(p1.cuadrante())
p2 = Punto(0,8)
print(p1.vector(p2))
print(f'dist = {p1.distancia(p2)}' )
rect = Rectangulo(p1,p2)
print(rect)
print(rect.base())
print(rect.altura())
print(rect.Area())









class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def obtener_otro_vertice(self):
        # Calcula las coordenadas del tercer vértice del rectángulo
        x3 = self.punto2.x - (self.punto2.y - self.punto1.y)
        y3 = self.punto2.y + (self.punto2.x - self.punto1.x)
        return Punto(x3, y3)

    def calcular_area(self):
        # Calcula el área del rectángulo
        base = abs(self.punto2.x - self.punto1.x)
        altura = abs(self.punto2.y - self.punto1.y)
        return base * altura

    def __str__(self):
        return f'Rectángulo: Vértice1{self.punto1}, Vértice2{self.punto2}, Vértice3{self.obtener_otro_vertice()}'



# Creamos dos puntos en el plano
punto1 = Punto(1, 3)
punto2 = Punto(5, 5)

# Creamos un rectángulo con los dos puntos extremos de una diagonal
rectangulo = Rectangulo(punto1, punto2)

# Mostramos información del rectángulo
print(rectangulo)
print("Área del rectángulo:", rectangulo.calcular_area())
