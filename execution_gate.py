def can_execute(state, vix):

    if vix > 30:
        return False, "VIX过高"

    if state == "crisis":
        return False, "危机模式禁止加仓"

    return True, "允许执行"
