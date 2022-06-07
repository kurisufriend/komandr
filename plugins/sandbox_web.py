depends = ["bprint", "sand"]

from http.server import BaseHTTPRequestHandler, HTTPServer

def run(l):
    class MyServer(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>komand'r</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><ul>", "utf-8")) 
            for key in l["sand"].box.keys():
                self.wfile.write(bytes(f"<li>{key}:{l['sand'].box[key]}</li>", "utf-8"))
            self.wfile.write(bytes("</ul></body></html>", "utf-8"))
    server = HTTPServer(("localhost", 8080), MyServer)
    l["bprint"].p("started sandbox server at port 8080")
    server.serve_forever()#TODO: SUPPRESS THE LOGGING FROM THE WEBSERVER (AND ONLY THE WEBSERVER)
    server.server_close()