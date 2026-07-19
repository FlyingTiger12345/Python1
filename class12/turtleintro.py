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

s = 6
a = 360/6
for n in range (s):
    t.forward(100)
    t.left(a)
t.end_fill()
turtle.done()