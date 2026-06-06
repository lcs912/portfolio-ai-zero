import os
from datetime import datetime

FILE = "data/log.csv"

def log(state, allowed, reason):

    os.makedirs("data", exist_ok=True)

    exists = os.path.isfile(FILE)

    with open(FILE, "a") as f:

        if not exists:
            f.write("time,state,allowed,reason\n")

        f.write(f"{datetime.now()},{state},{allowed},{reason}\n")
