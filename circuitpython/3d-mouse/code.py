# for RaspberryPi Pico : Circuit Python HID
# Sensor : KXM52-1050
from board import *
import analogio
import digitalio
import time
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

posX = analogio.AnalogIn(A0)
posY = analogio.AnalogIn(A1)
posZ = analogio.AnalogIn(A2)

grid = 660 / 2

led = digitalio.DigitalInOut(LED)
led.direction = digitalio.Direction.OUTPUT

pin = digitalio.DigitalInOut( GP16 )
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.DOWN

iniX = (posX.value)
iniY = (posY.value)
#iniZ = (posZ.value)

mouse = Mouse(usb_hid.devices)
#kbd = Keyboard(usb_hid.devices)
lpress = False;

while True:
    time.sleep(0.02)
    numX = int((iniX - posX.value) / grid)
    numY = int((iniY - posY.value) / grid)
    #numZ = int((iniZ - posZ.value) / grid)
    #print( str( numX ) +' - '+ str( numY ) +' - '+ str( numZ ) )
    if pin.value :
        if lpress == False:
            mouse.press( Mouse.LEFT_BUTTON )
            led.value = True
            lpress = True
    else:
        if lpress:
            mouse.release( Mouse.LEFT_BUTTON )
            led.value = False
            lpress = False        
    if abs( numX) > 5 or abs( numY ) > 5:
        numX = numX*-1
        numY = numY*-1
        mouse.move( numY, numX )
    #if pin.value:
    #    print( 'Button ON')
