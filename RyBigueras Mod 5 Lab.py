#Ryne Bigueras
#2/20/22


#Problem 1 "Hello World" 100 times

for i in range (100):
    print("Hello World")


#Problem 2 print numbers to their own line

for n in (12,10,32,3,66,17,42,99,20):
    print(n)

#Problem 3

import turtle
ws = turtle.Screen()
lime = turtle.Turtle()

sides = input("How many sides? ")
length = input("What is the length? ")
pcolor = input("Color of line? ")
fcolor = input("Color inside? ")

lime.pencolor(pcolor)
lime.fillcolor(fcolor)

lime.begin_fill()

for i in range(int(sides)):
    lime.forward(int(length))
    lime.left(int(360)/int(sides))

lime.end_fill()

#Problem 4 print 1-50 divisble by 3, 5, and both.

one = int(1)
fifty = int(50)
for i in range (one, fifty):
    if(i%3==0):
        print("Divisible by 3", i)

for i in range (one, fifty):
    if(i%5==0):
        print("Divisible by 5", i)

for i in range (one, fifty):
    if((i%3==0)and(i%5==0)):
        print("Divisible by both", i)

#Problem 5 draw something
import turtle

bm = turtle.Turtle()

ws=turtle.Screen()
ws.bgcolor("yellow")

bm.fillcolor("black")

bm.begin_fill()

#Tail
bm.right (45)
bm.forward (85)
bm.left (90)
bm.forward (85)

#right wing

bm.right (90)
bm.forward (50)
bm.left (90)
bm.forward (50)
bm.circle (50,150)

bm.left (45)
bm.forward (50)
bm.right (90)
bm.forward (50)

#head
bm.right(40)
bm.forward (25)
bm.left(160)
bm.forward (25)
bm.right(90)
bm.forward(5)
bm.right(90)
bm.forward(25)
bm.left(160)
bm.forward(25)
bm.right(40)

#left wing

bm.left (0)
bm.forward (50)
bm.right (90)
bm.forward (50)
bm.left(45)
bm.circle (50,150)
bm.forward (50)
bm.left(95)
bm.forward (50)

bm.end_fill()

#Batman...kind of.

