import turtle
import math
flower = turtle.Turtle()
flower.color('red','yellow')
flower.speed(15)

for i in range(500):
    flower.forward(100)
    flower.left(math.sin(i))


turtle.done()