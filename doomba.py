import time

import pyroomba


ROOMBA_PORT = '/dev/tty.usbserial-A2001mZT'


class Doomba(pyroomba.RoombaClassic):
    def __init__(self, port=ROOMBA_PORT, **kwargs):
        super(Doomba, self).__init__(port, **kwargs)
        self.start()
        #self.safe()
        self.speed = 200
        self.turn_ratio = 0.75

    def left(self):
        self.drive_direct(-self.speed, self.speed)

    def right(self):
        self.drive_direct(self.speed, -self.speed)

    def forward_left(self):
        right_wheel = self.speed * (1 - self.turn_ratio + 1)
        left_wheel = self.speed * self.turn_ratio

        self.drive_direct(left_wheel, right_wheel)

    def forward_right(self):
        rightt_wheel = self.speed * self.turn_ratio
        left_wheel = self.speed * (1 - self.turn_ratio + 1)

        self.drive_direct(left_wheel, right_wheel)

    def forward(self):
        self.drive_direct(-self.speed, -self.speed)

    def back(self):
        self.drive_direct(self.speed, self.speed)

    def stop(self):
        self.drive_direct(0, 0)

if __name__ == '__main__':
    doomba = Doomba()
    doomba.forward()
    time.sleep(1)
    doomba.forward_left()
    time.sleep(1)
    doomba.forward_right()
    time.sleep(1)
    doomba.right()
    time.sleep(1)
    doomba.left()
    time.sleep(1)
    doomba.back()
    time.sleep(1)
    doomba.stop()
