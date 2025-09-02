from picozero import pico_led
import machine
import time
import math

sensor=machine.ADC(0) # 103JT-025/050
sensor_temp = machine.ADC(4) # RaspberryPi pico onboard Thermistor
conversion_factor = 3.3 / (65535)

B = 3950.0
R0 = 10000.0
T0 = 25.0
Z = 273.15

def calcThermistorTemp( adc_val ):
    # ADC値から電圧を計算
    volt = adc_val * conversion_factor    
    # 電圧からサーミスタ抵抗を計算(r)
    r = (( 3.3 / volt ) - 1.0 ) * R0
    # 抵抗値から係数を計算
    #B0 = 3452.9 * math.pow( r, -0.012329 )
    B0 = B * math.pow( r, -0.012329 )
    # サーミスタ抵抗から温度を計算
    T_bar = (1.0 / B0 ) * math.log( r / R0 ) + (1 / ( T0 + Z ))    
    # 計算結果はケルビン温度の逆数になっているので摂氏に戻す
    T = (1.0 / T_bar) - Z
    return T

while True :
    pico_led.on()
    time.sleep(1)
    reading = sensor_temp.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
    temperature = 27 - (reading - 0.706)/0.001721

    sens = sensor.read_u16()
    templ = calcThermistorTemp( sens )

    print( "----+----+----+" )
    print( temperature )
    print( templ )
    pico_led.off()
    time.sleep(1)
