import pygame
import RPi.GPIO as GPIO
import time

servoPIN = 17
min = 1.5
max = 12.5
dutyCycle = 1.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(dutyCycle) # Initialization

pygame.init()
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print "move left"
                    if dutyCycle > min:
                        dutyCycle = dutyCycle - 0.1
                if event.key == pygame.K_RIGHT:
                    print "move right"
                    if dutyCycle < max:
                        dutyCycle = dutyCycle + 0.1
        p.ChangeDutyCycle(dutyCycle)
        time.sleep(0.1)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()