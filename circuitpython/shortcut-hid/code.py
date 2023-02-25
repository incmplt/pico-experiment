# for RaspberryPi Pico : Circuit Python HID
from board import *
#import analogio
import digitalio
import time
import usb_hid
#from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard( usb_hid.devices)

ssbtn = digitalio.DigitalInOut( GP2 )
ssbtn.direction = digitalio.Direction.INPUT
ssbtn.pull = digitalio.Pull.DOWN

wsbtn = digitalio.DigitalInOut( GP3 )
wsbtn.direction = digitalio.Direction.INPUT
wsbtn.pull = digitalio.Pull.DOWN

escbtn = digitalio.DigitalInOut( GP4 )
escbtn.direction = digitalio.Direction.INPUT
escbtn.pull = digitalio.Pull.DOWN

ssp=False
wsp=False
esp=False

while True:
    # GP2 : Full screen shot to file.
    if ssbtn.value:
        if ssp== False:
            print("Full Screen Shot Autosave")
            kbd.send(Keycode.GUI, Keycode.PRINT_SCREEN)
            ssp = True
    else:
        if ssp:
            ssp=False
    # GP3 : Current Window Screen shot to Clipboard.
    if wsbtn.value:
        if wsp== False:
            print("Window Screen Shot")
            kbd.send(Keycode.ALT,Keycode.PRINT_SCREEN)
            wsp = True
    else:
        if wsp:
            wsp=False

    # GP4 : ESC key.
    if escbtn.value:
        if esp== False:
            print("ESC")
            kbd.send(Keycode.ESCAPE)
            esp = True
    else:
        if esp:
            esp=False

