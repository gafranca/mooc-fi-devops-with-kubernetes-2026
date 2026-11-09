import json
import os
import random
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

HEX_CHARS = "0123456789abcdef"


def random_hex(length):
    return "".join(random.choices(HEX_CHARS, k=length))


def time_stamp():
    now = datetime.now(timezone.utc)
    return now.isoformat(timespec="milliseconds").replace("+00:00", "Z")

final_string = (
    f"{random_hex(8)}-{random_hex(4)}-"
    f"{random_hex(4)}-{random_hex(4)}-"
    f"{random_hex(12)}"
)

class StatusHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path

        if path not in ("/", "/status"):
            self.send_error(404, "Not Found")
            return

        status = {
            "timestamp": time_stamp(),
            "randomString": final_string
        }

        response = json.dumps(status).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

port = int(os.environ.get("PORT", 3000))

server = ThreadingHTTPServer(("0.0.0.0", port), StatusHandler)

print(f"HTTP server listening on port {port}", flush=True)

import threading
server_thread = threading.Thread(target=server.serve_forever, daemon=True)
server_thread.start()

while True:
    print(f"{time_stamp()}: {final_string}", flush=True)
    time.sleep(5)