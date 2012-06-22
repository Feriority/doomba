import tornado.autoreload
import tornado.ioloop
import tornado.web

import vulcanuino

_request_handlers = []


class VulcanuinoHandler(tornado.web.RequestHandler):
    class __metaclass__(type(tornado.web.RequestHandler)):
        def __init__(cls, name, bases, class_dict):
            super(type(cls), cls).__init__(name, bases, class_dict)
            _request_handlers.append(cls)

    gun = None

    name = None
    url = r'/'

    def get(self):
        self.send_command()
        for handler_class in _request_handlers:
            if handler_class.name is not None:
                self.write_link(handler_class.url, handler_class.name)

    def write_link(self, url, name):
        self.write('<a href="%s">%s</a><br>' % (url, name))

    def send_command(self):
        pass


class CommenceFiringHandler(VulcanuinoHandler):
    name = 'Commence Firing'
    url = r'/commence_firing'

    def send_command(self):
        self.gun.commence_firing()


class CeaseFireHandler(VulcanuinoHandler):
    name = 'Cease Fire'
    url = r'/cease_fire'

    def send_command(self):
        self.gun.cease_fire()


class PauseHandler(VulcanuinoHandler):
    name = 'Pause'
    url = r'/pause'

    def send_command(self):
        self.gun.pause()


def main():
    port_name = vulcanuino.guess_port_filename()
    VulcanuinoHandler.gun = vulcanuino.Vulcanuino(port_name)

    handlers = [tornado.web.url(h.url, h, name=h.name) for h in _request_handlers]
    application = tornado.web.Application(handlers)
    application.listen(8888)

    tornado.autoreload.start()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
