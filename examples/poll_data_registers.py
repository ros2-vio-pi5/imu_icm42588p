import time

import click

from imu_icm42688p.comm import Spi
from imu_icm42688p.imu import Imu
from imu_icm42688p.registers import (
    ACCEL_CONFIG0,
    ACCEL_DATA_X0,
    ACCEL_DATA_X1,
    ACCEL_DATA_Y0,
    ACCEL_DATA_Y1,
    ACCEL_DATA_Z0,
    ACCEL_DATA_Z1,
    GYRO_CONFIG0,
    GYRO_DATA_X0,
    GYRO_DATA_X1,
    GYRO_DATA_Y0,
    GYRO_DATA_Y1,
    GYRO_DATA_Z0,
    GYRO_DATA_Z1,
    PWR_MGMT0,
    TEMP_DATA0,
    TEMP_DATA1,
)


def pretty_print_register(register, value):
    click.echo(f"{register.name} (0x{register.address:02X}): 0x{value:02X}")
    for bitfield in register.bits:
        bit_val = value & bitfield.mask
        click.echo(f"  {bitfield.name.ljust(20)}  0x{bit_val:02X}      0b{bit_val:08b}")


def enable_sensors(imu):
    pwr_mgmt_value = (3 << 0) | (3 << 2) | (0 << 5)
    imu.write_masked(
        PWR_MGMT0,
        pwr_mgmt_value,
        PWR_MGMT0.get_bit("TEMP_DIS").mask | PWR_MGMT0.get_bit("GYRO_MODE").mask | PWR_MGMT0.get_bit("ACCEL_MODE").mask,
    )
    click.echo("Enabled sensors")


def setup_odr(imu):
    odr_value = 0b0111
    imu.write_masked(GYRO_CONFIG0, odr_value, GYRO_CONFIG0.get_bit("GYRO_ODR").mask)
    imu.write_masked(ACCEL_CONFIG0, odr_value, ACCEL_CONFIG0.get_bit("ACCEL_ODR").mask)
    click.echo(f"Set gyro and accel ODR to 0b{odr_value:04b}")


def reset_imu(imu):
    imu.reset()
    imu.wait_for_reset_done()
    click.echo("Device reset completed")


def read_16bit_registers(imu, msb_reg, lsb_reg):
    msb = imu.read(msb_reg)[0]
    lsb = imu.read(lsb_reg)[0]
    value = (msb << 8) | lsb
    if value & 0x8000:
        value -= 0x10000
    return value


def poll_data(imu, poll_count, poll_interval):
    enable_sensors(imu)
    setup_odr(imu)
    time.sleep(0.01)

    for i in range(poll_count):
        temp_raw = read_16bit_registers(imu, TEMP_DATA1, TEMP_DATA0)
        click.echo(f"Temperature raw: {temp_raw}")

        accel_x = read_16bit_registers(imu, ACCEL_DATA_X1, ACCEL_DATA_X0)
        accel_y = read_16bit_registers(imu, ACCEL_DATA_Y1, ACCEL_DATA_Y0)
        accel_z = read_16bit_registers(imu, ACCEL_DATA_Z1, ACCEL_DATA_Z0)
        click.echo(f"Accel raw: X={accel_x}, Y={accel_y}, Z={accel_z}")

        gyro_x = read_16bit_registers(imu, GYRO_DATA_X1, GYRO_DATA_X0)
        gyro_y = read_16bit_registers(imu, GYRO_DATA_Y1, GYRO_DATA_Y0)
        gyro_z = read_16bit_registers(imu, GYRO_DATA_Z1, GYRO_DATA_Z0)
        click.echo(f"Gyro raw: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

        time.sleep(poll_interval)


@click.command()
@click.option("--spi-device", required=True, type=int, help="SPI device number, e.g., 0 or 1")
@click.option("--poll-interval", default=0.01, type=float, help="Polling interval in seconds")
@click.option("--poll-count", default=50, type=int, help="Number of timestamp polls")
def run(spi_device, poll_interval, poll_count):
    spi = Spi(device=spi_device)
    imu = Imu(spi)

    reset_imu(imu)
    poll_data(imu, poll_count, poll_interval)


if __name__ == "__main__":
    run()
