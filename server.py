from bottle import route, run

import doomba
import vulcanuino


doomba = doomba.Doomba()
gun = vulcanuino.Vulcanuino(vulcanuino.guess_port_filename())


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
def shoot_dart():
	gun.single_shot()

@route('/start_rampage')
def start_rampage():
	gun.commence_firing()

@route('/end_rampage')
def end_rampage():
	gun.cease_fire()


run(host='10.12.5.29', port=8081)