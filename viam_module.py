#!/usr/bin/env python3
import asyncio
from typing import Dict, Mapping
from viam.components.motor import Motor
from viam.components.base import Base
from viam.module import Module
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.easy_resource import EasyResource, stub_model
from src.motor import TpMotor
from src.i2c import I2C
from src.util import BUS_ADDR, BUS
from src.base import Base as TPBase

# todo: mutex maybe
GLOBAL_I2C = I2C(BUS, BUS_ADDR)

@stub_model
class MyMotor(Motor, EasyResource):
    MODEL = "awinter:turbopi:motor"
    motor: TpMotor

    def __init__(self, name: str):
        self.motor = TpMotor(1, GLOBAL_I2C, name)
        super().__init__(name)

    async def set_power(self, power: float, **kwargs):
        self.motor.actuate(power)
    
    # async def go_for(
    # async def go_to(
    # async def set_rpm(
    # async def reset_zero_position(
    # async def get_position(
    # async def get_properties(
    
    async def stop(self, **kwargs):
        return await self.set_power(0)

    # async def is_powered(
    # async def is_moving(self) -> bool:

def mecanum_velocity(linear, angular):
    "returns FL, FR, RL, RR"
    fl = linear.y - linear.x - (linear.y + linear.x) * angular.z
    fr = linear.y + linear.x + (linear.y + linear.x) * angular.z
    rl = linear.y + linear.x - (linear.y + linear.x) * angular.z
    rr = linear.y - linear.x + (linear.y + linear.x) * angular.z
    return fl, fr, rl, rr

@stub_model
class MyBase(Base, EasyResource):
    MODEL = "awinter:turbopi:base"
    tp: TPBase

    def __init__(self, name):
        self.tp = TPBase(GLOBAL_I2C)
        super().__init__(name)

    # async def move_straight(self, distance: int, velocity: float, **kwargs):
    #     raise NotImplementedError

    async def set_power(self, linear, angular, **kwargs):
        self.tp.actuate(*mecanum_velocity(linear, angular))

    async def stop(self, **kwargs):
        self.tp.actuate()

    # async def move_straight(
    # async def spin(
    # async def set_power(
    # async def set_velocity(
    # async def is_moving(self) -> bool:
    # async def get_properties(self, *, timeout: Optional[float] = None, **kwargs) -> Properties:


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
