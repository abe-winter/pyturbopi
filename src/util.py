# import smbus2

BUS = "/dev/i2c-1"
BUS_ADDR = 0x7a

def signed_clamp(val, low, high):
    "clamps val to the range of (low, high) or (-low, -high)"
    # todo: move to util
    if val == 0:
        return val
    sign = 1 if val > 0 else -1
    clamped = max(min(abs(val), high), low)
    return clamped * sign

# def init_bus(bus: smbus2.SMBus):
#     # todo: move to util
#     bus._set_address(BUS_ADDR)
