import time

import pyroomba


ROOMBA_PORT = '/dev/tty.usbserial-A2001mZT'


class Doomba(pyroomba.RoombaClassic):
	def __init__(self, port=ROOMBA_PORT, **kwargs):
		super(Doomba, self).__init__(port, **kwargs)
		self.start()
		self.safe()
		self.speed = 100

	def left(self):
		self.drive_direct(-self.speed, self.speed)
		
	def right(self):
		self.drive_direct(self.speed, -self.speed)

	def forward(self):
		self.drive_direct(self.speed, self.speed)

	def back(self):
		self.drive_direct(-self.speed, -self.speed)

	def stop(self):
		self.drive_direct(0, 0)

if __name__ == '__main__':
	doomba = Doomba()
	doomba.forward()
	time.sleep(1)
	doomba.right()
	time.sleep(1)
	doomba.left()
	time.sleep(1)
	doomba.back()
	time.sleep(1)
	doomba.stop()