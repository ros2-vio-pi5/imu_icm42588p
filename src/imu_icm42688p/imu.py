import time

from .comm import Comm
from .registers import DEVICE_CONFIG, INT_STATUS, REG_BANK_SEL


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

    def reset(self):
        soft_reset_bit = DEVICE_CONFIG.get_bit("SOFT_RESET_CONFIG").mask
        self.write_masked(DEVICE_CONFIG, soft_reset_bit, soft_reset_bit)

    def wait_for_reset_done(self, timeout=1.0):
        start = time.time()
        reset_done_bit = INT_STATUS.get_bit("RESET_DONE_INT").mask
        while time.time() - start < timeout:
            int_status = self.read(INT_STATUS)[0]
            if int_status & reset_done_bit:
                return True
            time.sleep(0.01)
        return False
