#!/usr/bin/env python
import SimpleHTTPServer

class MyHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header('Content-Security-Policy', "script-src 'sha256-uybHLI+qDunPRU2zC6ky8w1ywagNzyQn4XzCpBw8pp4='")
        self.send_header('X-Paws', 'hello')

if __name__ == '__main__':
    SimpleHTTPServer.test(HandlerClass=MyHTTPRequestHandler)