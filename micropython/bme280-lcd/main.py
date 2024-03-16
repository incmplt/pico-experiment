# MicroPython for Rapperry Pi Pico
# -*- coding: utf-8 -*-
import utime
from machine import Pin, I2C, ADC
# ST7032.py : Class ST7032
from ST7032 import ST7032
# BME280
import bme280

# sensor_pos : 0=indoor, 1=Outdoors 
sensor_pos = 1

if __name__ == '__main__':
    sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
    conversion_factor = 3.3 / (65535)
    utime.sleep(5)
    #pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    #sensor = DHT11( pin )

    i2c=I2C(0, scl=Pin(17), sda=Pin(16), freq=100000)
    bme = bme280.BME280(i2c=i2c)
    
    lcd = ST7032(i2c) 
    lcd.setContrast(1)
    lcd.clear()
    while True:
        reading = sensor_temp.read_u16() * conversion_factor
        # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected tothe fifth ADC channel
        # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
        temperature = 27 - (reading - 0.706)/0.001721
        tempStr = "  {:5.1f}C".format(temperature)
        #lcd.setCursor(0, 0)
        #lcd.print('Temp:')
        #lcd.setCursor(0, 1)
        #lcd.print(tempStr)
        #print( bme.values )
        t,p,h= bme.read_compensated_data()
        t1 = int(t/100 + 0.5)
        h1 = int(h/1024 + 0.5)
        #p = p//256
        #p1 = int(p/100 + 0.5)

        t1Str = "T:{:5.1f}C".format(t1)
        h1Str = "H:{:5.1f}%".format(h1)

        lcd.setCursor(0, 0)
        lcd.print(t1Str)
        lcd.setCursor(0, 1)
        lcd.print(h1Str)
        #print( tempStr )
        print(t1Str)
        print(h1Str)
        utime.sleep(3)
        
        # WBGT
        if sensor_pos == 1:
            # indoor sensor
            wbgt = round( float( t1 *0.725 + h1 *0.0368 + 0.00364* t1 * h1 - 3.246 ), 2 )
        else:
            # outdoors sensor
            wbgt = round( float( t1 *0.735 + h1 *0.0374 + 0.00292* t1 * h1 - 4.064 ), 2 )
        lcd.setCursor(0, 0)
        lcd.print("WBGT:   ")
        lcd.setCursor(0, 1)
        wbgtStr = "W:{:5.1f}C".format( wbgt )
        lcd.print( wbgtStr )
        print(wbgtStr)
        print("----------")
        utime.sleep(3)

