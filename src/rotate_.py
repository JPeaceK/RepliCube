# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

def rotate_Main():
    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c, address = 0x41)

    pca.frequency = 50

    push = servo.Servo(pca.channels[7])
    base = servo.Servo(pca.channels[0])

    push.angle = 180
    time.sleep(0)
    push.angle = 0
    time.sleep(0)
    push.angle = 90
    time.sleep(0)

    base.angle = 0
    time.sleep(0.082)
    #Antes teníamos ángulo 0 y 0.1 seg
    base.angle = None
    time.sleep(1)

    base.angle = 103
    time.sleep(0.051)
    base.angle = None
    time.sleep(1)

#rotate_Main()
