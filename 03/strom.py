from turtle import forward, left, exitonclick, right, shape, circle, fillcolor, begin_fill, end_fill, penup, pendown

shape('turtle')

fillcolor('brown')
begin_fill()
for kmen in range(2):
    forward(20)
    left(90)
    forward(60)
    left(90)
end_fill()

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