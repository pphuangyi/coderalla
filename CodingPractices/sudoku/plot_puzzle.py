#! /Users/yhuang10/opt/anaconda3/bin/python3.8
import turtle
from time import sleep

myPen = turtle.Turtle()
# myPen.tracer(0)
myPen.speed(0)
myPen.color('#000000')
myPen.hideturtle()
topLeft_x, topLeft_y = -150, 150

def text(message, x, y, size):
	FONT = ('Arial', size, 'normal')
	myPen.penup()
	myPen.goto(x, y)
	myPen.write(message, align='center', font=FONT)

def drawGrid(grid):
	intDim = 35

	for row in range(0, 10):
		if (row % 3) == 0:
			myPen.pensize(3)
		else:
			myPen.pensize(1)
		y, x_start, x_end = topLeft_y - row * intDim, topLeft_x, topLeft_x + 9 * intDim
		myPen.penup()
		myPen.goto(x_start, y)
		myPen.pendown()
		myPen.goto(x_end, y)

	for col in range(0, 10):
		if (col % 3) == 0:
			myPen.pensize(3)
		else:
			myPen.pensize(1)
		x, y_start, y_end = topLeft_x + col * intDim, topLeft_y, topLeft_y - 9 * intDim
		myPen.penup()
		myPen.goto(x, y_start)
		myPen.pendown()
		myPen.goto(x, y_end)

	for row in range(0, 9):
		for col in range(0, 9):
			x = topLeft_x + (col + .5) * intDim
			y = topLeft_y - (row + .8) * intDim
			text(grid[row][col], x, y, 18)

if __name__ == '__main__':
	grid = []
	for i in range(9):
		grid.append([0 for _ in range(9)])

	drawGrid(grid)
	myPen.getscreen().update()
	input()
	grid = []
	for i in range(9):
		grid.append([i for i in range(9)])

	drawGrid(grid)
	myPen.getscreen().update()
	input()
	# sleep(1)
