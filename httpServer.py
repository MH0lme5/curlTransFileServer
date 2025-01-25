from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        length = int(self.headers['Content-Length'])
        with open(self.path[1:], 'wb') as f:  # 路径前有个 /，去掉它
            f.write(self.rfile.read(length))
        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(('0.0.0.0', 8787), SimpleHTTPRequestHandler)
print("Serving on port 8787...")
httpd.serve_forever()
