import time
from render import Render
from canvas import Canvas
#from render_strategy import *
from raster_strategy import RasterPath
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

# screen = Canvas() # use default values for the Etch-a-sketch
status("Initializing Render() object.")
image_to_draw = Render()

status("Setting path generator strategy.")
#image_to_draw.set_path_generator(HelloWorld)
image_to_draw.set_path_generator(RasterPath)


status("Loading image.")
image_to_draw.open_image()

status("Generating path.")
image_to_draw.generate_path()

# status("Closing image.")
# image_to_draw.close_image()

img_file = open("sim.svg", "wb")

img_file.write("<svg width='")
img_file.write(str(image_to_draw.width))
img_file.write("' height='")
img_file.write(str(image_to_draw.height))
img_file.write("'>\n\n")

img_file.write("<rect width='")
img_file.write(str(image_to_draw.width))
img_file.write("' height='")
img_file.write(str(image_to_draw.height))
img_file.write("' style='fill:#d3d3d3; stroke-width:3; stroke:black' />\n\n")

img_file.write("<polyline points='")
path = image_to_draw.path

for point in path: #n in range(0, len(path)-1):
    img_file.write(str(point.x) + "," + str(image_to_draw.height-point.y) + " ")
 
img_file.write("'\nstyle='fill:none; stroke:black; stroke-width:3' />\n\n")
img_file.write("</svg>\n")
img_file.close()
