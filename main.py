import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
distance=random.randrange(1,100)
race=random.randrange(1,100)
michelangelo.forward(race)
leonardo.forward(race)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for match in range(10):
  for mich in range(1):
    random_distance=random.randrange(1,10)
    michelangelo.forward(random_distance)
  for leo in range(1):
    random_race=random.randrange(1,10)
    leonardo.forward(random_race)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
seq=(3,4,6,9,12)
for i in range(5):
  list=seq[i]
  leonardo.down()
  for x in range(list):
    leonardo.forward(50)
    leonardo.left(360/list)
  leonardo.up()
  leonardo.clear()


window.exitonclick()
