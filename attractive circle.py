import turtle 
turtle.bgcolor("red")
Cppsecrets = turtle.Turtle()
Cppsecrets.speed(0)
for i in range(180):
    Cppsecrets.forward(100)
    Cppsecrets.right(30)
    Cppsecrets.forward(20)
    Cppsecrets.left(60)
    Cppsecrets.forward(50)
    Cppsecrets.right(30)
    Cppsecrets.penup()
    Cppsecrets.setposition(0, 0)
    Cppsecrets.pendown()
    Cppsecrets.right(2)
turtle.done()
