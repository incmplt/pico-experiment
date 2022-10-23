# MicroPython for Rapperry Pi Pico
# -*- coding: utf-8 -*-
import utime

class ST7032():
    def __init__(self, i2c, addr=0x3e):
        self.i2c = i2c
        self.addr = addr
        self.buf = bytearray(2)
        self.initDisplay()

    def writeCmd(self, cmd):
        self.buf[0] = 0x00
        self.buf[1] = cmd
        self.i2c.writeto(self.addr, self.buf)

    def writeData(self, char):
        self.buf[0] = 0x40
        self.buf[1] = char
        self.i2c.writeto(self.addr, self.buf)

    def initDisplay(self):
        self.i2c.writeto(self.addr, b'\x00\x38')
        self.i2c.writeto(self.addr, b'\x00\x39')
        self.i2c.writeto(self.addr, b'\x00\x14')
        self.i2c.writeto(self.addr, b'\x00\x73')
        self.i2c.writeto(self.addr, b'\x00\x56')
        self.i2c.writeto(self.addr, b'\x00\x6c')
        self.i2c.writeto(self.addr, b'\x00\x38')
        self.i2c.writeto(self.addr, b'\x00\x0C')
        self.i2c.writeto(self.addr, b'\x00\x01')

    def clear(self):
        self.writeCmd(0x01)
        utime.sleep(0.01)
        self.writeCmd(0x02)
        utime.sleep(0.01)

    def home(self):
        self.write_cmd(0x02)
        utime.sleep(0.01)

    def setContrast(self, contrast):
        if contrast < 0:
            contrast = 0
        if contrast > 0x0f:
            contrast = 0x0f
        self.writeCmd(0x39)
        self.writeCmd(0x70 + contrast)

    def setCursor(self, x, y):
        if x < 0: x = 0
        if y < 0: y = 0
        addr = y * 0x40 + x
        self.writeCmd(0x80 + addr)

    def print(self, str):
        for c in str:
            self.writeData(ord(c))

