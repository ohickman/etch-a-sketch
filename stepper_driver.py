import time
import RPi.GPIO as GPIO

"""
Extensible image processing and Etch-a-sketch drawing program
Copyright (C) 2014 Oliver Hickman

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class Stepper(object):
    """Stepper class will know it's position, and will include the //take_step//
    method.
    This object assumes that one full rotation is not very big.
    If I have to do an eighth of a rotation then I'll have to rewrite
    this object."""
    def __init__(self, pins=[04,17,27,22], current_position=0, limit=2000, delay=0.00125):
        self.pins = pins
        # self.pins = [04,17,27,22] # 2013-12-26 vertical motor
        # self.pins = [18,23,24,25] # 2013-12-26 horizontal motor
        self.current_position = current_position
        self.limit = limit
        self.substep_delay = delay

        self.forward_sequence = [
                [True,False,False,False],
                [True,True,False,False],
                [False,True,False,False],
                [False,True,True,False],
                [False,False,True,False],
                [False,False,True,True],
                [False,False,False,True],
                [True,False,False,True]]

        self.reverse_sequence = [
                [False,False,False,True],
                [False,False,True,True],
                [False,False,True,False],
                [False,True,True,False],
                [False,True,False,False],
                [True,True,False,False],
                [True,False,False,False],
                [True,False,False,True]]

        self.error_sequence = [
                [True,False,False,True]]

        GPIO.setmode(GPIO.BCM) #BOARD)
        # Set pins as output
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


    def take_step(self, direction=1):
        if direction == 1:
            firing_sequence = self.forward_sequence
        elif direction == -1:
            firing_sequence = self.reverse_sequence
        else:
            firing_sequence = self.error_sequence
            direction = 0

        # Prevent sending signals to stepper if it is out-of-bounds, but
        # continue counting its position. By continuing to keep track of the
        # virtual position we can allow better representation of shapes drawn
        # partly off screen.
        if (self.current_position + direction >= self.limit or
                self.current_position + direction <= 0):
            firing_sequence = self.error_sequence

        for sub_step in range(0, len(firing_sequence)):
            for pin in range(0, len(firing_sequence[sub_step])):
                GPIO.output(self.pins[pin], firing_sequence[sub_step][pin])
                time.sleep(self.substep_delay)
        self.current_position += (direction)

    def __del__(self):
        """ deleter method needed to de-allocate pins when a stepper object is
        no longer needed.  If this isn't done then whatever pins that were high
        when a program stopped drawing will be left high when the program exits.
        There is probably a more pythonic way to do this."""
        GPIO.cleanup()


if __name__ == '__main__':
    main()
