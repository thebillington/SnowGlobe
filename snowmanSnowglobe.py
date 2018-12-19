from snowglobe import *

def body():

    t.penup()
    t.goto(-100, -110)
    t.pendown()

    t.color("white")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def head():

    t.penup()
    t.goto(-100, -35)
    t.pendown()

    t.color("white")
    t.begin_fill()
    t.circle(25)
    t.end_fill()

def buttons():

    t.penup()
    t.goto(-100, -90)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    t.penup()
    t.goto(-100, -70)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    t.penup()
    t.goto(-100, -50)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()

def eyes():

    t.penup()
    t.goto(-110, -5)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(2)
    t.end_fill()

    t.penup()
    t.goto(-90, -5)
    t.pendown()

    t.color("black")
    t.begin_fill()
    t.circle(2)
    t.end_fill()

def nose():

    t.penup()
    t.goto(-100, -10)
    t.pendown()

    t.color("orange")

    t.begin_fill()

    t.right(30)
    t.forward(15)
    t.right(150)
    t.forward(15)

    t.end_fill()

    t.setheading(0)

def snowman():

    body()
    head()
    buttons()
    eyes()
    nose()
    
snowglobe = Snowglobe("Mr Rebecchi's Snowglobe", 15, snowman)
snowglobe.snowHeight = 200

while True:
    
    snowglobe.update()
