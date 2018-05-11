import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

clients = []

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('open')        
        clients.append(self)
      
    def on_message(self, message):
        print('send message')
        self.write_message('No messages allowed')

        
    def on_close(self):
        if self in clients:
            clients.remove(self)
            
    def check_origin(self, origin):
        return True


def WebServer(logfile):
    print('Server running')

    application = tornado.web.Application([
                (r'/ws', WSHandler),
            ])   
    
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()

