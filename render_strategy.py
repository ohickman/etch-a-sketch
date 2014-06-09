from point import Point
from path_interface import PathInterface

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

class EdgeDetectDONTUSE(PathInterface):
    """ As of 2014-01-05 this path generator doesn't do anything.  Sorry."""
    # from scipy import ndimage
    # import numpy as np
    def __init__(self, image):
        # self._source = source 
        # img = plt.imread(self._source)
        # image = np.flipud(image)
        self.image = image
        self.height = len(iamge[1])
        self.width = len(image)
        self.path = []
       # what did I put in Megan's text?  Grab that stuff!
       # now do all that fancy edge detection stuff here.

        image = image[...,2] # Grab only one chanel?
        image = ndimage.gaussian_filter(image, sigma=10) #sigma fn of img size
        image = (image > image.mean()).astype(np.float) # threshold mask at
        image = ndimage.sobel(image, axis=0, mode='constant') # edge-detection


class NullPath(PathInterface):
    def __init__(self, image):
        self.width = "0"
        self.height = "0"
        self.path = []


class TinyTestPath(PathInterface):
    """ Tiny path handy for doctest examples.
    [(0, 0), (12, 18), (24, 9), (0, 0)]
    """
    def __init__(self, image):
        self.width = 24
        self.height = 18
        self.path = [Point(0,0),
                Point(12, 18),
                Point(24, 9),
                Point(0,0)]


class ShortTestPath(PathInterface):
    """ Short path handy for testing code.  Includes Points initialized
    with negative values, non-ints, vertical lines, horizontal lines, lines
    with zero length, etc.
    """
    def __init__(self, image):
        self.width = 100
        self.height = 100
        self.path = [Point(0,0),
            Point(20,20),
            Point(20,100),      # Vertical line up
            Point(100,100),     # Horizontal line right
            Point(120,120),     # Point outside height, width
            Point(100,100),
            Point(20,100),      # Horizontal line left
            Point(20,20),       # Vertical line down
            Point(60,60),       # Positive slope up
            Point(100,20),      # Negative slope down
            Point(100,20),      # Line of zero length
            Point(60,60),       # Negative slope up
            Point(20,20),       # Positive slope down
            Point(80,20),
            Point(50,-30),      # Point with negative element
            Point(20,20.1234),  # Point with non int num
            Point("cow", 20),   # Point with invalid value
            Point(0,20),
            Point(0,0)]

class HelloWorld( PathInterface ):
    """ This path is quick and dirty - I wrote it quickly so that I'd have a 
    path to play with, don't judge."""
    def __init__(self, image):
        # for this path image is not used.
        self.width = 980
        self.height = 230
        self.path = [Point(0,0), #H
            Point(0,220),
            Point(0,110),
            Point(90,110),
            Point(90,220),
            Point(90,0),
            Point(215,0), #e
            Point(215,30),
            Point(180,0),
            Point(145,25),
            Point(130,90),
            Point(145,145),
            Point(180,170),
            Point(210,145),
            Point(215,90),
            Point(130,90),
            Point(145,25),
            Point(180,0),
            Point(250,0), #l
            Point(250,230),
            Point(250,0),
            Point(300,0), #l
            Point(300,230),
            Point(300,0),
            Point(380,0), #o
            Point(350,25),
            Point(340,90),
            Point(350,145),
            Point(380,170),
            Point(410,145),
            Point(420,90),
            Point(410,25),
            Point(380,0),
            Point(545,0), #W
            Point(510,220),
            Point(545,0),
            Point(580,220),
            Point(620,0),
            Point(655,220),
            Point(620,0),
            Point(715,0), #o
            Point(685,25),
            Point(675,90),
            Point(685,145),
            Point(715,170),
            Point(745,145),
            Point(755,90),
            Point(745,25),
            Point(715,0),
            Point(790,0), #r
            Point(790,170),
            Point(790,140),
            Point(820,155),
            Point(820,160),
            Point(820,155),
            Point(790,140),
            Point(790,0),
            Point(870,0), #l
            Point(870,230),
            Point(870,0),
            Point(980,0), #d
            Point(980,230),
            Point(980,130),
            Point(970,145),
            Point(940,170),
            Point(910,145),
            Point(900,90),
            Point(910,25),
            Point(940,0),
            Point(970,25),
            Point(980,40),
            Point(980,0),
            Point(0,0)]



if __name__ == "__main__":
    import doctest
    doctest.testmod()
