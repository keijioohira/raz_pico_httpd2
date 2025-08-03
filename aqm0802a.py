import time

class AQM0802A:
    def __init__(self, i2c, addr=0x3E):
        self.i2c = i2c
        self.addr = addr
        self.init_display()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, b'\x00' + bytes([cmd]))

    def write_data(self, data):
        self.i2c.writeto(self.addr, b'\x40' + data.encode('utf-8'))

    def init_display(self):
        for cmd in [0x38, 0x39, 0x14, 0x70, 0x56, 0x6C]:
            self.write_cmd(cmd)
            time.sleep(0.05)
        self.write_cmd(0x38)
        self.write_cmd(0x0C)
        self.write_cmd(0x01)
        time.sleep(0.05)

    def clear(self):
        self.write_cmd(0x01)
        time.sleep(0.05)

    def write(self, text):
        self.write_data(text[:8])

    def set_cursor(self, col, row):
        addr = 0x00 if row == 0 else 0x40
        self.write_cmd(0x80 | (addr + col))
