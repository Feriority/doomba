import os
import time

from arduino_serial import SerialPort


COMMENCE_FIRING = '1'
CEASE_FIRE = '0'
PAUSE = '.'

ARDUINO_PORT = '/dev/tty.usbmodem1411'

class Vulcanuino(object):
    def __init__(self, port_name=ARDUINO_PORT):
        self.serial_port = SerialPort(port_name, 9600)

        # Arduino resets when the serial port is open, give it time to boot up.
        time.sleep(5)

    def single_shot(self, pause_time=20):
        self.commence_firing()
        self.pause(pause_time)
        self.cease_fire()

    def commence_firing(self):
        self._write(COMMENCE_FIRING)

    def cease_fire(self):
        self._write(CEASE_FIRE)

    def pause(self, n=1):
        self._write(PAUSE * n)

    def _write(self, s):
        self.serial_port.write(s)


def main():
    port_filename = guess_port_filename()
    vulcanuino = Vulcanuino(port_filename)
    for i in range(5):
        vulcanuino.commence_firing()
        vulcanuino.pause(20)
        vulcanuino.cease_fire()
        vulcanuino.pause(10)

    # Give the commands time to execute before the port is closed.
    time.sleep(10)

if __name__ == '__main__':
    main()
