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

	def stop(self):
		self.drive_direct(0, 0)