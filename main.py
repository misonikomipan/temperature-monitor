from send2slack import send_msg
from calc_temp import calc_tmp
from time_signal import time_signal
import dht11

import RPi.GPIO as GPIO
from time import sleep
import datetime


WEBHOOK_URL = "***"
message = "Hello, slack!!"
N_PIN = 14 # GPIO pin's number (to get temperature data)
INTERVAL_TIME = 120 # [sec]

FAILLED_LIMIT = 60 # [times]
TEMPERATURE_UPPER_LIMIT = 30 # [C]
JIHO_TIME = 8 #0-24 [hour]

# 8zi ikou
now_hour = datetime.datetime.today().hour
date_flag = True if now_hour < 8 else False
today = datetime.datetime.today().date() # date





# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
# read data using pin 14
instance = dht11.DHT11(pin=N_PIN)

# main loop
while 1:
    # get temperature data
    valid = False 
    failled_cnt = 0
    while not(valid):
        sleep(INTERVAL_TIME)
        res = calc_tmp(N_PIN, instance)
        valid = res.is_valid()
        failled_cnt += 1
        # abnormality detected
        if failled_cnt == FAILLED_LIMIT:
            message = f"failled {FAILLED_LIMIT} times >< \nhelp!!"
            send_msg(WEBHOOK_URL, message)

    temperature = res.temperature
    humid = res.humidity
    
    # time signal (jiho-)
    today, date_flag = time_signal(today, date_flag, JIHO_TIME, temperature, humid, WEBHOOK_URL)
    
    # abnormality detected
    if temperature >= TEMPERATURE_UPPER_LIMIT:
        message = f":fire::fire: 室温: {temperature} C :fire::fire:"
        send_msg(WEBHOOK_URL, message)


