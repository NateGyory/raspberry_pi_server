from flask import Flask, request
from pwm_driver import PwmDriver

app = Flask(__name__)
pwm_driver = PwmDriver()

@app.route("/servo1", methods=['POST'])
def servo1():
    request_data = request.get_json()

    motor_angle_update = request_data['motor_angle_update']
    angle = pwm_driver.move_servo1(motor_angle_update)

    msg = ''
    if angle >= 0:
        msg = 'servo1 angle: {}'.format(angle)
    else:
        msg = 'servo1 is at its limit'

    return msg

@app.route("/servo2", methods=['POST'])
def servo2():
    request_data = request.get_json()

    motor_angle_update = request_data['motor_angle_update']
    angle = pwm_driver.move_servo2(motor_angle_update)

    msg = ''
    if angle >= 0:
        msg = 'servo2 angle: {}'.format(angle)
    else:
        msg = 'servo2 is at its limit'

    return msg

@app.route("/servo3", methods=['POST'])
def servo3():
    request_data = request.get_json()

    motor_angle_update = request_data['motor_angle_update']
    angle = pwm_driver.move_servo3(motor_angle_update)

    msg = ''
    if angle >= 0:
        msg = 'servo3 angle: {}'.format(angle)
    else:
        msg = 'servo3 is at its limit'

    return msg

@app.route("/servo4", methods=['POST'])
def servo4():
    request_data = request.get_json()

    motor_angle_update = request_data['motor_angle_update']
    angle = pwm_driver.move_servo4(motor_angle_update)

    msg = ''
    if angle >= 0:
        msg = 'servo4 angle: {}'.format(angle)
    else:
        msg = 'servo4 is at its limit'

    return msg

@app.route("/servo5", methods=['POST'])
def servo5():
    request_data = request.get_json()

    motor_angle_update = request_data['motor_angle_update']
    angle = pwm_driver.move_servo5(motor_angle_update)

    msg = ''
    if angle >= 0:
        msg = 'servo5 angle: {}'.format(angle)
    else:
        msg = 'servo5 is at its limit'

    return msg

