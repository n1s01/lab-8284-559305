#!/usr/bin/env python3

"""Simple health check HTTP server.

Provides a `/health` endpoint that returns HTTP 200 with body 'OK'.
Run with `python main.py health` to start the server.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

def start_health_server(host: str = "0.0.0.0", port: int = 8000):
    """Start the health check HTTP server."""
    server = HTTPServer((host, port), HealthHandler)
    print(f"Health check server running at http://{host}:{port}/health")
    server.serve_forever()
