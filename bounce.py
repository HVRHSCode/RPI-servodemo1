import time
from adafruit_servokit import ServoKit
hat = ServoKit(channels=16)
angle = 0
direction = -1
def get_servos():
    servos = input("How many servos are connected? (type a whole number) ")
    try: 
        servos = int(servos)
    except(ValueError): 
        print("Invalid input.\n")
        get_servos()
    return servos
servos = get_servos()
while True:
    print("Setting angle {}".format(angle))
    for i in range (servos):
        hat.servo[i].angle = angle
    if (angle >= 180) or (angle <= 0):
        direction = -direction
    angle += (10*direction)
    time.sleep(0.6)