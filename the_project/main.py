import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="todo app")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
      <head><title>Todo app</title></head>
      <body>
        <h1>Todo app</h1>
        <p>Nothing to do yet.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.getenv("PORT") or 8000)
    print(f"Server started in port {port}", flush=True)
    uvicorn.run(app, host="0.0.0.0", port=port)