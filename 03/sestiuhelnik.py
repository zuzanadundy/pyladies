from turtle import forward, left, exitonclick, right, shape

shape('turtle')

#sestiuhelnik ma 60 stupnu, osmiuhelnik 45, petiuhelnik ma 72

for sestiuhelnik in range(5):
    forward(100)
    left(72)
exitonclick()

from turtle import forward, left, exitonclick, right, shape

shape('turtle')

n = input('pocet?')
for xuhelnik in range(n):
    forward(100)
    left(180*(1-(2/n)))
exitonclick