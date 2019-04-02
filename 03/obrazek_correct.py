from turtle import forward, left, exitonclick, right, shape, circle, fillcolor, begin_fill, end_fill, penup, pendown

shape('turtle')

#dum
fillcolor('blue')
begin_fill()
for ctverec in range(4):
    forward(150)
    left(90)
end_fill()

#strecha
left(90)
forward(150)
fillcolor('red')
begin_fill()
right(30)
forward(150)
right(120)
forward(150)
end_fill()

#presun k slunci
right(75)
penup()
left(180)
forward(250)
pendown()

#slunce
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()
left(135)

#presun od slunce
penup()
forward(700)
left(90)
forward(325)
pendown()
left(90)

#kmen
fillcolor('brown')
begin_fill()
for kmen in range(2):
    forward(20)
    left(90)
    forward(40)
    left(90)
end_fill()

#strom
fillcolor('lightgreen')
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
right(135)
forward(70.71)
right(90)
forward(70.71)
right(135)
forward(60)
end_fill()
right(180)
forward(10)
left(90)
penup()
forward(49.99)
pendown()

#strom2
for strom in range(2):
    fillcolor('lightgreen')
    begin_fill()
    left(90)
    forward(50)
    right(135)
    forward(70.71)
    right(90)
    forward(70.71)
    right(135)
    forward(50)
    right(90)
    penup()
    forward(49.99)
    pendown()
    end_fill()

exitonclick()