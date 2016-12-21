import turtle
from tkinter import *
t = turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
for x in range(1,9):
    t.forward(100)
    t.left(225)

t.reset()
for x in range(1,38):
    t.forward(100)
    t.left(175)

t.reset()
a=int(input("Ingrese numero de lados: "))
b = 180/a
c = 180- b
t = turtle.Pen()
t.reset()
if a % 2==0:
    print("No se puede graficar solo funciona para pares")
else:
    t.reset()
    for i in range(a):
        t.forward(100)
        t.right(c)


t.reset()
la=int(input("Ingrese el numero del lado: "))
def micuadrado(size):
    for x in range(1,5):
        t.forward(size)
        t.left(90)
micuadrado(la)



turtle.getscreen()._root.mainloop()

