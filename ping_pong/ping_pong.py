import os
import threading

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="ping-pong")

counter = 0
counter_lock = threading.Lock()


# Answers on /pingpong, and also on / so it keeps working if the Ingress
# strips the /pingpong prefix before forwarding the request.
@app.get("/pingpong")
@app.get("/")
def pingpong():
    global counter
    # Requests can be handled in several threads at once; the lock keeps the counter correct.
    with counter_lock:
        current = counter
        counter += 1
    return PlainTextResponse(f"pong {current}")


if __name__ == "__main__":
    port = int(os.getenv("PORT") or 3000)
    uvicorn.run(app, host="0.0.0.0", port=port)