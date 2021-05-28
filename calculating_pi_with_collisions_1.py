#code to calculate digits of pi using elastics collisions
#written by PrAnjal

import turtle
from Block import Block

n = int(input("n: "))			#enter the number of digits you want to calculate
collisions = 0

def isCollision(t1, t2):		#a function to check the collision betwwen the blocks
	distance = abs(t1.xcor()-t2.xcor())

	if distance <= 10*(n+1)+1:
		return True
	else:
		return False

#Set up the screen and the environment
turtle.speed()
wn = turtle.Screen()
wn.setup(width=800, height=500)
wn.bgcolor("black")
wn.title("Pie")
wn.tracer(0)

pen = turtle.Turtle()
pen.setposition(-130,100)
pen.hideturtle()
pen.speed(0)
pen.color('white')
pen.right(90)
pen.fd(110)
pen.left(90)
pen.fd(700)

#Create a collision counter
collisions_pen = turtle.Turtle()
collisions_pen.speed(0)
collisions_pen.color("white")
collisions_pen.penup()
collisions_pen.setposition(-290, 200)
scorestring = "Collisions: %s" %collisions
collisions_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))
collisions_pen.hideturtle()

#create two block objects
small = Block(1, turtle.Vec2D(0, 0), turtle.Vec2D(0, 1), 1, "yellow")
big = Block(100**(n-1), turtle.Vec2D(-2/(10**(n-1)), 0), turtle.Vec2D(100, 10*(n-1)+1), n, "green")

block = [small, big]
blocks = [turtle.Turtle(), turtle.Turtle()]

while True:
	wn.update()

	i = 0
	for blk in block:
		blk.update()
		blk.draw(blocks[i])
		i += 1

	if small.position[0] <= -119:			#Check the collision with the wall
		small.velocity *= -1
		collisions += 1
		scorestring = "Collisions: %s" %collisions
		collisions_pen.clear()
		collisions_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))

	mass1 = small.mass
	mass2 = big.mass
	M = mass1 + mass2

	#Set the velocities after each collision
	vel1 = (mass1 - mass2)/M * block[0].velocity
	vel1 += 2*mass2/M * block[1].velocity

	vel2 = (mass2 - mass1)/M * block[1].velocity
	vel2 += 2*mass1/M * block[0].velocity

	if isCollision(blocks[0], blocks[1]):
		block[0].velocity = vel1
		block[1].velocity = vel2
		collisions += 1

		scorestring = "Collisions: %s" %collisions
		collisions_pen.clear()
		collisions_pen.write(scorestring, False, align="left", font=("Arial", 14,"normal"))

wn.exitonclick()
wn.mainloop()