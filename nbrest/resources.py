import http.server
import socketserver
from functools import wraps
import threading

endpoints = {}


def expose(path):
    def real_decorator(function):
        global endpoints
        print(path, "to endpoints")
        endpoints[path] = function
        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
    return real_decorator






class MyHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print("Do Get Gatooo", self.path, str(endpoints))
        if self.path in endpoints:
            self.wfile.write(
                bytes(
                    str(endpoints[self.path]()), "utf-8"
                )
            )
        else:
            super().do_GET()




def runserver(PORT=8911):
    server = socketserver.TCPServer(("", PORT), MyHandler)
    thread = threading.Thread(target = server.serve_forever)
    thread.setdaemon = True
    thread.start()
