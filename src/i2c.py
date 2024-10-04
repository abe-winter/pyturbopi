import fcntl
import os
import struct

class I2C:
    "replace with a library soon please"
    def __init__(self, bus, addr):
        self.bus = bus
        self.addr = addr
        self.open()
    
    def open(self):
        self.fd = os.open(self.bus, os.O_RDWR)
        ret = fcntl.ioctl(self.fd, 0x0703, self.addr)
        print('ioctl', ret)

    def write(self, register: int, *data: int):
        data = list(data)
        data[0] += register
        buf = struct.pack('b' * len(data), *data)
        n = os.write(self.fd, buf)
        assert n == len(buf)
