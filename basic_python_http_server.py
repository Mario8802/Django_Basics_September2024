import http.server
import socketserver

# Define the handler for the server
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Send a 200 OK response
        self.send_response(200)

        # Set the content-type header
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Write the content to the response
        self.wfile.write(b"Hello, User! Welcome to your server.")

# Port to listen on
PORT = 8080

# Set up the socket server
handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
