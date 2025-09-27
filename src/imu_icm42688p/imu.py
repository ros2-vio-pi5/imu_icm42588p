from .comm import Comm
from .registers import REG_BANK_SEL


class Imu:
    def __init__(self, comm: Comm):
        self.comm = comm
        self._current_bank = None

    def set_bank(self, bank):
        if bank not in range(5):
            raise ValueError("Invalid bank")
        if self._current_bank != bank:
            # read
            tx = [REG_BANK_SEL.address | 0x80, 0]
            rx = self.comm.read(tx[0])
            current_val = rx[0]
            # modify
            new_val = (current_val & 0xF8) | (bank & REG_BANK_SEL.get_bit("BANK_SEL").mask)
            # write
            self.comm.write(REG_BANK_SEL.address, new_val)
            self._current_bank = bank

    def read(self, reg, length=1):
        _, bank, reg_addr, *_ = reg
        self.set_bank(bank)
        return self.comm.read(reg_addr, length)

    def write(self, reg, value):
        _, bank, reg_addr, *_ = reg
        self.set_bank(bank)
        self.comm.write(reg_addr, value)

    def write_masked(self, reg, value, mask):
        current_val = self.read(reg)[0]
        new_val = (current_val & ~mask) | (value & mask)
        self.write(reg, new_val)
