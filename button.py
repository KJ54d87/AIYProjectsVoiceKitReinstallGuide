#!/usr/bin/env python
# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-

import os
from time import sleep
import random

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def rndmp3():
        randomfile = random.choice(os.listdir("/home/pi/Music/"))
        file = ' /home/pi/Music/' + randomfile
        ext = os.path.splitext(randomfile)[-1].lower()
        if ext == ".mp3":
                os.system('pkill mpg123')
                os.system('mpg123' + file + ' &');
        else:
                os.system('pkill aplay')
                os.system('aplay' + file + ' &');

while True:
        if (GPIO.input(23) == False):
                rndmp3()

        sleep(0.1);
