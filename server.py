from bottle import route, run
import pyroomba

ROOMBA_PORT = '/dev/tty.usbserial-A2001mZT'


class Doomba(pyroomba.Roomba):
	def __init__(self, port, **kwargs):
		super(SimpleDoomba, self).__init__(self, port, **kwargs)
		self.start()
		self.safe()
		self.speed = 100

	def left(self):
		self.drive_direct(-self.speed, self.speed)
		
	def right(self):
		self.drive_direct(self.speed, -self.speed)

	def forward(self):
		self.drive_direct(self.speed, self.speed)

	def stop(self):
		self.drive_direct(0, 0)


doomba = Doomba(ROOMBA_PORT)

@route('/')
def home():
	return "Press up to go forward, left to go left, right to go right, back to stop, and space to fire."

@route('/forward')
def go_forward(speed=100):
	doomba.forward()

@route('/speed=:speed')
def set_speed(speed):
	doomba.speed = speed

@route('/left')
def turn_left():
	doomba.left()

@route('/right')
def turn_right():
	doomba.right()

@route('/stop')
def stop_moving():
	doomba.stop()

@route('/fire')
def fire_missles():
	return "Fire ze missles!"


run(host='localhost', port=8080)