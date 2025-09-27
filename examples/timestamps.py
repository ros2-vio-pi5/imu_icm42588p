import time

import click

from imu_icm42688p.comm import Spi
from imu_icm42688p.imu import Imu
from imu_icm42688p.registers import (
    ACCEL_CONFIG0,
    GYRO_CONFIG0,
    INTF_CONFIG1,
    INTF_CONFIG5,
    PWR_MGMT0,
    SIGNAL_PATH_RESET,
    TMST_CONFIG,
    TMSTVAL0,
    TMSTVAL1,
    TMSTVAL2,
)


def pretty_print_register(register, value):
    click.echo(f"{register.name} (0x{register.address:02X}): 0x{value:02X}")
    for bitfield in register.bits:
        bit_val = value & bitfield.mask
        click.echo(f"  {bitfield.name.ljust(20)}  0x{bit_val:02X}      0b{bit_val:08b}")


def read_16bit_registers(imu, msb_reg, lsb_reg):
    msb = imu.read(msb_reg)[0]
    lsb = imu.read(lsb_reg)[0]
    value = (msb << 8) | lsb
    if value & 0x8000:  # Convert to signed 16-bit
        value -= 0x10000
    return value


def enable_sensors(imu):
    pwr_mgmt_value = (3 << 0) | (3 << 2) | (0 << 5)
    imu.write_masked(
        PWR_MGMT0,
        pwr_mgmt_value,
        PWR_MGMT0.get_bit("TEMP_DIS").mask | PWR_MGMT0.get_bit("GYRO_MODE").mask | PWR_MGMT0.get_bit("ACCEL_MODE").mask,
    )
    click.echo("Enabled sensors")


def enable_external_clock(imu):
    imu.write_masked(
        INTF_CONFIG1,
        INTF_CONFIG1.get_bit("RTC_MODE").mask | 0b00,
        INTF_CONFIG1.get_bit("ACCEL_LP_CLK_SEL").mask
        | INTF_CONFIG1.get_bit("RTC_MODE").mask
        | INTF_CONFIG1.get_bit("CLKSEL").mask,
    )
    click.echo("Configured INTF_CONFIG1 for external clock")

    pin9_func_value = 0b10 << 1
    imu.write_masked(INTF_CONFIG5, pin9_func_value, INTF_CONFIG5.get_bit("PIN9_FUNCTION").mask)
    click.echo("Configured INTF_CONFIG5 PIN9_FUNCTION to CLKIN for external clock on pin 9")


def setup_baseline(imu):
    click.echo("Performing baseline setup...")

    imu.reset()
    imu.wait_for_reset_done()
    click.echo("Device reset completed")

    imu.write(TMST_CONFIG, 0x00)

    odr_value = 0b0111
    imu.write_masked(GYRO_CONFIG0, odr_value, GYRO_CONFIG0.get_bit("GYRO_ODR").mask)
    imu.write_masked(ACCEL_CONFIG0, odr_value, ACCEL_CONFIG0.get_bit("ACCEL_ODR").mask)

    click.echo("---")


def poll_data(imu, poll_count, poll_interval):
    enable_sensors(imu)
    time.sleep(0.01)

    for i in range(poll_count):
        imu.write_masked(
            SIGNAL_PATH_RESET,
            SIGNAL_PATH_RESET.get_bit("TMST_STROBE").mask,
            SIGNAL_PATH_RESET.get_bit("TMST_STROBE").mask,
        )
        click.echo("Timestamp strobe set")

        val0 = imu.read(TMSTVAL0)[0]
        val1 = imu.read(TMSTVAL1)[0]
        val2 = imu.read(TMSTVAL2)[0] & TMSTVAL2.get_bit("TMST_VALUE").mask
        timestamp = (val2 << 16) | (val1 << 8) | val0
        click.echo(f"Timestamp {i + 1}: {timestamp}")

        time.sleep(poll_interval)


@click.command()
@click.option("--spi-device", required=True, type=int, help="SPI device number, e.g., 0 or 1")
@click.option("--poll-interval", default=0.001, type=float, help="Polling interval in seconds")
@click.option("--poll-count", default=5, type=int, help="Number of timestamp polls")
def timestamp_test(spi_device, poll_interval, poll_count):
    spi = Spi(device=spi_device)
    imu = Imu(spi)

    ###
    ###
    ###

    click.echo("\n\n===\n baseline scenario\n===")
    setup_baseline(imu)

    value = imu.read(TMST_CONFIG)[0]
    pretty_print_register(TMST_CONFIG, value)

    click.echo("---")
    poll_data(imu, poll_count, poll_interval)

    ###
    ###
    ###

    click.echo("\n\n===\n scenario TMST_EN set\n===")
    setup_baseline(imu)
    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_EN").mask,
        TMST_CONFIG.get_bit("TMST_EN").mask,
    )
    click.echo("TMST_EN bit set")

    value = imu.read(TMST_CONFIG)[0]
    pretty_print_register(TMST_CONFIG, value)

    click.echo("---")
    poll_data(imu, poll_count, poll_interval)

    ###
    ###
    ###

    click.echo("\n\n===\n scenario TMST_EN set, TMST_TO_REGS_EN set\n===")
    setup_baseline(imu)

    imu.write_masked(TMST_CONFIG, TMST_CONFIG.get_bit("TMST_EN").mask, TMST_CONFIG.get_bit("TMST_EN").mask)
    click.echo("TMST_EN bit set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
    )
    click.echo("TMST_TO_REGS_EN bits set")

    value = imu.read(TMST_CONFIG)[0]
    pretty_print_register(TMST_CONFIG, value)

    click.echo("---")
    poll_data(imu, poll_count, poll_interval)

    ###
    ###
    ###

    click.echo("\n\n===\n scenario TMST_EN set, TMST_TO_REGS_EN set, TMST_RES set\n===")
    setup_baseline(imu)

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_EN").mask,
        TMST_CONFIG.get_bit("TMST_EN").mask,
    )
    click.echo("TMST_EN bit set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
    )
    click.echo("TMST_TO_REGS_EN bits set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_RES").mask,
        TMST_CONFIG.get_bit("TMST_RES").mask,
    )
    click.echo("TMST_RES bits set")

    value = imu.read(TMST_CONFIG)[0]
    pretty_print_register(TMST_CONFIG, value)

    click.echo("---")
    poll_data(imu, poll_count, poll_interval)

    ###
    ###
    ###

    click.echo("\n\n===\n scenario TMST_EN set, TMST_TO_REGS_EN set, TMST_RES set, TMST_DELTA_EN set\n===")
    setup_baseline(imu)

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_EN").mask,
        TMST_CONFIG.get_bit("TMST_EN").mask,
    )
    click.echo("TMST_EN bit set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
    )
    click.echo("TMST_TO_REGS_EN bits set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_RES").mask,
        TMST_CONFIG.get_bit("TMST_RES").mask,
    )
    click.echo("TMST_RES bits set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_DELTA_EN").mask,
        TMST_CONFIG.get_bit("TMST_DELTA_EN").mask,
    )
    click.echo("TMST_DELTA_EN bits set")

    tmst_config_value = imu.read(TMST_CONFIG)[0]
    pretty_print_register(TMST_CONFIG, tmst_config_value)

    click.echo("---")
    poll_data(imu, poll_count, poll_interval)

    ###
    ###
    ###

    click.echo(
        "\n\n===\n scenario TMST_EN set, TMST_TO_REGS_EN set, TMST_RES set, TMST_DELTA_EN set, enable external clock source\n==="
    )
    setup_baseline(imu)

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_EN").mask,
        TMST_CONFIG.get_bit("TMST_EN").mask,
    )
    click.echo("TMST_EN bit set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
        TMST_CONFIG.get_bit("TMST_TO_REGS_EN").mask,
    )
    click.echo("TMST_TO_REGS_EN bits set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_RES").mask,
        TMST_CONFIG.get_bit("TMST_RES").mask,
    )
    click.echo("TMST_RES bits set")

    imu.write_masked(
        TMST_CONFIG,
        TMST_CONFIG.get_bit("TMST_DELTA_EN").mask,
        TMST_CONFIG.get_bit("TMST_DELTA_EN").mask,
    )
    click.echo("TMST_DELTA_EN bits set")

    enable_external_clock(imu)

    tmst_config_value = imu.read(TMST_CONFIG)[0]
    pretty_print_register(TMST_CONFIG, tmst_config_value)

    click.echo("---")
    poll_data(imu, poll_count, poll_interval)


if __name__ == "__main__":
    timestamp_test()
