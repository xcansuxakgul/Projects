import turtle as tr
import time 

size = 2
x, y = tr.position()
tr.penup()
tr.setposition(x,y-size*85)
tr.pendown()
tr.color('red')
tr.begin_fill()
tr.pensize(3)
tr.left(50)
tr.forward(133*size)
tr.circle(50*size,200)
tr.right(140)
tr.circle(50*size,200)
tr.forward(133*size)
tr.end_fill()
time.sleep(5)