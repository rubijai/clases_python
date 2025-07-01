import math as m
from turtle import Turtle, Screen
class Punto:
    '''punto en el plano: coordenadas x,y'''
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def distancia(self,punto1):
        d = m.sqrt((self.x - punto1.x)**2 + (self.y - punto1.y)**2)
        return d

class Rectangulo:
    '''esquina, alto y ancho son sus atributos'''
    def __init__(self,esquina,h=20,b=40,):
        self.h = h
        self.b = b
        self.esquina = esquina

    def __str__(self):
        return f'b = {self.b}, h = {self.h}, esquina = {self.esquina}'

    def find_center(self):
        xc = self.esquina.x + self.b/2
        yc = self.esquina.y + self.h/2
        return (xc,yc)

    def grow_rect(self,dh,db):
        self.h += dh
        self.b += db
        return self

class Circulo:
    '''los atributos son centro y radio'''
    def __init__(self,centro,radio=10):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f' circulo con centro en {self.centro} y radio {self.radio}'

    def punto_dentro_circulo(self,p):
        print(p.distancia(self.centro))
        if p.distancia(self.centro) <= self.radio:
            return True

        return False

    def rect_circle_overlap(self,p1,p2,p3,p4):
        if ((p1.distancia(self.centro) <= self.radio) or  (p2.distancia(self.centro) <= self.radio)
            or (p3.distancia(self.centro) <= self.radio) or (p4.distancia(self.centro) <= self.radio)):
            return True
        return False


punto1 = Punto(10,20)
print(punto1)
punto2 = Punto(-30,40)
d = punto1.distancia(punto2)
print(d,type(d))
esquina = Punto(10,10)




rect1 = Rectangulo(esquina,300,40)
print(rect1)
print(rect1.esquina.x)
v1 = esquina
print(v1,esquina)
v2 = Punto(v1.x + rect1.b,v1.y)
print((v2))
v3 = Punto(v1.x,v1.y + rect1.h)
print(v3)
v4= Punto(v1.x + rect1.b,v1.y + rect1.h)
print(v4)


rect2 = Rectangulo(punto1, 10,20)
print(rect2)
print(rect2.find_center())
print(rect2.grow_rect(5,5))
print(rect2)
centro = Punto(15,10)
rueda = Circulo(centro,75)
print(rueda)
print(rueda.punto_dentro_circulo(punto1))
print(rueda.rect_circle_overlap(v1,v2,v3,v4))


tim = Turtle()
screen = Screen()
screen.setup(800,800)
tim.shape('turtle')
tim.color('green')
tim.penup()
tim.goto(-400,0)
tim.pendown()
tim.forward(800)
tim.penup()
tim.goto(0,-400)
tim.pendown()
tim.left(90)
tim.forward(800)
tim.penup()


tim.goto((rueda.centro.x + rueda.radio),rueda.centro.y)
tim.pendown()
tim.pensize(1)
tim.circle(75)
tim.penup()
tim.goto(v1.x,v1.y)
tim.pendown()
tim.forward(rect1.h)
tim.right(90)
tim.forward(rect1.b)
tim.right(90)
tim.forward(rect1.h)
tim.right(90)
tim.forward(rect1.b)

#tim.hideturtle()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


screen.exitonclick()





