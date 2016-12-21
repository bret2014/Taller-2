a=125

import turtle
##CUADRADO GRANDE 
t= turtle.Pen()
def micuadrado(a):
    for x in range (1,5):
        t.forward(a)
        t.left(90)
micuadrado(a)
##CUADRADO PEQUEÑO
t.goto(31.25,31.25)
b=50

def micuadrado(b):
    for x in range (1,5):
        t.forward(b)
        t.left(90)
micuadrado(b)
##CUADRADO ABAJO

c=150
t.goto(0,0)
def micuadrado(c):
    for x in range (1,5):
        t.forward(c)
        t.left(-90)
micuadrado(c)
##Cuadrado pequeño abajo
t.goto(0,0)
t.goto(37.5,-37.5)
d=75

def micuadrado(d):
    for x in range (1,5):
        t.forward(d)
        t.left(-90)
micuadrado(d)


turtle.getscreen()._root.mainloop()
