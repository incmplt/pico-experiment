# MicroPython for Rapperry Pi Pico
# -*- coding: utf-8 -*-
from machine import Pin, I2C

i2c0 = I2C(0)
addr = i2c0.scan()
print(i2c0)
print("Address is:"+str(addr))

i2c1 = I2C(1)
addr = i2c1.scan()
print(i2c1)
print("Address is:"+str(addr))

