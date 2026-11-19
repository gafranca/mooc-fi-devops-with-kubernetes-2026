import os
import random
import threading
import time
from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI, Response

HEX_CHARS = "0123456789abcdef"


def random_hex(length):
    return "".join(random.choices(HEX_CHARS, k=length))


def time_stamp():
    now = datetime.now(timezone.utc)
    return now.isoformat(timespec="milliseconds").replace("+00:00", "Z")

random_string_8_characters = random_hex(8)
random_string_4_characters_1 = random_hex(4)
random_string_4_characters_2 = random_hex(4)
random_string_4_characters_3 = random_hex(4)
random_string_12_characters = random_hex(12)

final_string = (
    f"{random_string_8_characters}-{random_string_4_characters_1}-"
    f"{random_string_4_characters_2}-{random_string_4_characters_3}-"
    f"{random_string_12_characters}"
)

app = FastAPI(title="log output")


@app.get("/")
@app.get("/status")
def status():
    return {"timestamp": time_stamp(), "random_string": final_string}


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)


def log_forever():
    while True:
        print(f"{time_stamp()}: {final_string}", flush=True)
        time.sleep(5)


if __name__ == "__main__":
    threading.Thread(target=log_forever, daemon=True).start()
    port = int(os.getenv("PORT") or 3000)
    uvicorn.run(app, host="0.0.0.0", port=port)