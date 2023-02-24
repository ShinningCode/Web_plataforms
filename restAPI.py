import tornado.ioloop


import tornado.web


class AddHandler(tornado.web.RequestHandler):
    def get(self, n1, n2):
        result = int(n1) + int(n2)
        self.write(str(result))


class AddHandler(tornado.web.RequestHandler):
    def get(self, n1, n2):
        result = int(n1) + int(n2)
        self.write(str(result))


class MultiplyHandler(tornado.web.RequestHandler):
    def post(self):
        n1 = int(self.get_argument('n1'))
        n2 = int(self.get_argument('n2'))
        result = n1 * n2
        self.write(str(result))


class DivideHandler(tornado.web.RequestHandler):
    def put(self):
        n1 = int(self.get_argument('n1'))
        n2 = int(self.get_argument('n2'))
        result = n1 / n2
        self.write(str(result))

        
class PowerHandler(tornado.web.RequestHandler):
    def patch(self):
        n1 = int(self.get_argument('n1'))
        n2 = int(self.get_argument('n2'))
        result = pow(n1, n2)
        self.write(str(result))


class SubtractHandler(tornado.web.RequestHandler):
    def delete(self, n1, n2):
        result = int(n1) - int(n2)
        self.write(str(result))

        
app = tornado.web.Application([
    (r'/results/(\d+)/(\d+)', AddHandler),
    (r'/results/', MultiplyHandler),
    (r'/results/', DivideHandler),
    (r'/results/', PowerHandler),
    (r'/results/(\d+)/(\d+)', SubtractHandler)
])


if __name__ == '__main__':
    app.listen(4000)
    tornado.ioloop.IOLoop.current().start()
