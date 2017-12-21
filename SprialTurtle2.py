import turtle
Jessica = turtle.Turtle()
Jessica.color("red")
Jessica.shape("turtle")
print (range(5,100,2))
Jessica.penup()
for size in range (5,100,2) :
       Jessica.stamp()
       Jessica.forward(size)
       Jessica.left(25) 
       
