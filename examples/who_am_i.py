import click

from imu_icm42688p.comm import Spi
from imu_icm42688p.imu import Imu
from imu_icm42688p.registers import WHO_AM_I


@click.command()
@click.option("--spi-device", required=True, type=int, help="SPI device number, e.g., 0 or 1")
def who_am_i(spi_device):
    spi = Spi(device=spi_device)
    imu = Imu(spi)
    device_id = imu.read(WHO_AM_I)[0]
    if device_id is not None:
        click.echo(f"ICM-42688-P WHO_AM_I device ID: 0x{device_id:02X}")
    else:
        click.echo("Failed to read WHO_AM_I")


if __name__ == "__main__":
    who_am_i()
