# Auto-generated register definitions
# WARNING: This file is generated. Do not edit manually.
# Datasheet Revision: 1.8
# Document Number: DS-000347


from dataclasses import dataclass, field
from typing import Dict, Tuple


@dataclass(frozen=True)
class BitField:
    name: str
    mask: int

    def __repr__(self):
        return f"BitField(name={self.name!r}, mask=0x{self.mask:X})"


@dataclass(frozen=True)
class Register:
    name: str
    bank: int
    address: int
    serial_if: str
    reset_value: int
    clock_domain: str
    bits: Tuple[BitField, ...]

    _bit_map: Dict[str, BitField] = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        object.__setattr__(self, "_bit_map", {bit.name: bit for bit in self.bits})

    def get_bit(self, name: str) -> BitField:
        return self._bit_map[name]

    def iter_bits(self):
        return iter(self.bits)

    def __repr__(self):
        bits_str = ", ".join(repr(bit) for bit in self.bits)
        return (
            f"Register(name={self.name!r}, bank={self.bank}, address=0x{self.address:X}, "
            f"serial_if={self.serial_if!r}, reset_value=0x{self.reset_value:X}, "
            f"clock_domain={self.clock_domain!r}, bits=[{bits_str}])"
        )

    def __iter__(self):
        yield self.name
        yield self.bank
        yield self.address
        yield self.serial_if
        yield self.reset_value
        yield self.clock_domain
        yield self.bits

    def bitmask(self) -> int:
        combined = 0
        for bit in self.bits:
            combined |= bit.mask
        return combined

    def is_default(self, value: int) -> bool:
        mask = self.bitmask()
        masked_val = value & mask
        masked_reset = self.reset_value & mask
        return masked_val == masked_reset

    def bits_dict(self, value: int) -> dict:
        result = {}
        for bit in self.bits:
            masked_val = value & bit.mask
            shift = 0
            mask = bit.mask
            while (mask & 1) == 0:
                mask >>= 1
                shift += 1
            field_val = masked_val >> shift
            result[bit.name] = field_val
        return result


# Register constants

DEVICE_CONFIG = Register(
    name="DEVICE_CONFIG",
    bank=0,
    address=0x11,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="SPI_MODE", mask=0x10),
        BitField(name="SOFT_RESET_CONFIG", mask=0x1),
    ),
)

DRIVE_CONFIG = Register(
    name="DRIVE_CONFIG",
    bank=0,
    address=0x13,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="I2C_SLEW_RATE", mask=0x38),
        BitField(name="SPI_SLEW_RATE", mask=0x7),
    ),
)

INT_CONFIG = Register(
    name="INT_CONFIG",
    bank=0,
    address=0x14,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="INT2_MODE", mask=0x20),
        BitField(name="INT2_DRIVE_CIRCUIT", mask=0x10),
        BitField(name="INT2_POLARITY", mask=0x8),
        BitField(name="INT1_MODE", mask=0x4),
        BitField(name="INT1_DRIVE_CIRCUIT", mask=0x2),
        BitField(name="INT1_POLARITY", mask=0x1),
    ),
)

FIFO_CONFIG = Register(
    name="FIFO_CONFIG",
    bank=0,
    address=0x16,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_MODE", mask=0xC0),),
)

TEMP_DATA1 = Register(
    name="TEMP_DATA1",
    bank=0,
    address=0x1D,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="TEMP_DATA", mask=0xFF),),
)

TEMP_DATA0 = Register(
    name="TEMP_DATA0",
    bank=0,
    address=0x1E,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="TEMP_DATA", mask=0xFF),),
)

ACCEL_DATA_X1 = Register(
    name="ACCEL_DATA_X1",
    bank=0,
    address=0x1F,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_DATA_X", mask=0xFF),),
)

ACCEL_DATA_X0 = Register(
    name="ACCEL_DATA_X0",
    bank=0,
    address=0x20,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_DATA_X", mask=0xFF),),
)

ACCEL_DATA_Y1 = Register(
    name="ACCEL_DATA_Y1",
    bank=0,
    address=0x21,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_DATA_Y", mask=0xFF),),
)

ACCEL_DATA_Y0 = Register(
    name="ACCEL_DATA_Y0",
    bank=0,
    address=0x22,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_DATA_Y", mask=0xFF),),
)

ACCEL_DATA_Z1 = Register(
    name="ACCEL_DATA_Z1",
    bank=0,
    address=0x23,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_DATA_Z", mask=0xFF),),
)

ACCEL_DATA_Z0 = Register(
    name="ACCEL_DATA_Z0",
    bank=0,
    address=0x24,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_DATA_Z", mask=0xFF),),
)

GYRO_DATA_X1 = Register(
    name="GYRO_DATA_X1",
    bank=0,
    address=0x25,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_DATA_X", mask=0xFF),),
)

GYRO_DATA_X0 = Register(
    name="GYRO_DATA_X0",
    bank=0,
    address=0x26,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_DATA_X", mask=0xFF),),
)

GYRO_DATA_Y1 = Register(
    name="GYRO_DATA_Y1",
    bank=0,
    address=0x27,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_DATA_Y", mask=0xFF),),
)

GYRO_DATA_Y0 = Register(
    name="GYRO_DATA_Y0",
    bank=0,
    address=0x28,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_DATA_Y", mask=0xFF),),
)

GYRO_DATA_Z1 = Register(
    name="GYRO_DATA_Z1",
    bank=0,
    address=0x29,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_DATA_Z", mask=0xFF),),
)

GYRO_DATA_Z0 = Register(
    name="GYRO_DATA_Z0",
    bank=0,
    address=0x2A,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_DATA_Z", mask=0xFF),),
)

TMST_FSYNCH = Register(
    name="TMST_FSYNCH",
    bank=0,
    address=0x2B,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="TMST_FSYNC_DATA_UI", mask=0xFF),),
)

TMST_FSYNCL = Register(
    name="TMST_FSYNCL",
    bank=0,
    address=0x2C,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="TMST_FSYNC_DATA_UI", mask=0xFF),),
)

INT_STATUS = Register(
    name="INT_STATUS",
    bank=0,
    address=0x2D,
    serial_if="R/C",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="UI_FSYNC_INT", mask=0x40),
        BitField(name="PLL_RDY_INT", mask=0x20),
        BitField(name="RESET_DONE_INT", mask=0x10),
        BitField(name="DATA_RDY_INT", mask=0x8),
        BitField(name="FIFO_THS_INT", mask=0x4),
        BitField(name="FIFO_FULL_INT", mask=0x2),
        BitField(name="AGC_RDY_INT", mask=0x1),
    ),
)

FIFO_COUNTH = Register(
    name="FIFO_COUNTH",
    bank=0,
    address=0x2E,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_COUNT", mask=0xFF),),
)

FIFO_COUNTL = Register(
    name="FIFO_COUNTL",
    bank=0,
    address=0x2F,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_COUNT", mask=0xFF),),
)

FIFO_DATA = Register(
    name="FIFO_DATA",
    bank=0,
    address=0x30,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_DATA", mask=0xFF),),
)

APEX_DATA0 = Register(
    name="APEX_DATA0",
    bank=0,
    address=0x31,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="STEP_CNT", mask=0xFF),),
)

APEX_DATA1 = Register(
    name="APEX_DATA1",
    bank=0,
    address=0x32,
    serial_if="SYNCR",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="STEP_CNT", mask=0xFF),),
)

APEX_DATA2 = Register(
    name="APEX_DATA2",
    bank=0,
    address=0x33,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="STEP_CADENCE", mask=0xFF),),
)

APEX_DATA3 = Register(
    name="APEX_DATA3",
    bank=0,
    address=0x34,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="DMP_IDLE", mask=0x4),
        BitField(name="ACTIVITY_CLASS", mask=0x3),
    ),
)

APEX_DATA4 = Register(
    name="APEX_DATA4",
    bank=0,
    address=0x35,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="TAP_NUM", mask=0x18),
        BitField(name="TAP_AXIS", mask=0x6),
        BitField(name="TAP_DIR", mask=0x1),
    ),
)

APEX_DATA5 = Register(
    name="APEX_DATA5",
    bank=0,
    address=0x36,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="DOUBLE_TAP_TIMING", mask=0x3F),),
)

INT_STATUS2 = Register(
    name="INT_STATUS2",
    bank=0,
    address=0x37,
    serial_if="R/C",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="SMD_INT", mask=0x8),
        BitField(name="WOM_Z_INT", mask=0x4),
        BitField(name="WOM_Y_INT", mask=0x2),
        BitField(name="WOM_X_INT", mask=0x1),
    ),
)

INT_STATUS3 = Register(
    name="INT_STATUS3",
    bank=0,
    address=0x38,
    serial_if="R/C",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="STEP_DET_INT", mask=0x20),
        BitField(name="STEP_CNT_OVF_INT", mask=0x10),
        BitField(name="TILT_DET_INT", mask=0x8),
        BitField(name="WAKE_INT", mask=0x4),
        BitField(name="SLEEP_INT", mask=0x2),
        BitField(name="TAP_DET_INT", mask=0x1),
    ),
)

SIGNAL_PATH_RESET = Register(
    name="SIGNAL_PATH_RESET",
    bank=0,
    address=0x4B,
    serial_if="W/C",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="DMP_INIT_EN", mask=0x40),
        BitField(name="DMP_MEM_RESET_EN", mask=0x20),
        BitField(name="ABORT_AND_RESET", mask=0x8),
        BitField(name="TMST_STROBE", mask=0x4),
        BitField(name="FIFO_FLUSH", mask=0x2),
    ),
)

INTF_CONFIG0 = Register(
    name="INTF_CONFIG0",
    bank=0,
    address=0x4C,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="FIFO_COUNT_REC", mask=0x40),
        BitField(name="FIFO_COUNT_ENDIAN", mask=0x20),
        BitField(name="SENSOR_DATA_ENDIAN", mask=0x10),
        BitField(name="UI_SIFS_CFG", mask=0x3),
    ),
)

INTF_CONFIG1 = Register(
    name="INTF_CONFIG1",
    bank=0,
    address=0x4D,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_LP_CLK_SEL", mask=0x8),
        BitField(name="RTC_MODE", mask=0x4),
        BitField(name="CLKSEL", mask=0x3),
    ),
)

PWR_MGMT0 = Register(
    name="PWR_MGMT0",
    bank=0,
    address=0x4E,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="TEMP_DIS", mask=0x20),
        BitField(name="IDLE", mask=0x10),
        BitField(name="GYRO_MODE", mask=0xC),
        BitField(name="ACCEL_MODE", mask=0x3),
    ),
)

GYRO_CONFIG0 = Register(
    name="GYRO_CONFIG0",
    bank=0,
    address=0x4F,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="GYRO_FS_SEL", mask=0xE0),
        BitField(name="GYRO_ODR", mask=0xF),
    ),
)

ACCEL_CONFIG0 = Register(
    name="ACCEL_CONFIG0",
    bank=0,
    address=0x50,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_FS_SEL", mask=0xE0),
        BitField(name="ACCEL_ODR", mask=0xF),
    ),
)

GYRO_CONFIG1 = Register(
    name="GYRO_CONFIG1",
    bank=0,
    address=0x51,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="TEMP_FILT_BW", mask=0xE0),
        BitField(name="GYRO_UI_FILT_ORD", mask=0xC),
        BitField(name="GYRO_DEC2_M2_ORD", mask=0x3),
    ),
)

GYRO_ACCEL_CONFIG0 = Register(
    name="GYRO_ACCEL_CONFIG0",
    bank=0,
    address=0x52,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_UI_FILT_BW", mask=0xF0),
        BitField(name="GYRO_UI_FILT_BW", mask=0xF),
    ),
)

ACCEL_CONFIG1 = Register(
    name="ACCEL_CONFIG1",
    bank=0,
    address=0x53,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_UI_FILT_ORD", mask=0x18),
        BitField(name="ACCEL_DEC2_M2_ORD", mask=0x6),
    ),
)

TMST_CONFIG = Register(
    name="TMST_CONFIG",
    bank=0,
    address=0x54,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="TMST_TO_REGS_EN", mask=0x10),
        BitField(name="TMST_RES", mask=0x8),
        BitField(name="TMST_DELTA_EN", mask=0x4),
        BitField(name="TMST_FSYNC_EN", mask=0x2),
        BitField(name="TMST_EN", mask=0x1),
    ),
)

APEX_CONFIG0 = Register(
    name="APEX_CONFIG0",
    bank=0,
    address=0x56,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="DMP_POWER_SAVE", mask=0x80),
        BitField(name="TAP_ENABLE", mask=0x40),
        BitField(name="PED_ENABLE", mask=0x20),
        BitField(name="TILT_ENABLE", mask=0x10),
        BitField(name="R2W_EN", mask=0x8),
        BitField(name="DMP_ODR", mask=0x3),
    ),
)

SMD_CONFIG = Register(
    name="SMD_CONFIG",
    bank=0,
    address=0x57,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="WOM_INT_MODE", mask=0x8),
        BitField(name="WOM_MODE", mask=0x4),
        BitField(name="SMD_MODE", mask=0x3),
    ),
)

FIFO_CONFIG1 = Register(
    name="FIFO_CONFIG1",
    bank=0,
    address=0x5F,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="FIFO_RESUME_PARTIAL_RD", mask=0x40),
        BitField(name="FIFO_WM_GT_TH", mask=0x20),
        BitField(name="FIFO_HIRES_EN", mask=0x10),
        BitField(name="FIFO_TMST_FSYNC_EN", mask=0x8),
        BitField(name="FIFO_TEMP_EN", mask=0x4),
        BitField(name="FIFO_GYRO_EN", mask=0x2),
        BitField(name="FIFO_ACCEL_EN", mask=0x1),
    ),
)

FIFO_CONFIG2 = Register(
    name="FIFO_CONFIG2",
    bank=0,
    address=0x60,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_WM", mask=0xFF),),
)

FIFO_CONFIG3 = Register(
    name="FIFO_CONFIG3",
    bank=0,
    address=0x61,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_WM", mask=0xF),),
)

FSYNC_CONFIG = Register(
    name="FSYNC_CONFIG",
    bank=0,
    address=0x62,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="FSYNC_UI_SEL", mask=0x70),
        BitField(name="FSYNC_POLARITY", mask=0x1),
    ),
)

INT_CONFIG0 = Register(
    name="INT_CONFIG0",
    bank=0,
    address=0x63,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="UI_DRDY_INT_CLEAR", mask=0x30),
        BitField(name="FIFO_THS_INT_CLEAR", mask=0xC),
        BitField(name="FIFO_FULL_INT_CLEAR", mask=0x3),
    ),
)

INT_CONFIG1 = Register(
    name="INT_CONFIG1",
    bank=0,
    address=0x64,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="INT_TPULSE_DURATION", mask=0x40),
        BitField(name="INT_TDEASSERT_DISABLE", mask=0x20),
        BitField(name="INT_ASYNC_RESET", mask=0x10),
    ),
)

INT_SOURCE0 = Register(
    name="INT_SOURCE0",
    bank=0,
    address=0x65,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="UI_FSYNC_INT1_EN", mask=0x40),
        BitField(name="PLL_RDY_INT1_EN", mask=0x20),
        BitField(name="RESET_DONE_INT1_EN", mask=0x10),
        BitField(name="UI_DRDY_INT1_EN", mask=0x8),
        BitField(name="FIFO_THS_INT1_EN", mask=0x4),
        BitField(name="FIFO_FULL_INT1_EN", mask=0x2),
        BitField(name="UI_AGC_RDY_INT1_EN", mask=0x1),
    ),
)

INT_SOURCE1 = Register(
    name="INT_SOURCE1",
    bank=0,
    address=0x66,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="SMD_INT1_EN", mask=0x8),
        BitField(name="WOM_Z_INT1_EN", mask=0x4),
        BitField(name="WOM_Y_INT1_EN", mask=0x2),
        BitField(name="WOM_X_INT1_EN", mask=0x1),
    ),
)

INT_SOURCE3 = Register(
    name="INT_SOURCE3",
    bank=0,
    address=0x68,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="UI_FSYNC_INT2_EN", mask=0x40),
        BitField(name="PLL_RDY_INT2_EN", mask=0x20),
        BitField(name="RESET_DONE_INT2_EN", mask=0x10),
        BitField(name="UI_DRDY_INT2_EN", mask=0x8),
        BitField(name="FIFO_THS_INT2_EN", mask=0x4),
        BitField(name="FIFO_FULL_INT2_EN", mask=0x2),
        BitField(name="UI_AGC_RDY_INT2_EN", mask=0x1),
    ),
)

INT_SOURCE4 = Register(
    name="INT_SOURCE4",
    bank=0,
    address=0x69,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="SMD_INT2_EN", mask=0x8),
        BitField(name="WOM_Z_INT2_EN", mask=0x4),
        BitField(name="WOM_Y_INT2_EN", mask=0x2),
        BitField(name="WOM_X_INT2_EN", mask=0x1),
    ),
)

FIFO_LOST_PKT0 = Register(
    name="FIFO_LOST_PKT0",
    bank=0,
    address=0x6C,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_LOST_PKT_CNT", mask=0xFF),),
)

FIFO_LOST_PKT1 = Register(
    name="FIFO_LOST_PKT1",
    bank=0,
    address=0x6D,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="FIFO_LOST_PKT_CNT", mask=0xFF),),
)

SELF_TEST_CONFIG = Register(
    name="SELF_TEST_CONFIG",
    bank=0,
    address=0x70,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_ST_POWER", mask=0x40),
        BitField(name="EN_AZ_ST", mask=0x20),
        BitField(name="EN_AY_ST", mask=0x10),
        BitField(name="EN_AX_ST", mask=0x8),
        BitField(name="EN_GZ_ST", mask=0x4),
        BitField(name="EN_GY_ST", mask=0x2),
        BitField(name="EN_GX_ST", mask=0x1),
    ),
)

WHO_AM_I = Register(
    name="WHO_AM_I",
    bank=0,
    address=0x75,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="WHOAMI", mask=0xFF),),
)

REG_BANK_SEL = Register(
    name="REG_BANK_SEL",
    bank=0,
    address=0x76,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="ALL",
    bits=(BitField(name="BANK_SEL", mask=0x7),),
)

SENSOR_CONFIG0 = Register(
    name="SENSOR_CONFIG0",
    bank=1,
    address=0x03,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ZG_DISABLE", mask=0x20),
        BitField(name="YG_DISABLE", mask=0x10),
        BitField(name="XG_DISABLE", mask=0x8),
        BitField(name="ZA_DISABLE", mask=0x4),
        BitField(name="YA_DISABLE", mask=0x2),
        BitField(name="XA_DISABLE", mask=0x1),
    ),
)

GYRO_CONFIG_STATIC2 = Register(
    name="GYRO_CONFIG_STATIC2",
    bank=1,
    address=0x0B,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="GYRO_AAF_DIS", mask=0x2),
        BitField(name="GYRO_NF_DIS", mask=0x1),
    ),
)

GYRO_CONFIG_STATIC3 = Register(
    name="GYRO_CONFIG_STATIC3",
    bank=1,
    address=0x0C,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_AAF_DELT", mask=0x3F),),
)

GYRO_CONFIG_STATIC4 = Register(
    name="GYRO_CONFIG_STATIC4",
    bank=1,
    address=0x0D,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_AAF_DELTSQR", mask=0xFF),),
)

GYRO_CONFIG_STATIC5 = Register(
    name="GYRO_CONFIG_STATIC5",
    bank=1,
    address=0x0E,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="GYRO_AAF_BITSHIFT", mask=0xF0),
        BitField(name="GYRO_AAF_DELTSQR", mask=0xF),
    ),
)

GYRO_CONFIG_STATIC6 = Register(
    name="GYRO_CONFIG_STATIC6",
    bank=1,
    address=0x0F,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_X_NF_COSWZ", mask=0xFF),),
)

GYRO_CONFIG_STATIC7 = Register(
    name="GYRO_CONFIG_STATIC7",
    bank=1,
    address=0x10,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_Y_NF_COSWZ", mask=0xFF),),
)

GYRO_CONFIG_STATIC8 = Register(
    name="GYRO_CONFIG_STATIC8",
    bank=1,
    address=0x11,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_Z_NF_COSWZ", mask=0xFF),),
)

GYRO_CONFIG_STATIC9 = Register(
    name="GYRO_CONFIG_STATIC9",
    bank=1,
    address=0x12,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="GYRO_Z_NF_COSWZ_SEL", mask=0x20),
        BitField(name="GYRO_Y_NF_COSWZ_SEL", mask=0x10),
        BitField(name="GYRO_X_NF_COSWZ_SEL", mask=0x8),
        BitField(name="GYRO_Z_NF_COSWZ", mask=0x4),
        BitField(name="GYRO_Y_NF_COSWZ", mask=0x2),
        BitField(name="GYRO_X_NF_COSWZ", mask=0x1),
    ),
)

GYRO_CONFIG_STATIC10 = Register(
    name="GYRO_CONFIG_STATIC10",
    bank=1,
    address=0x13,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_NF_BW_SEL", mask=0x70),),
)

XG_ST_DATA = Register(
    name="XG_ST_DATA",
    bank=1,
    address=0x5F,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="XG_ST_DATA", mask=0xFF),),
)

YG_ST_DATA = Register(
    name="YG_ST_DATA",
    bank=1,
    address=0x60,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="YG_ST_DATA", mask=0xFF),),
)

ZG_ST_DATA = Register(
    name="ZG_ST_DATA",
    bank=1,
    address=0x61,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ZG_ST_DATA", mask=0xFF),),
)

TMSTVAL0 = Register(
    name="TMSTVAL0",
    bank=1,
    address=0x62,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="TMST_VALUE", mask=0xFF),),
)

TMSTVAL1 = Register(
    name="TMSTVAL1",
    bank=1,
    address=0x63,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="TMST_VALUE", mask=0xFF),),
)

TMSTVAL2 = Register(
    name="TMSTVAL2",
    bank=1,
    address=0x64,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="TMST_VALUE", mask=0xF),),
)

INTF_CONFIG4 = Register(
    name="INTF_CONFIG4",
    bank=1,
    address=0x7A,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="I3C_BUS_MODE", mask=0x40),
        BitField(name="SPI_AP_4WIRE", mask=0x2),
    ),
)

INTF_CONFIG5 = Register(
    name="INTF_CONFIG5",
    bank=1,
    address=0x7B,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="PIN9_FUNCTION", mask=0x6),),
)

INTF_CONFIG6 = Register(
    name="INTF_CONFIG6",
    bank=1,
    address=0x7C,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ASYNCTIME0_DIS", mask=0x80),
        BitField(name="I3C_EN", mask=0x10),
        BitField(name="I3C_IBI_BYTE_EN", mask=0x8),
        BitField(name="I3C_IBI_EN", mask=0x4),
        BitField(name="I3C_DDR_EN", mask=0x2),
        BitField(name="I3C_SDR_EN", mask=0x1),
    ),
)

ACCEL_CONFIG_STATIC2 = Register(
    name="ACCEL_CONFIG_STATIC2",
    bank=1,
    address=0x03,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_AAF_DELT", mask=0x7E),
        BitField(name="ACCEL_AAF_DIS", mask=0x1),
    ),
)

ACCEL_CONFIG_STATIC3 = Register(
    name="ACCEL_CONFIG_STATIC3",
    bank=1,
    address=0x04,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_AAF_DELTSQR", mask=0xFF),),
)

ACCEL_CONFIG_STATIC4 = Register(
    name="ACCEL_CONFIG_STATIC4",
    bank=1,
    address=0x05,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_AAF_BITSHIFT", mask=0xF0),
        BitField(name="ACCEL_AAF_DELTSQR", mask=0xF),
    ),
)

XA_ST_DATA = Register(
    name="XA_ST_DATA",
    bank=1,
    address=0x3B,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="XA_ST_DATA", mask=0xFF),),
)

YA_ST_DATA = Register(
    name="YA_ST_DATA",
    bank=1,
    address=0x3C,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="YA_ST_DATA", mask=0xFF),),
)

ZA_ST_DATA = Register(
    name="ZA_ST_DATA",
    bank=1,
    address=0x3D,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ZA_ST_DATA", mask=0xFF),),
)

CLKDIV = Register(
    name="CLKDIV",
    bank=2,
    address=0x2A,
    serial_if="R",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="CLKDIV", mask=0x7F),),
)

APEX_CONFIG1 = Register(
    name="APEX_CONFIG1",
    bank=3,
    address=0x40,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="LOW_ENERGY_AMP_TH_SEL", mask=0xF0),),
)

APEX_CONFIG2 = Register(
    name="APEX_CONFIG2",
    bank=3,
    address=0x41,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="PED_AMP_TH_SEL", mask=0xF0),
        BitField(name="PED_STEP_CNT_TH_SEL", mask=0xF),
    ),
)

APEX_CONFIG3 = Register(
    name="APEX_CONFIG3",
    bank=3,
    address=0x42,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="PED_STEP_DET_TH_SEL", mask=0xE0),
        BitField(name="PED_SB_TIMER_TH_SEL", mask=0x1C),
        BitField(name="PED_HI_EN_TH_SEL", mask=0x3),
    ),
)

APEX_CONFIG4 = Register(
    name="APEX_CONFIG4",
    bank=3,
    address=0x43,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="TILT_WAIT_TIME_SEL", mask=0xC0),
        BitField(name="SLEEP_TIME_OUT", mask=0x38),
    ),
)

APEX_CONFIG5 = Register(
    name="APEX_CONFIG5",
    bank=3,
    address=0x44,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="MOUNTING_MATRIX", mask=0x7),),
)

APEX_CONFIG6 = Register(
    name="APEX_CONFIG6",
    bank=3,
    address=0x45,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="SLEEP_GESTURE_DELAY", mask=0x7),),
)

APEX_CONFIG7 = Register(
    name="APEX_CONFIG7",
    bank=3,
    address=0x46,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="TAP_MIN_JERK_THR", mask=0xFC),
        BitField(name="TAP_MAX_PEAK_TOL", mask=0x3),
    ),
)

APEX_CONFIG8 = Register(
    name="APEX_CONFIG8",
    bank=3,
    address=0x47,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="TAP_TMAX", mask=0x60),
        BitField(name="TAP_TAVG", mask=0x18),
        BitField(name="TAP_TMIN", mask=0x7),
    ),
)

APEX_CONFIG9 = Register(
    name="APEX_CONFIG9",
    bank=3,
    address=0x48,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="SENSITIVITY_MODE", mask=0x1),),
)

ACCEL_WOM_X_THR = Register(
    name="ACCEL_WOM_X_THR",
    bank=3,
    address=0x4A,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="WOM_X_TH", mask=0xFF),),
)

ACCEL_WOM_Y_THR = Register(
    name="ACCEL_WOM_Y_THR",
    bank=3,
    address=0x4B,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="WOM_Y_TH", mask=0xFF),),
)

ACCEL_WOM_Z_THR = Register(
    name="ACCEL_WOM_Z_THR",
    bank=3,
    address=0x4C,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="WOM_Z_TH", mask=0xFF),),
)

INT_SOURCE6 = Register(
    name="INT_SOURCE6",
    bank=3,
    address=0x4D,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="STEP_DET_INT1_EN", mask=0x20),
        BitField(name="STEP_CNT_OFL_INT1_EN", mask=0x10),
        BitField(name="TILT_DET_INT1_EN", mask=0x8),
        BitField(name="WAKE_DET_INT1_EN", mask=0x4),
        BitField(name="SLEEP_DET_INT1_EN", mask=0x2),
        BitField(name="TAP_DET_INT1_EN", mask=0x1),
    ),
)

INT_SOURCE7 = Register(
    name="INT_SOURCE7",
    bank=3,
    address=0x4E,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="STEP_DET_INT2_EN", mask=0x20),
        BitField(name="STEP_CNT_OFL_INT2_EN", mask=0x10),
        BitField(name="TILT_DET_INT2_EN", mask=0x8),
        BitField(name="WAKE_DET_INT2_EN", mask=0x4),
        BitField(name="SLEEP_DET_INT2_EN", mask=0x2),
        BitField(name="TAP_DET_INT2_EN", mask=0x1),
    ),
)

INT_SOURCE8 = Register(
    name="INT_SOURCE8",
    bank=3,
    address=0x4F,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="FSYNC_IBI_EN", mask=0x20),
        BitField(name="PLL_RDY_IBI_EN", mask=0x10),
        BitField(name="UI_DRDY_IBI_EN", mask=0x8),
        BitField(name="FIFO_THS_IBI_EN", mask=0x4),
        BitField(name="FIFO_FULL_IBI_EN", mask=0x2),
        BitField(name="AGC_RDY_IBI_EN", mask=0x1),
    ),
)

INT_SOURCE9 = Register(
    name="INT_SOURCE9",
    bank=3,
    address=0x50,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="SMD_IBI_EN", mask=0x10),
        BitField(name="WOM_Z_IBI_EN", mask=0x8),
        BitField(name="WOM_Y_IBI_EN", mask=0x4),
        BitField(name="WOM_X_IBI_EN", mask=0x2),
    ),
)

INT_SOURCE10 = Register(
    name="INT_SOURCE10",
    bank=3,
    address=0x51,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="STEP_DET_IBI_EN", mask=0x20),
        BitField(name="STEP_CNT_OFL_IBI_EN", mask=0x10),
        BitField(name="TILT_DET_IBI_EN", mask=0x8),
        BitField(name="WAKE_DET_IBI_EN", mask=0x4),
        BitField(name="SLEEP_DET_IBI_EN", mask=0x2),
        BitField(name="TAP_DET_IBI_EN", mask=0x1),
    ),
)

OFFSET_USER0 = Register(
    name="OFFSET_USER0",
    bank=3,
    address=0x77,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_X_OFFUSER", mask=0xFF),),
)

OFFSET_USER1 = Register(
    name="OFFSET_USER1",
    bank=3,
    address=0x78,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="GYRO_Y_OFFUSER", mask=0xF0),
        BitField(name="GYRO_X_OFFUSER", mask=0xF),
    ),
)

OFFSET_USER2 = Register(
    name="OFFSET_USER2",
    bank=3,
    address=0x79,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_Y_OFFUSER", mask=0xFF),),
)

OFFSET_USER3 = Register(
    name="OFFSET_USER3",
    bank=3,
    address=0x7A,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="GYRO_Z_OFFUSER", mask=0xFF),),
)

OFFSET_USER4 = Register(
    name="OFFSET_USER4",
    bank=3,
    address=0x7B,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_X_OFFUSER", mask=0xF0),
        BitField(name="GYRO_Z_OFFUSER", mask=0xF),
    ),
)

OFFSET_USER5 = Register(
    name="OFFSET_USER5",
    bank=3,
    address=0x7C,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_X_OFFUSER", mask=0xFF),),
)

OFFSET_USER6 = Register(
    name="OFFSET_USER6",
    bank=3,
    address=0x7D,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_Y_OFFUSER", mask=0xFF),),
)

OFFSET_USER7 = Register(
    name="OFFSET_USER7",
    bank=3,
    address=0x7E,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(
        BitField(name="ACCEL_Z_OFFUSER", mask=0xF0),
        BitField(name="ACCEL_Y_OFFUSER", mask=0xF),
    ),
)

OFFSET_USER8 = Register(
    name="OFFSET_USER8",
    bank=3,
    address=0x7F,
    serial_if="R/W",
    reset_value=0x00,
    clock_domain="SCLK_UI",
    bits=(BitField(name="ACCEL_Z_OFFUSER", mask=0xFF),),
)


# Hardcoded reverse lookup table
REVERSE_LOOKUP = {
    (0, 0x11): DEVICE_CONFIG,
    (0, 0x13): DRIVE_CONFIG,
    (0, 0x14): INT_CONFIG,
    (0, 0x16): FIFO_CONFIG,
    (0, 0x1D): TEMP_DATA1,
    (0, 0x1E): TEMP_DATA0,
    (0, 0x1F): ACCEL_DATA_X1,
    (0, 0x20): ACCEL_DATA_X0,
    (0, 0x21): ACCEL_DATA_Y1,
    (0, 0x22): ACCEL_DATA_Y0,
    (0, 0x23): ACCEL_DATA_Z1,
    (0, 0x24): ACCEL_DATA_Z0,
    (0, 0x25): GYRO_DATA_X1,
    (0, 0x26): GYRO_DATA_X0,
    (0, 0x27): GYRO_DATA_Y1,
    (0, 0x28): GYRO_DATA_Y0,
    (0, 0x29): GYRO_DATA_Z1,
    (0, 0x2A): GYRO_DATA_Z0,
    (0, 0x2B): TMST_FSYNCH,
    (0, 0x2C): TMST_FSYNCL,
    (0, 0x2D): INT_STATUS,
    (0, 0x2E): FIFO_COUNTH,
    (0, 0x2F): FIFO_COUNTL,
    (0, 0x30): FIFO_DATA,
    (0, 0x31): APEX_DATA0,
    (0, 0x32): APEX_DATA1,
    (0, 0x33): APEX_DATA2,
    (0, 0x34): APEX_DATA3,
    (0, 0x35): APEX_DATA4,
    (0, 0x36): APEX_DATA5,
    (0, 0x37): INT_STATUS2,
    (0, 0x38): INT_STATUS3,
    (0, 0x4B): SIGNAL_PATH_RESET,
    (0, 0x4C): INTF_CONFIG0,
    (0, 0x4D): INTF_CONFIG1,
    (0, 0x4E): PWR_MGMT0,
    (0, 0x4F): GYRO_CONFIG0,
    (0, 0x50): ACCEL_CONFIG0,
    (0, 0x51): GYRO_CONFIG1,
    (0, 0x52): GYRO_ACCEL_CONFIG0,
    (0, 0x53): ACCEL_CONFIG1,
    (0, 0x54): TMST_CONFIG,
    (0, 0x56): APEX_CONFIG0,
    (0, 0x57): SMD_CONFIG,
    (0, 0x5F): FIFO_CONFIG1,
    (0, 0x60): FIFO_CONFIG2,
    (0, 0x61): FIFO_CONFIG3,
    (0, 0x62): FSYNC_CONFIG,
    (0, 0x63): INT_CONFIG0,
    (0, 0x64): INT_CONFIG1,
    (0, 0x65): INT_SOURCE0,
    (0, 0x66): INT_SOURCE1,
    (0, 0x68): INT_SOURCE3,
    (0, 0x69): INT_SOURCE4,
    (0, 0x6C): FIFO_LOST_PKT0,
    (0, 0x6D): FIFO_LOST_PKT1,
    (0, 0x70): SELF_TEST_CONFIG,
    (0, 0x75): WHO_AM_I,
    (0, 0x76): REG_BANK_SEL,
    (1, 0x03): ACCEL_CONFIG_STATIC2,
    (1, 0x0B): GYRO_CONFIG_STATIC2,
    (1, 0x0C): GYRO_CONFIG_STATIC3,
    (1, 0x0D): GYRO_CONFIG_STATIC4,
    (1, 0x0E): GYRO_CONFIG_STATIC5,
    (1, 0x0F): GYRO_CONFIG_STATIC6,
    (1, 0x10): GYRO_CONFIG_STATIC7,
    (1, 0x11): GYRO_CONFIG_STATIC8,
    (1, 0x12): GYRO_CONFIG_STATIC9,
    (1, 0x13): GYRO_CONFIG_STATIC10,
    (1, 0x5F): XG_ST_DATA,
    (1, 0x60): YG_ST_DATA,
    (1, 0x61): ZG_ST_DATA,
    (1, 0x62): TMSTVAL0,
    (1, 0x63): TMSTVAL1,
    (1, 0x64): TMSTVAL2,
    (1, 0x7A): INTF_CONFIG4,
    (1, 0x7B): INTF_CONFIG5,
    (1, 0x7C): INTF_CONFIG6,
    (1, 0x04): ACCEL_CONFIG_STATIC3,
    (1, 0x05): ACCEL_CONFIG_STATIC4,
    (1, 0x3B): XA_ST_DATA,
    (1, 0x3C): YA_ST_DATA,
    (1, 0x3D): ZA_ST_DATA,
    (2, 0x2A): CLKDIV,
    (3, 0x40): APEX_CONFIG1,
    (3, 0x41): APEX_CONFIG2,
    (3, 0x42): APEX_CONFIG3,
    (3, 0x43): APEX_CONFIG4,
    (3, 0x44): APEX_CONFIG5,
    (3, 0x45): APEX_CONFIG6,
    (3, 0x46): APEX_CONFIG7,
    (3, 0x47): APEX_CONFIG8,
    (3, 0x48): APEX_CONFIG9,
    (3, 0x4A): ACCEL_WOM_X_THR,
    (3, 0x4B): ACCEL_WOM_Y_THR,
    (3, 0x4C): ACCEL_WOM_Z_THR,
    (3, 0x4D): INT_SOURCE6,
    (3, 0x4E): INT_SOURCE7,
    (3, 0x4F): INT_SOURCE8,
    (3, 0x50): INT_SOURCE9,
    (3, 0x51): INT_SOURCE10,
    (3, 0x77): OFFSET_USER0,
    (3, 0x78): OFFSET_USER1,
    (3, 0x79): OFFSET_USER2,
    (3, 0x7A): OFFSET_USER3,
    (3, 0x7B): OFFSET_USER4,
    (3, 0x7C): OFFSET_USER5,
    (3, 0x7D): OFFSET_USER6,
    (3, 0x7E): OFFSET_USER7,
    (3, 0x7F): OFFSET_USER8,
}


# List of all registers
ALL_REGISTERS = [
    DEVICE_CONFIG,
    DRIVE_CONFIG,
    INT_CONFIG,
    FIFO_CONFIG,
    TEMP_DATA1,
    TEMP_DATA0,
    ACCEL_DATA_X1,
    ACCEL_DATA_X0,
    ACCEL_DATA_Y1,
    ACCEL_DATA_Y0,
    ACCEL_DATA_Z1,
    ACCEL_DATA_Z0,
    GYRO_DATA_X1,
    GYRO_DATA_X0,
    GYRO_DATA_Y1,
    GYRO_DATA_Y0,
    GYRO_DATA_Z1,
    GYRO_DATA_Z0,
    TMST_FSYNCH,
    TMST_FSYNCL,
    INT_STATUS,
    FIFO_COUNTH,
    FIFO_COUNTL,
    FIFO_DATA,
    APEX_DATA0,
    APEX_DATA1,
    APEX_DATA2,
    APEX_DATA3,
    APEX_DATA4,
    APEX_DATA5,
    INT_STATUS2,
    INT_STATUS3,
    SIGNAL_PATH_RESET,
    INTF_CONFIG0,
    INTF_CONFIG1,
    PWR_MGMT0,
    GYRO_CONFIG0,
    ACCEL_CONFIG0,
    GYRO_CONFIG1,
    GYRO_ACCEL_CONFIG0,
    ACCEL_CONFIG1,
    TMST_CONFIG,
    APEX_CONFIG0,
    SMD_CONFIG,
    FIFO_CONFIG1,
    FIFO_CONFIG2,
    FIFO_CONFIG3,
    FSYNC_CONFIG,
    INT_CONFIG0,
    INT_CONFIG1,
    INT_SOURCE0,
    INT_SOURCE1,
    INT_SOURCE3,
    INT_SOURCE4,
    FIFO_LOST_PKT0,
    FIFO_LOST_PKT1,
    SELF_TEST_CONFIG,
    WHO_AM_I,
    REG_BANK_SEL,
    SENSOR_CONFIG0,
    GYRO_CONFIG_STATIC2,
    GYRO_CONFIG_STATIC3,
    GYRO_CONFIG_STATIC4,
    GYRO_CONFIG_STATIC5,
    GYRO_CONFIG_STATIC6,
    GYRO_CONFIG_STATIC7,
    GYRO_CONFIG_STATIC8,
    GYRO_CONFIG_STATIC9,
    GYRO_CONFIG_STATIC10,
    XG_ST_DATA,
    YG_ST_DATA,
    ZG_ST_DATA,
    TMSTVAL0,
    TMSTVAL1,
    TMSTVAL2,
    INTF_CONFIG4,
    INTF_CONFIG5,
    INTF_CONFIG6,
    ACCEL_CONFIG_STATIC2,
    ACCEL_CONFIG_STATIC3,
    ACCEL_CONFIG_STATIC4,
    XA_ST_DATA,
    YA_ST_DATA,
    ZA_ST_DATA,
    CLKDIV,
    APEX_CONFIG1,
    APEX_CONFIG2,
    APEX_CONFIG3,
    APEX_CONFIG4,
    APEX_CONFIG5,
    APEX_CONFIG6,
    APEX_CONFIG7,
    APEX_CONFIG8,
    APEX_CONFIG9,
    ACCEL_WOM_X_THR,
    ACCEL_WOM_Y_THR,
    ACCEL_WOM_Z_THR,
    INT_SOURCE6,
    INT_SOURCE7,
    INT_SOURCE8,
    INT_SOURCE9,
    INT_SOURCE10,
    OFFSET_USER0,
    OFFSET_USER1,
    OFFSET_USER2,
    OFFSET_USER3,
    OFFSET_USER4,
    OFFSET_USER5,
    OFFSET_USER6,
    OFFSET_USER7,
    OFFSET_USER8,
]
