import turtle


screen = turtle.Screen()
screen.screensize(400,400)
screen.title("polygon")
screen.bgcolor("black")
t = turtle.Turtle()
t.color("whitesmoke")
t.width(5)
t.fillcolor("blue")
t.begin_fill()

s = 3
a = 360/3
for n in range (s):
    t.forward(100)
    t.left(a)
t.left(90)
t.penup()
t.forward(65)
t.right(90)
t.pendown()

for n in range(s):
    t.forward(100)
    t.right(a)
t.end_fill()
turtle.done()