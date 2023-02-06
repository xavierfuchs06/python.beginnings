import turtle
c = 0
r = 0
a = 0
aa = 0
t = turtle.Turtle()
s = turtle.getscreen()
t.speed(7)

print('Welche Form? Kreis = 0. Rechteck = 1')
ch=int(input())

if ch == 0:
    print('Wie viele Kreise sollen es werden?')
    a=int(input())

    print('Welcher Radius sollen die Kreise haben?')
    r=int(input())

    while c != a:
        t.circle(int(r))
        c=c+1
        r=r+25

if ch == 1:
    print('Wie viele Rechtecke sollen es werden?')
    a=int(input())

    print('Wie Lang sollen die Seiten werden?')
    r=int(input())

    while c != a:
            while aa<4:
                t.forward(r)
                t.left(90)
                aa=aa+1
            c=c+1
            r=r+10
        


