import turtle
screen = turtle.Screen()
screen.screensize(600,600)
screen.title("spiral square")
t = turtle.Turtle()
screen.bgcolor("green")
t.color("blue")
s = 20

while True:
    t.forward(s)
    t.right(90)
    s+=5