import tornado.ioloop
import tornado.web

# Creamos una clase que maneja la petición HTTP
class MyHandler(tornado.web.RequestHandler):
    def initialize(self, data):
        self.data = data
        
    def get(self):
        self.write("Datos: " + self.data)

    def post(self):
        new_data = self.get_argument("new_data")
        self.data += new_data
        self.write("Datos actualizados: " + self.data)

    def put(self):
        updated_data = self.get_argument("updated_data")
        self.data = updated_data
        self.write("Datos actualizados: " + self.data)

    def delete(self):
        self.data = ""
        self.write("Datos eliminados")

if __name__ == "__main__":
    data = "Hola, mundo"
    # Creamos la aplicación web Tornado
    app = tornado.web.Application([
        (r"/", MyHandler, dict(data=data)),
    ])
    # Iniciamos el servidor web
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
