import yfinance as yf

def run_core():

    ndx = yf.download("^NDX", period="6mo")["Close"]
    vix = yf.download("^VIX", period="6mo")["Close"]

    ret = ndx.iloc[-1] / ndx.iloc[-20] - 1
    v = vix.iloc[-1]

    if ret > 0.05 and v < 18:
        state = "bull"
    elif -0.05 <= ret <= 0.05:
        state = "chop"
    elif ret < -0.08:
        state = "crisis"
    else:
        state = "pullback"

    base = {
        "SP500": 35,
        "NASDAQ100": 30,
        "TECH": 10,
        "CN_SEMI": 10,
        "DIVIDEND": 10,
        "GOLD": 5
    }

    if state == "crisis":
        base["GOLD"] += 8
        base["SP500"] -= 5

    total = sum(base.values())

    for k in base:
        base[k] = round(base[k] / total * 100, 2)

    return {
        "state": state,
        "allocation": base,
        "vix": float(v),
        "multiplier": 1.0
    }
