from bottle import request, route, run, static_file

import doomba
import vulcanuino


class MockObject(object):
	def __getattr__(self, name):
		return lambda *args, **kwargs: None

try:
	doomba = doomba.Doomba()
except:
	doomba = MockObject()
try:
	gun = vulcanuino.Vulcanuino(vulcanuino.guess_port_filename())
except:
	gun = MockObject()


@route('/')
def home():
	static_file('controls.html', root='/Users/nat/code/doomba/control_page')

@route('/forward')
def go_forward():
	doomba.forward()

@route('/back')
def go_back():
	doomba.back()

@route('/speed')
def set_speed():
	doomba.speed = request.query.speed or 100

@route('/left')
def turn_left():
	doomba.left()

@route('/right')
def turn_right():
	doomba.right()

@route('/custom')
def custom_movement():
	left = request.query.left or 0
	right = request.query.right or 0
	doomba.drive_direct(left, right)

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

run(host='10.12.5.29', port=8080)
