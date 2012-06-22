import os
import time

from arduino_serial import SerialPort

COMMENCE_FIRING = '1'
CEASE_FIRE = '0'
PAUSE = '.'


def guess_port_filename():
    dev_dir = '/dev'
    prefix = 'tty.usb'
    for filename in os.listdir(dev_dir):
        if filename.startswith(prefix):
            return os.path.join(dev_dir, filename)


class Vulcanuino(object):
    def __init__(self, port_name):
        self.serial_port = SerialPort(port_name, 9600)

        # Arduino resets when the serial port is open, give it time to boot up.
        time.sleep(5)

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
