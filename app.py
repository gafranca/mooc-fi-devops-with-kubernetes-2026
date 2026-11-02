import random
import time
from datetime import datetime, timezone

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

while True:
    print(f"{time_stamp()}: {final_string}", flush=True)
    time.sleep(5)