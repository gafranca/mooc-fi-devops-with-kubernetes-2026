import os

import uvicorn
from fastapi import FastAPI

app = FastAPI(title="todo app")

@app.get("/")
def read_root():
    return {"app": "todo app"}

if __name__ == "__main__":
    port = int(os.getenv("PORT") or 8000)
    print(f"Server started in port {port}", flush=True)
    uvicorn.run(app, host="0.0.0.0", port=port)