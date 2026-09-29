from lcd_api import LcdApi
from time import sleep_ms

MASK_RS = 0x01
MASK_E = 0x04

SHIFT_BACKLIGHT = 3
SHIFT_DATA = 4

class I2cLcd(LcdApi):

    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr

        self.i2c.writeto(self.i2c_addr, bytearray([0]))
        sleep_ms(20)

        self.hal_write_init_nibble(0x30)
        sleep_ms(5)

        self.hal_write_init_nibble(0x30)
        sleep_ms(1)

        self.hal_write_init_nibble(0x30)
        sleep_ms(1)

        self.hal_write_init_nibble(0x20)
        sleep_ms(1)

        LcdApi.__init__(self, num_lines, num_columns)

        self.hal_write_command(0x28)
        self.hal_write_command(0x0C)
        self.hal_write_command(0x06)

        self.clear()

    def hal_write_init_nibble(self, nibble):
        byte = ((nibble >> 4) << SHIFT_DATA) | (1 << SHIFT_BACKLIGHT)

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte | MASK_E])
        )

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte])
        )

    def hal_write_command(self, cmd):
        byte = (
            ((cmd >> 4) & 0x0F) << SHIFT_DATA
        ) | (1 << SHIFT_BACKLIGHT)

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte | MASK_E])
        )

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte])
        )

        byte = (
            (cmd & 0x0F) << SHIFT_DATA
        ) | (1 << SHIFT_BACKLIGHT)

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte | MASK_E])
        )

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte])
        )

    def hal_write_data(self, data):
        byte = (
            MASK_RS |
            (((data >> 4) & 0x0F) << SHIFT_DATA) |
            (1 << SHIFT_BACKLIGHT)
        )

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte | MASK_E])
        )

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte])
        )

        byte = (
            MASK_RS |
            ((data & 0x0F) << SHIFT_DATA) |
            (1 << SHIFT_BACKLIGHT)
        )

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte | MASK_E])
        )

        self.i2c.writeto(
            self.i2c_addr,
            bytearray([byte])
        )
