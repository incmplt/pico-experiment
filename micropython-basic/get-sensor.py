import machine
import utime

sensor = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    tempval = sensor.read_u16() * conversion_factor
    temperature = 27 - (tempval - 0.706)/0.001721
    print(temperature)
    utime.sleep(5)