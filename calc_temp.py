import RPi.GPIO as GPIO
import dht11
import time
import datetime



def calc_tmp(n_pin, instance):
    result = instance.read()
    if result.is_valid():
        temperature = result.temperature
        humid = result.humidity
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
    return result

if __name__ == '__main__':
    n_pin = 14
    
    # initialize GPIO
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    # read data using pin 14
    instance = dht11.DHT11(pin=n_pin)
    result = calc_tmp(n_pin, instance)
    if result.is_valid():
        temperature = result.temperature
        print(f"temp: {temperature} C")
    else:
        print("failed")
    GPIO.cleanup()
