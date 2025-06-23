from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random

class SNMPMockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mock_data = {
            "in_octets": random.randint(10000, 100000),
            "out_octets": random.randint(10000, 100000),
            "in_errors": random.randint(0, 5),
            "out_errors": random.randint(0, 5),
            "speed": 1000000000
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(mock_data).encode())

if __name__ == "__main__":
    print("✅ SNMP Agent running on http://localhost:8000")
    server = HTTPServer(("localhost", 8000), SNMPMockHandler)
    server.serve_forever()
