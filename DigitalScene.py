import turtle
import random

t= turtle.Turtle()
bg = turtle.Screen()
bg.bgcolor("black")
bg.tracer(0,0)

def drawRectangle(width,height,x,y,color):
    t.penup()
    t.color(color)
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    for x in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def drawTriangle(size,x,y,color):
    t.penup()
    t.color(color)
    t.goto(x,y)
    t.setheading(60)
    t.pendown()
    t.forward(size)
    for x in range(2):
        t.right(120)
        t.forward(size)
    

def drawSnowyGrass():
    t.speed(30)
    t.penup()
    xPos = -400
    yPos = -300
    t.goto(xPos,yPos)
    for x in range(200):
        t.begin_fill()
        drawTriangle(4,xPos,yPos,"white")
        t.end_fill()
        xPos+=4
    t.begin_fill()
    drawRectangle(800,50,-400,-350,"white")
    t.end_fill()

def drawTree(x,y):
    t.begin_fill()
    drawRectangle(5,25,x,y,"burlywood4")
    t.end_fill()
    size = 35
    x_decrement = 15
    y_increment = 10
    for z in range (3):
        t.begin_fill()
        drawTriangle(size,x-x_decrement,y+y_increment,"dark green")
        t.end_fill()
        size -=10
        x_decrement-=5
        y_increment+=15

def drawParallelogram(size):
    colors = ["white"]
    t.color(random.choice(colors))
    t.forward(size)
    t.left(60)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(60)
    t.forward(size)

def drawSnowflake():
    angle=0;
    for x in range(0,6):
        t.penup()
        t.goto(random.randint(-400,400),random.randint(-350,350))
        t.setheading(angle)
        t.pendown()
        t.begin_fill()
        drawParallelogram(3)
        t.end_fill()
        angle+=360/6

def drawMoon():
    t.penup()
    t.goto(150,150)
    t.pendown()
    bg.colormode(255)
    t.color((255,255,0))
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()
    t.goto(130,153)
    t.pendown()
    t.color(0,0,0)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    

drawSnowyGrass()
for x in range(-300,300,30):
    drawTree(x,-300)

drawMoon()
    
for x in range(random.randint(100,300)):
    drawSnowflake()

bg.update()
