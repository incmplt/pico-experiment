import machine
from machine import Pin, PWM, ADC
import time
import sys

def keypad_getvalue(pinA=6,pinB=7,pinC=8,pinD=9,pinX=2,pinY=3,pinZ=4):
  sw_a = Pin(pinA, Pin.IN, Pin.PULL_DOWN)
  sw_b = Pin(pinB, Pin.IN, Pin.PULL_DOWN)
  sw_c = Pin(pinC, Pin.IN, Pin.PULL_DOWN)
  sw_d = Pin(pinD, Pin.IN, Pin.PULL_DOWN)

  sw_x = Pin(pinX, Pin.OUT)
  sw_y = Pin(pinY, Pin.OUT)
  sw_z= Pin(pinZ, Pin.OUT)
  
  output=""

  sw_x.high()
  sw_y.high()
  sw_z.high()
  swiches=[sw_x,sw_y,sw_z]
    
  for x in swiches:
    x.low()
    # for DEBUG output
    #print([sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()])
    if sw_x.value()==0:
      if [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[0,1,1,1]:
        print("*")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,0,1,1]:
        print("7")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,1,0,1]:
        print("4")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,1,1,0]:
        print("1")
      
    elif sw_y.value()==0:
      if [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[0,1,1,1]:
        print("0")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,0,1,1]:
        print("8")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,1,0,1]:
        print("5")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,1,1,0]:
        print("2")
      
    elif sw_z.value()==0:
      if [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[0,1,1,1]:
        print("#")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,0,1,1]:
        print("9")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,1,0,1]:
        print("6")
      elif [sw_a.value(),sw_b.value(),sw_c.value(),sw_d.value()]==[1,1,1,0]:
        print("3")
      
    time.sleep(0.01)
    x.high()
  return output

while True:
  keypad_getvalue(A=6,B=7,C=8,D=9,X=2,Y=3,Z=4)
  time.sleep(0.3)
