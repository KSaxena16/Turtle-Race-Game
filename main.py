from turtle import *
from random import randint

speed(0)
penup()
goto(-140,140)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)


#adding racing turtles ....
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()


bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

pop = Turtle()
pop.color('yellow')
pop.shape('turtle')

pop.penup()
pop.goto(-160,40)
pop.pendown()

aku = Turtle()
aku.color('green')
aku.shape('turtle')

aku.penup()
aku.goto(-160,10)
aku.pendown()



for i in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    pop.forward(randint(1,5))
    aku.forward(randint(1,5))
    


