import os
import threading

import uvicorn
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="ping-pong")

counter = 0
counter_lock = threading.Lock()

@app.get("/pingpong")
@app.get("/")

def pingpong():
    global counter
    with counter_lock:
        current = counter
        counter += 1
    return PlainTextResponse(f"pong {current}")


if __name__ == "__main__":
    port = int(os.getenv("PORT") or 3000)
    uvicorn.run(app, host="0.0.0.0", port=port)