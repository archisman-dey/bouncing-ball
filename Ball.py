"""A dancing ball writeen in Python3"""

import curses as cp
import time
import random
import sys


length = 50
height = 20
speed = 20 #number of miliseconds between each ball movement
ballSymbol = '@'	#should be a single character

class Ball (object) :
	def __init__ (self):
		x = random.randint(1, length-2)
		y = random.randint(1, height-2)
		self.pos = (y, x)
		self.direction = "NE"

	def move (self, direction = None):
		if direction == None:
			direction = self.direction

		if direction == "NE":
			self.pos = (self.pos[0]-1, self.pos[1]+1)
		
		elif direction == "NW":
			self.pos = (self.pos[0]-1, self.pos[1]-1)
		
		elif direction == "SE":
			self.pos = (self.pos[0]+1, self.pos[1]+1)
		
		elif direction == "SW":
			self.pos = (self.pos[0]+1, self.pos[1]-1)

	def fatalCollision(self):
		if (self.pos[0] < 1 or self.pos[0] > height-2) and (self.pos[1] < 1 or self.pos[1] > length-2):
			return True
		else:
			return False

	def collides(self):
		if self.pos[0] < 1 or self.pos[0] > height-2:
			return True
		if self.pos[1] < 1 or self.pos[1] > length-2:
			return True
		return False

	def newDirection(self):
		if self.direction == "NE":
			if self.pos[0] < 1 : 
				self.direction = "SE"
			elif self.pos[1] > length-2 :
				self.direction = "NW"

		if self.direction == "NW":
			if self.pos[0] < 1 : 
				self.direction = "SW"
			elif self.pos[1] < 1 :
				self.direction = "NE"

		if self.direction == "SE":
			if self.pos[0] > height-2 : 
				self.direction = "NE"
			elif self.pos[1] > length-2 :
				self.direction = "SW"

		if self.direction == "SW":
			if self.pos[0] > height-2 : 
				self.direction = "NW"
			elif self.pos[1] < 1 :
				self.direction = "SE"


def makeScreen():
	scrvar = cp.initscr()
	
	screen = cp.newwin(height, length, 0, 0)
	
	cp.noecho()
	cp.cbreak()
	cp.curs_set(False)
	cp.flushinp()

	screen.border(0)
	screen.keypad(True)
	screen.refresh()

	return screen

def close(screen):
	screen.keypad(False)
	cp.curs_set(True)
	cp.nocbreak()
	cp.echo()
	cp.endwin()
	sys.exit(0)

def displayBall(screen, ball):
	screen.erase()
	screen.border(0)

	screen.addstr(ball.pos[0], ball.pos[1], ballSymbol)

	screen.refresh()

print("Press q to exit.")
time.sleep(1)

screen = makeScreen()

screen.timeout(speed)
key = 222 #initialises key with a random number

ball = Ball()

while True:
	displayBall(screen, ball)

	ball.move()

	if ball.fatalCollision():
		time.sleep(1)
		close(screen)
	elif ball.collides():
		ball.newDirection()

	key = screen.getch()

	if (key == 113 or key == 811):		#113 and 811 are codes for q and Q respectively
		close(screen)
