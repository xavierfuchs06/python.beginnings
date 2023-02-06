import turtle
t = turtle.Turtle()
s = turtle.getscreen()
w = 0
x = 400
z = 800
t.speed(7)

while w<400:
    t.forward(100)
    t.left(90)
    w=w+100

while x<800:
    t.forward(150)
    t.left(90)
    x=x+100

while z<1200:
    t.forward(200)
    t.left(90)
    z=z+100
     
