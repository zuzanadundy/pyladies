from turtle import forward, left, exitonclick, right, shape

shape('turtle')

#pro 95 uhelnik zkrat forward na 10

n = int(input('pocet?'))

for xuhelnik in range(n):
    forward(100)
    left(180-(180*(1-(2/n))))
exitonclick

