import turtle

square = turtle.Turtle()
square.color("red","yellow") #2nd parameter represents the inside fill value
# To define the turtle colour border(Outline) of the thing, You can use hexcode and RGB values too
square.begin_fill()
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.end_fill()
square.penup()
square.forward(100)
square.pendown()
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)

turtle.done()