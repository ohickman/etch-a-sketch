from stepper_driver import Stepper

""" This is quick and dirty.  Don't judge."""

def up(dist):
    motor = Stepper([18,23,24,25], 1000)
    for n in range(0, dist):
        motor.take_step(1)
    del motor

def dn(dist):
    motor = Stepper([18,23,24,25], 1000)
    for n in range(0, dist):
        motor.take_step(-1)
    del motor

def rt(dist):
    motor = Stepper([04,17,27,22], 1000)
    for n in range(0, dist):
        motor.take_step(1)
    del motor

def lt(dist):
    motor = Stepper ([04,17,27,22], 1000)
    for n in range(0, dist):
        motor.take_step(-1)
    del motor

while True:
    command = raw_input ("?: ")
    if command:
        direction = command[:1]
        distance = command[1:]
        if int(distance):
            distance = int(distance)
            if direction == "u":
                up(distance)
            if direction == "d":
                dn(distance)
            if direction == "r":
                rt(distance)
            if direction == "l":
                lt(distance)


