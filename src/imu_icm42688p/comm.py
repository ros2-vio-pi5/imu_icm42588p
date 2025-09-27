import spidev


class Comm:
    def read(self, reg_addr, length=1):
        raise NotImplementedError

    def write(self, reg_addr, value):
        raise NotImplementedError


class Spi(Comm):
    def __init__(self, bus=0, device=0, max_speed_hz=8000000, mode=0b11):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = max_speed_hz
        self.spi.mode = mode

    def read(self, reg_addr, length=1):
        tx = [reg_addr | 0x80] + [0] * length
        rx = self.spi.xfer2(tx)
        return rx[1:]

    def write(self, reg_addr, value):
        self.spi.xfer2([reg_addr & 0x7F, value])
