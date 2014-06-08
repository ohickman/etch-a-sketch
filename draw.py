import time
from bressenham_functions import *
from render import Render
from canvas import Canvas
from stepper_driver import Stepper
from render_strategy import *

from raster_strategy import RasterPath # this is the one that uses "maxels"
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

def status(message):
    message = " " + message
    print (time.clock()),
    print message


status("Initializing Canvas() object.")
screen = Canvas() # use default values for the Etch-a-sketch

status("Initializing Render() object.")
image_to_draw = Render() # defaults to NullPath

#status("Loading image.")
#image_to_draw.load_image()

status("Setting path generator strategy.")
image_to_draw.set_path_generator(HelloWorld)
image_to_draw.set_path_generator(RasterPath)


status("Loading image.")
image_to_draw.open_image()

status("Generating path.")
image_to_draw.generate_path()

status("Closing image.")
image_to_draw.close_image()

status("Scaling image for Canvas.")
v_factor = float(screen.height) / float(image_to_draw.height)
h_factor = float(screen.width) / float(image_to_draw.width)
scale_factor = v_factor if v_factor < h_factor else h_factor

status("Scale factor: %s." %scale_factor)

image_to_draw.scale(scale_factor)
# image_to_draw.scale(.125) # make it quick for testing.
path = image_to_draw.path

status("Initializing motors.")
horizontal_motor = Stepper([04,17,27,22], 0, screen.width, 0.003)
vertical_motor = Stepper([18,23,24,25], 0, screen.height, 0.003)

status("Drawing image.")
for n in range(0, len(path)-1):
    leg_steps = step_bressenham(path[n], path[n+1])
    for step in leg_steps:
        horizontal_motor.take_step(step.x)
        vertical_motor.take_step(step.y)

status("Deleting motor objects.")
del horizontal_motor
del vertical_motor

status("Terminating program.")
