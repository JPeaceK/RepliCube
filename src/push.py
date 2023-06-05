# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

def pushMain():

    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c, address = 0x41)

    pca.frequency = 50

    push = servo.Servo(pca.channels[7])

    push.angle = 180
    time.sleep(1.1) #(1.135)/(1.138)
    push.angle = 0
    time.sleep(0.1)
    push.angle = 90
    time.sleep(1)

#pushMain()

