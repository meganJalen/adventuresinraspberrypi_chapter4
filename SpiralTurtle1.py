import turtle
Jessica = turtle.Turtle()
Jessica.color("purple")
Jessica.pensize(5)
Jessica.shape("turtle")
print (range(5,100,2) )
for size in range(5,100,2):
    Jessica.forward(size)
    Jessica.left(25)
