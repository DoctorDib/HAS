import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(11, 50)

p.start(7.5)


position = 7.5
try:
    while True:

        move = raw_input("move: ")

        if move == "a":
            position = position - 2
            p.start(position)
            time.sleep(1)
            p.stop()

        elif move == "d":
            position = position + 2
            p.start(position)
            time.sleep(1)
            p.stop()
        elif move == "e":
            p.stop()
            GPIO.cleanup()

        else:
            p.ChangeDutyCycle(7.5)

        print position



except KeyboardInterrupt:
    print "hello"
