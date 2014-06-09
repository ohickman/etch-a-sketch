from point import Point
from path_interface import PathInterface
from render_strategy import NullPath

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

class Render( PathInterface ):
    """The Render() class inherits height, width, and path getters and setters
    from PathInterface as well as the __len__ special method.
    It extends this by including a path_generator object (to do the image
    conversion), a _source attribute (file name as a string), and an _image
    attribute (array representing an image read from a file).
    
    Unless one of the path_generators has been selected and it has generated
    a path, self.path returns an empty list "[]"."""

    def __init__(self, path_generator=NullPath):
        # self.height = 0 # handled by PathInterface x3
        # self.width = 0
        # self.path = []
        self.path_generator = path_generator
        self._source = ""
        self._image = ""

    def set_path_generator(self, generator=NullPath):
        """ Strategy pattern! """
        self.path_generator = generator


    def open_image(self, source="dolphin.jpg"):
        """ This method is the PIL version of load_image below.  No promises
        about what will be supported when, or what the differences will be.
        """
        from PIL import Image
        im = Image.open(source)
        self.width, self.height = im.size


    def load_image(self, source="dolphin.jpg"):
        """ This method only needs to be called if a path generator needs an
        image object passed to it.  If the generator doesn't need an image,
        then don't call it.  That feels like I'm not properly encapsulating
        things, but at some point someone needs to know what they are doing.
        """
        # from scipy import ndimage
        # import numpy as np
        # import matplotlib.pyplot as plt # plt.imshow(), plt.show()

        self._source = source
        image = plt.imread(self._source) # open image with matplotlip
        # Flip the image upside down.  The origin in a .jpg is the top left
        # but it should be the bottom left, because math.
        image = np.flipud(image)
        self._image = image
        self._path = [] # don't carry over _path from previous image.

    def generate_path(self):
        """ Call the selected path generator to return a path, widdth, and
        height.
        >>> from render_strategy import *
        >>> a = Render()
        >>> a.set_path_generator(TinyTestPath)
        >>> a.generate_path()
        >>> a.path
        [(0, 0), (12, 18), (24, 9), (0, 0)]
        >>> a.set_path_generator(ShortTestPath)
        >>> a.generate_path() # remmeber ShortTestPath has built-in errors.
        Could not convert "cow" into an integer.
        >>> a.path
        [(0, 0), (20, 20), (20, 100), (100, 100), (120, 120), (100, 100), (20, 100), (20, 20), (60, 60), (100, 20), (100, 20), (60, 60), (20, 20), (80, 20), (50, -30), (20, 20), (0, 20), (0, 20), (0, 0)]"""
        generated_path_object = self.path_generator(self._image)
        self.path = generated_path_object.path
        self.width = generated_path_object.width
        self.height = generated_path_object.height

    @property
    def aspect(self):
        """Returns the ratio width/height as a single float type.
        Lanscape image with the ratio 3:2 would return 1.5
        Portrait image with the ratio 10:16.18 would return 0.618.
        >>> from render_strategy import TinyTestPath 
        >>> a = Render()
        >>> a.set_path_generator(TinyTestPath)
        >>> a.generate_path()
        >>> a.aspect
        1.3333333333333333
        >>> type(a.aspect)
        <type 'float'>"""
        return float(self.width) / float(self.height)

    def scale(self, factor=1):
        """ Given a float or an int, each Point in path will be multiplied by
        that factor.  self.height and self.width will also be scaled similarly.
        All Points in self.path will remain composed of integers.
        >>> from render_strategy import TinyTestPath
        >>> a = Render()
        >>> a.set_path_generator(TinyTestPath)
        >>> a.generate_path() 
        >>> a.scale(0.5)
        >>> a.path
        [(0, 0), (6, 9), (12, 4), (0, 0)]"""
        for index, point in enumerate(self.path):
            self.path[index] = factor * self.path[index]
        self.width = int(factor * self.width)
        self.height = int(factor * self.height)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
