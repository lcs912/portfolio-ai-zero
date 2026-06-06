from fastapi import FastAPI
from core import run_core
from execution_gate import can_execute
from logger import log
from notifier import send_wechat, send_email, format_msg

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/today")
def today():

    data = run_core()

    ok, reason = can_execute(data["state"], data["vix"])

    log(data["state"], ok, reason)

    msg = format_msg(data, ok, reason)

    send_wechat(msg)
    send_email(msg)

    data["execution_allowed"] = ok
    data["reason"] = reason

    return data
