from point import Point

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

class PathInterface(object):
    """ interface for path generator strategies, this is part of the interface
    for the Render() class, and it is the whole interface for the strategy
    pattern classes.
    """

    def __init__(self):
        self.width = 0 
        self.height = 0
        self.path = []

    @property
    def width(self):
        """
        >>> a = PathInterface()
        >>> a.width = -7.8
        >>> a.width
        7
        >>> a.width = "cow"
        Could not convert "cow" into an int.
        >>> a.width
        0"""
        return self.__width

    @width.setter
    def width(self, value):
        try:
            value = abs(int(value))
        except ValueError:
            print ("Could not convert \"%s\" into an int." %value)
            value = 0
        self.__width = value
   
    @property
    def height(self):
        """
        >>> a = PathInterface()
        >>> a.height = -10.34
        >>> print a.height
        10
        >>> a.height = "robot"
        Could not convert "robot" into an int.
        """
        return self.__height

    @height.setter
    def height(self, value):
        try:
            value = abs(int(value))
        except ValueError:
            print "Could not convert \"%s\" into an int." %value
            value = 0
        self.__height = value

    @property
    def path(self):
        """
        >>> a = PathInterface()
        >>> a.path
        []"""
        return self.__path

    @path.setter
    def path(self, list):
        """ The path is intended to be a list of Point()s, but they could just
        be 2 tupples if no one calls for an element by name.  I'll leave off
        the test for now."""
        # if isinstance(list[0], Point)
        self.__path = list

    def __len__(self):
        """ Returns an Int type representing the number of Point()s in the path
        >>> a = PathInterface()
        >>> len(a.path)
        0
        >>> a.path = [Point(0,0), Point(1,1), Point(2,2)]
        >>> len(a.path)
        3"""
        return len(self._path)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
