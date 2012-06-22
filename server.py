import time

from bottle import request, route, run, static_file

import doomba as doomba_
import vulcanuino


class MockObject(object):
    def __getattr__(self, name):
    	print name
        return lambda *args, **kwargs: None

try:
    doomba = doomba_.Doomba()
except:
    print "Warning: Roomba not connected"
    doomba = MockObject()
try:
    gun = vulcanuino.Vulcanuino()
except:
    print "Warning: Gun not connected"
    gun = MockObject()


@route('/')
def home():
    return static_file('controls.html', root='/Users/nat/code/doomba/control_page')

@route('/reset')
def reset_doomba():
    global doomba
    doomba = doomba_.Doomba()

@route('/forward')
def go_forward():
    doomba.forward()

@route('/back')
def go_back():
    doomba.back()

@route('/speed')
def set_speed():
    doomba.speed = int(request.query.speed) or 100

@route('/forward_left')
def go_forward_left():
    doomba.forward_left()

@route('/forward_right')
def go_forward_right():
    doomba.forward_right()

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
