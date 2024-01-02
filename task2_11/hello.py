from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

if __name__ == '__main__':
    try:
        server_address = ('localhost', 8000)
        httpd = HTTPServer(server_address, HelloWorldHandler)
        print('Сервер запущен на http://{}:{}/'.format(server_address[0], server_address[1]))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nСервер остановлен.')