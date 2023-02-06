import datetime
import json
import http.server
import socketserver
import logging


class TestingServerApp:

    def __init__(self):
        self.app_name = "Testing server"

    @staticmethod
    def logger(*args):
        print(datetime.datetime.now(), *args)


class ServerHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        data = dict()
        data["action"] = None

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        # content_length = int(self.headers['Content-Length'])
        # body = self.rfile.read()

        body = None

            
        data = {'received': "bublik"}
        testing_server.logger(f"Data received: {data}")

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


if __name__ == "__main__":

    testing_server = TestingServerApp()

    PORT = 8080

    with socketserver.TCPServer(("", PORT), ServerHandler) as httpd:
        testing_server.logger("Start server at port", PORT)
        httpd.serve_forever()
