import turtle
screen = turtle.Screen()
screen.screensize(600,600)
screen.title("spiral square")
t = turtle.Turtle()
t.width(1)
screen.bgcolor("green")
t.color("blue")
s = 100
c = 4


for i in range(c):
    t.forward(s)
    t.right(90)