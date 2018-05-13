import pygame
# import RPi.GPIO as GPIO
import time

servoPIN = 18
min = 1.0
max = 12.5
dutyCycle = 1.5
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servoPIN, GPIO.OUT)

# p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
# p.start(dutyCycle) # Initialization
#
# GPIO.setwarnings(False)

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
        print "duty cycle: " + str(dutyCycle)
        # p.ChangeDutyCycle(dutyCycle)
        time.sleep(0.2)
except KeyboardInterrupt:
    print "done"
    # p.stop()
    # GPIO.cleanup()
