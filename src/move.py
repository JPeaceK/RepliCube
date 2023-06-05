import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

def moveMain():
    i2c = busio.I2C(SCL, SDA)
    pca = PCA9685(i2c, address = 0x41)

    pca.frequency = 50

    holder = servo.Servo(pca.channels[4])
    push = servo.Servo(pca.channels[7])
    base = servo.Servo(pca.channels[0])

    push.angle = 180
    time.sleep(0)
    push.angle = 0
    time.sleep(0)
    push.angle = 90
    time.sleep(0)

    #holder.angle = None
    #base.angle = None

    holder.angle = 0
    time.sleep(1)
    holder.angle = None


    base.angle = 180
    time.sleep(0.16)
    #Antes teníamos ángulo 0 y 0.1 seg
    base.angle = None
    time.sleep(1)

    base.angle = 80
    time.sleep(0.28)
    base.angle = None
    time.sleep(0.2)

    holder.angle = 180
    time.sleep(1)
    holder.angle = None

    base.angle = 100
    time.sleep(0.1)
   # time.sleep(0.003)
    base.angle = None
    #base.angle = 100
    #time.sleep(0.04)
    #base.angle = None
    time.sleep(1)

#moveMain()
