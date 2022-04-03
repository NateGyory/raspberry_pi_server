# Two different examples using different libraries

# https://github.com/adafruit/Adafruit_CircuitPython_PCA9685/blob/main/examples/pca9685_servo.py
# https://www.aranacorp.com/en/using-a-pca9685-module-with-raspberry-pi/

#from board import SCL, SDA
#import busio
#
#from adafruit_motor import servo
#from adafruit_pca9685 import PCA9685

#from response import Response

# TODO implement response class for error codes

class PwmDriver:
    def __init__(self):
        #i2c = busio.I2C(SCL, SDA)

        #self.pca = PCA9685(i2c)
        #self.pca.frequency = 50
        #self.servo1 = servo.Servo(pca.channels[0])
        #self.servo2 = servo.Servo(pca.channels[1])
        #self.servo3 = servo.Servo(pca.channels[2])
        #self.servo4 = servo.Servo(pca.channels[3])
        #self.servo5 = servo.Servo(pca.channels[4])

        self.angle_update_value = 5

        #self.servo1.angle = 50
        #self.servo2.angle = 50
        #self.servo3.angle = 50
        #self.servo4.angle = 50
        #self.servo5.angle = 50

        self.servo1_angle = 50
        self.servo2_angle = 50
        self.servo3_angle = 50
        self.servo4_angle = 50
        self.servo5_angle = 50

    def limit_check(self, angle, direction):
        ret = True
        #if direction == 1 and self.servo1.angle + self.angle_update_value > 180 or direction == -1 and self.servo1.angle - self.angle_update_value < 0:
        if direction == 1 and self.servo1_angle + self.angle_update_value > 180 or direction == -1 and self.servo1_angle - self.angle_update_value < 0:
            ret = False
        return ret

    def move_servo1(self, direction):
        #if limit_check(self.servo1.angle) == False:
        if self.limit_check(self.servo1_angle, direction) == False: return -1

        if direction == 1:
            #self.servo1.angle += self.angle_update_value
            self.servo1_angle += self.angle_update_value
        else:
            #self.servo1.angle -= self.angle_update_value
            self.servo1_angle -= self.angle_update_value

        return self.servo1_angle

    def move_servo2(self, direction):
        #if limit_check(self.servo2.angle) == False:
        if self.limit_check(self.servo2_angle, direction) == False: return -1

        if direction == 1:
            #self.servo2.angle += self.angle_update_value
            self.servo2_angle += self.angle_update_value
        else:
            #self.servo2.angle -= self.angle_update_value
            self.servo2_angle -= self.angle_update_value

        return self.servo2_angle

    def move_servo3(self, direction):
        #if limit_check(self.servo3.angle) == False:
        if self.limit_check(self.servo3_angle, direction) == False: return -1

        if direction == 1:
            #self.servo3.angle += self.angle_update_value
            self.servo3_angle += self.angle_update_value
        else:
            #self.servo3.angle -= self.angle_update_value
            self.servo3_angle -= self.angle_update_value

        return self.servo3_angle

    def move_servo4(self, direction):
        #if limit_check(self.servo4.angle) == False:
        if self.limit_check(self.servo4_angle, direction) == False: return -1

        if direction == 1:
            #self.servo4.angle += self.angle_update_value
            self.servo4_angle += self.angle_update_value
        else:
            #self.servo4.angle -= self.angle_update_value
            self.servo4_angle -= self.angle_update_value

        return self.servo4_angle

    def move_servo5(self, direction):
        #if limit_check(self.servo5.angle) == False:
        if self.limit_check(self.servo5_angle, direction) == False: return -1

        if direction == 1:
            #self.servo5.angle += self.angle_update_value
            self.servo5_angle += self.angle_update_value
        else:
            #self.servo5.angle -= self.angle_update_value
            self.servo5_angle -= self.angle_update_value

        return self.servo5_angle

