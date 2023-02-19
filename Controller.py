import pyfirmata
import numpy as np
comport='COM5'
board=pyfirmata.Arduino(comport)

servoPin = board.get_pin('d:13:s')
servoPin2 = board.get_pin('d:12:s')
def led(total):
    if total==0:
        servoPin.write(0)
        servoPin2.write(0)
    if total==1:
        servoPin.write(45)
        servoPin2.write(45)
    if total==2:
        servoPin.write(120)
        servoPin2.write(120)
    if total==3:
        servoPin.write(200)
        servoPin2.write(200)
    if total==4:
        servoPin.write(0)
        servoPin2.write(0)
    if total==5:
        servoPin.write(340)
        servoPin2.write(340)
