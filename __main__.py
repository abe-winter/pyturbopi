#!/usr/bin/env python3
import time, logging
from smbus2 import SMBus
from src.util import BUS, init_bus, BUS_ADDR
from src.base import Base
from src.i2c import I2C

logger = logging.getLogger(__name__)

def go_wait_stop(base: Base, *efforts):
    base.actuate(*efforts)
    time.sleep(3)
    base.actuate()
    time.sleep(1)

def main():
    logging.basicConfig(level=logging.INFO)
    i2c = I2C('/dev/i2c-1', BUS_ADDR)
    base = Base(i2c)

    for i in range(4):
        motor = base.motors[i]
        logger.info('motor %d %s', motor.id, motor.name)
        motor.actuate(2)
        time.sleep(3)
        motor.actuate(0)

    logger.info('forward')
    go_wait_stop(base, *[1] * 4)

    logger.info('fast')
    go_wait_stop(base, *[2] * 4)

    logger.info('reverse')
    go_wait_stop(base, *[-1] * 4)

    logger.info('right')
    go_wait_stop(base, 1, -1, -1, 1)

if __name__ == '__main__':
    main()
