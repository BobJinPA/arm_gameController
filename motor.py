import RPi.GPIO as GPIO
import time

servoPIN = 17
min = 1.5
max = 12.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(1.5) # Initialization
try:
    while True:
        # p.ChangeDutyCycle(5)
        # time.sleep(0.5)
        # p.ChangeDutyCycle(7.5)
        # time.sleep(0.5)
        # p.ChangeDutyCycle(10)
        # time.sleep(0.5)
        # p.ChangeDutyCycle(12.5)
        # time.sleep(0.5)
        # p.ChangeDutyCycle(10)
        # time.sleep(0.5)
        # p.ChangeDutyCycle(7.5)
        # time.sleep(0.5)
        # p.ChangeDutyCycle(5)
        # time.sleep(0.5)
        p.ChangeDutyCycle(1.5)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()