from bottle import route, run
import pyroomba

ROOMBA_DEV = 'dev/tty.usbserial-A2001mZT'

roomba = pyroomba.Roomba(ROOMBA_DEV)
roomba.start()
roomba.safe()

@route('/')
def home():
	return "Press up to go forward, left to go left, right to go right, back to stop, and space to fire."

@route('/up/:speed')
def go_forward(speed=100):
	return "Moving forward at %s" % speed

@route('/left')
def turn_left():
	return "Turning left!"

@route('/right')
def turn_right():
	return "Turning right!"

@route('/fire')
def turn_right():
	return "Fire ze missles!"

run(host='localhost', port=8080)