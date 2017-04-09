#!/usr/bin/python
from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import threading
from time import gmtime, strftime

from bluetooth import *

from pushbullet import Pushbullet

import os

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.OUT) 

auth = "74:A5:28:FA:51:B7"

pinList = [2, 3]

tick = 0

checkLoop = False

timeOut = False
AFK = True

back = False
dayLight = True

sleep = False

sentOutPush = False

#dayLightSave = False

pushNotify = Pushbullet("o.F6B2oUgRvVimbBBK02zywe0siPlbNqCl")

bConnected = False


def background():
    global sentOutPush
    global dayLight
    global sleep
    global tick
    global back
    
    while True:
        
        
        hour = int(strftime("%H"))
        if hour >= 8 and hour <= 17:
            sleep = False
            dayLight = True
            print "day"
        elif hour > 18 and hour <= 24 or hour >= 1 and hour < 8:
            dayLight = False
            print "night"

        print dayLight
        print hour
            

        nearby_devices = discover_devices(lookup_names = True)
        print "found %d devices" % len(nearby_devices)
        print str(nearby_devices)

        for addr in nearby_devices:
            for i in addr:
                print i
                print "i"
                    
       



        if len(nearby_devices) == 0:
            if back == True and tick == 3:
                print "-------------------------------------------------"
                print "================================================="
                print "                   GOOD BYE                      "
                print "================================================="
                print "-------------------------------------------------"

            if tick == 3:
                back = False
                OFF()
                tick += 1
            elif tick == 5 and sentOutPush == False:
                tick = 0
                sentOutPush = True
                push = pushNotify.push_note("Update: HAS", "Light 1 - OFF\nLight 2 - OFF")
            else:
                tick += 1
                print tick
                
            
        else:
            tick = 0
            for name, addr in nearby_devices:
                if sleep == False and name == auth:
                    sentOutPush = False
                    
                    print "ACCEPTED"
                    
                    if back == False:
                        print "-------------------------------------------------"
                        print "================================================="
                        print "                 WELCOME BACK                    "
                        print "================================================="
                        print "-------------------------------------------------"

                                
                    if dayLight == False and back == False:
                        print "================================================="
                        print "              NIGHT MODE - ACTIVE                "
                        print "================================================="
                        back = True
                        ON()
                    elif dayLight == True and back == False:
                        print "================================================="
                        print "              DAY MODE - ACTIVE                  "
                        print "================================================="
                        back = True
                        OFF()
                    elif back == True:
                        print "SKIPPED"
                    else:
                        print "Error"
               
                else:
                    print "**SLEEP MODE ACTIVE**"       
        


@app.route('/')
def main():
    global back
    
    if back == True:
        return render_template("index.html")
    elif back == False:
        return render_template("out.html")

@app.route('/ProcessL1On', methods=['L1On'])
def Light1On():
    global back
    if back == True:
        print "ON"
        GPIO.output(2, GPIO.LOW)
    elif back == False:
        print "FAILED: to turn on light 1"
    
	
@app.route('/ProcessL1Off', methods=['L1Off'])
def Light1Off():
    GPIO.output(2, GPIO.HIGH)
	
	
@app.route('/ProcessL2On', methods=['L2On'])
def Light2On():
    global back

    print back
    if back == True:
        print "ON"
        GPIO.output(3, GPIO.LOW)
    elif back == False:
        print "FAILED: to turn on light 2"
    
	
@app.route('/ProcessL2Off', methods=['L2Off'])
def Light2Off():
    GPIO.output(3, GPIO.HIGH)

@app.route('/ProcessOFF', methods=['OFF'])
def OFF():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.HIGH)

@app.route('/ProcessSLEEP', methods=['SLEEP'])
def sleep():
    global sleep
    print "Good night"
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(2, GPIO.HIGH)
    sleep = True

@app.route('/ProcessWAKE', methods=['WAKE'])
def wake():
    global sleep
    print "Good morning"
    sleep = False
    ON()
    

@app.route('/ProcessON', methods=['ON'])
def ON():
    global dayLight
    if dayLight == False:
        GPIO.output(3, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)


def mainSetup():
    t = threading.Thread(target=background)
    t.start()
    launch()


def launch():
    print "...Launching Systems..."
    print "...Launching Web Server..."
    app.run(host='192.168.0.29')
    print "Web application can be found: 192.168.0.29:5000"
    
    print "Enjoy!"
    main()

mainSetup()
