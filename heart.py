import turtle
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.hideturtle()
t.goto(1,-10)
 
t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-75,130)
t.pendown()
t.color('white')
t.write("cuzin hoje?",font=("Verdana",25,"bold"))

t.penup()
t.goto(-220,-180)
t.pendown()
t.color('white')
t.write("Ass:patricia",font=("Verdana",30,"bold"))

turtle.done()

