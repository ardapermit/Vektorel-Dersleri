#1 color
import turtle
t = turtle.Turtle()
t.color((.5, 1, 0))
for i in range(8):
    t.circle(50)
    t.left(45)
t.write("Çizim bitti!")
turtle.done()