depends = ["bprint", "sand"]

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

def run(l):
    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            queries = parse_qs(urlparse(self.path).query)
            
            single = None
            for asked in queries.keys():
                if l["sand"].box.get(asked):
                    single = asked
                    break

            self.wfile.write(bytes(json.dumps(l["sand"].box[single]) if single else json.dumps(l['sand'].box, indent = 4), "utf-8"))

    server = HTTPServer(("localhost", 8080), MyServer)
    l["bprint"].p("started sandbox server at port 8080")
    server.serve_forever()#TODO: SUPPRESS THE LOGGING FROM THE WEBSERVER (AND ONLY THE WEBSERVER)
    server.server_close()