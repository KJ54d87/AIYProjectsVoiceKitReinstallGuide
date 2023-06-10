#!/usr/bin/env python
# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
from __future__ import print_function

import os
from time import sleep
import random

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

f = open("MPG123.out", "w")
f.close()

def rndmp3():
        randomfile = random.choice(os.listdir("/home/pi/Music/"))
        file = ' /home/pi/Music/' + randomfile
        ext = os.path.splitext(randomfile)[-1].lower()
	print(randomfile)
        if ext == ".mp3":
                os.system('pkill mpg123')
                os.system('mpg123 2>MPG123.out -v ' + file + ' &');
        else:
                os.system('pkill aplay')
                os.system('aplay' + file + ' &');

while True:
        f = open('MPG123.out', 'r+')
	if (os.stat(f.name).st_size == 0):
                f.write("running")
                rndmp3()
		continue
	lst = list(f.readlines())
        last_line = lst[len(lst)-1]
        print(last_line, end = '\r')
        if "Decoding of" in last_line:
                print("yay")
                f.write("running")
                rndmp3()
        f.close()
        if (GPIO.input(23) == False):
                rndmp3()

        sleep(0.1)
