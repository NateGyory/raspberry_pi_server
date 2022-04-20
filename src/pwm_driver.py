# Two different examples using different libraries

# https://github.com/adafruit/Adafruit_CircuitPython_PCA9685/blob/main/examples/pca9685_servo.py
# https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

from response import Response

# TODO implement response class for error codes

class PwmDriver:
    def __init__(self):
        i2c = busio.I2C(SCL, SDA)

        self.pca = PCA9685(i2c)
        self.pca.frequency = 50
        self.servo1 = servo.Servo(self.pca.channels[0])
        self.servo2 = servo.Servo(self.pca.channels[1])
        self.servo3 = servo.Servo(self.pca.channels[2])
        self.servo4 = servo.Servo(self.pca.channels[3])
        self.servo5 = servo.Servo(self.pca.channels[4])

        self.servo1.angle = 90
        self.servo2.angle = 90
        self.servo3.angle = 90
        self.servo4.angle = 90
        self.servo5.angle = 90

    def limit_check(self, current_motor_angle, motor_angle_update):
        ret = True
        new_angle = current_motor_angle + motor_angle_update
        if new_angle > 180 or new_angle < 0:
            ret = False
        return ret

    def move_servo1(self, motor_angle_update):
        if self.limit_check(self.servo1.angle, motor_angle_update) == False: return -1

        self.servo1.angle = motor_angle_update

        return self.servo1.angle

    def move_servo2(self, motor_angle_update):
        if self.limit_check(self.servo2.angle, motor_angle_update) == False: return -1

        self.servo2.angle = motor_angle_update

        return self.servo2.angle

    def move_servo3(self, motor_angle_update):
        if self.limit_check(self.servo3.angle, motor_angle_update) == False: return -1

        self.servo3.angle = motor_angle_update

        return self.servo3.angle

    def move_servo4(self, motor_angle_update):
        if self.limit_check(self.servo4.angle, motor_angle_update) == False: return -1

        self.servo4.angle = motor_angle_update

        return self.servo4.angle

    def move_servo5(self, direction):
        if self.limit_check(self.servo5.angle, motor_angle_update) == False: return -1

        self.servo5.angle = motor_angle_update

        return self.servo5.angle

