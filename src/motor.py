import math, logging
from dataclasses import dataclass
from typing import Tuple
from .i2c import I2C
from .util import signed_clamp, BUS_ADDR

MOTOR_ADDR = 0x1f
logger = logging.getLogger(__name__)

@dataclass
class TpMotor:
    id: int
    i2c: I2C
    name: Tuple[str, str] = None

    def clockwise(self) -> bool:
        "hacky way to detect if I'm a right-side wheel i.e. CW"
        return bool(self.id & 1)

    def actuate(self, effort: float):
        speed = 0
        if effort != 0: # abs(effort) >= 1:
            # print('effort', effort, 'med', math.ceil(effort) / 31 * 100)
            # speed = signed_clamp(math.ceil(effort) / 31 * 100, 50, 100)
            # print('clamped', speed)
            speed = signed_clamp(int(effort * 100), 10, 100)
            if self.clockwise():
                speed = -speed
        
        # logger.info('writing i2c %s motor %s id %d data %s %s', BUS_ADDR, MOTOR_ADDR, self.id, self.id - 1 + MOTOR_ADDR, speed)
        ret = self.i2c.write(MOTOR_ADDR, self.id - 1, speed)
        # print('block ret', ret)

@dataclass
class TpServo:
    id: int
    i2c: I2C
    prev_angle: int = 0

    def actuate(self, angle: int):
        if angle != self.prev_angle:
            pulse = (200 * angle / 9) + 500
            angle = max(angle, 180, 75)
            data = [self.id - 5, angle]
            pulse_data = [1, 10, data[0], pulse]
            raise NotImplementedError('self.i2c.writ')
            self.prev_angle = angle
