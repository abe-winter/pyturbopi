#!/usr/bin/env python
import itertools
from typing import List
from .motor import TpMotor
from .i2c import I2C

MOTOR_NAMES = list(itertools.product(('front', 'rear'), ('left', 'right')))

class Base:
    ""
    motors: List[TpMotor]

    def __init__(self, i2c: I2C):
        self.motors = [TpMotor(i + 1, i2c, name) for i, name in enumerate(MOTOR_NAMES)]

    def actuate(self, *efforts: int):
        if not efforts:
            efforts = [0] * len(self.motors)
        for motor, effort in zip(self.motors, efforts):
            motor.actuate(effort)
