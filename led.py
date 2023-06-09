#!/usr/bin/env python3

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 7 #Définit le numéro du port GPIO qui alimente la led

GPIO.setup(LED, GPIO.OUT)

state = GPIO.input(LED)

if state :
    GPIO.output(LED, GPIO.LOW)
else:
    GPIO.output(LED, GPIO.HIGH)
