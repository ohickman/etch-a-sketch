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

class Point( object ):
    """ The Point class represents x, y pairs in a cartesian coordinate system
    x and y are intended to be ints, though at the moment I'm not testing for
    that.  In the future I'll probably make another class that inherits from
    Point and adds the requirement that elements be ints."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        """ x coordinate is a property of Point, must be any numeric data type.
        >>> a = Point(9,0)
        >>> a.x = 8
        >>> a.y = "elephant"
        Could not convert "elephant" into an integer."""
        return self._x

    @x.setter
    def x(self, x):
        try:
            x = int(x)
        except ValueError:
            print ("Could not convert \"%s\" into an integer." %x)
            x = 0
        self._x = x

    @property
    def y(self):
        """ y coordinate is a property of Point, must be any numeric data type.
        >>> a = Point(0,8)
        >>> a.y = 8"""
        return self._y

    @y.setter
    def y(self, y):
        try:
            y = int(y)
        except ValueError:
            print ("Could not convert \"%s\" into an integer." %y)
            y = 0
        self._y = y

    def __rmul__(self, other):
        """ Piecewise multiplies a scalar by each element in Point.
        >>> a = Point(1,2)
        >>> 2*a
        (2, 4)"""
        return Point(other*self.x, other*self.y)

    def __add__(self, other):
        """ Piecewise adds two Points together.
        >>> a = Point(1,2)
        >>> b = Point(1,2)
        >>> a + b
        (2, 4)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __neg__(self):
        """ Piecewise inverts each element in the Point.
        >>> a = Point(1,2)
        >>> -a
        (-1, -2)
        >>> b = Point(4,-7)
        >>> -b
        (-4, 7)
        >>> c = Point()
        >>> -c
        (0, 0)
        """
        return Point(-self.x, -self.y)

    def __sub__(self, other):
        """ Piecewise subtracts the elements of other from the elements of self.
        >>> a = Point(4,7)
        >>> b = Point(3,9)
        >>> a - b
        (1, -2)
        >>> c = Point()
        >>> a - c
        (4, 7)
        """
        return self + (-other)

    def __eq__(self, other):
        """Tests to see if two Point objects are piecewise equal.  The pieces
        don't need to be of the same type, just the same numeric value.
        >>> a = Point(1,2)
        >>> b = Point(1,2)
        >>> a == b
        True
        >>> c = Point() # default point = (0,0)
        >>> a == c
        False
        """
        if not isinstance(other, Point):
            return NotImplemented
        else:
            return self.x == other.x and self.y == other.y

    def __repr__(self):
        """ Machine readable representation of a Point in the format (x, y).
        This is the format that you'd want when building a list of points.
        >>> a = Point()
        >>> a
        (0, 0)"""
        return "({0._x!r}, {0._y!r})".format(self)

    def __str__(self):
        """ Human readable representation of a Point.
        >>> a = Point()
        >>> print a
        Point(0, 0)"""
        return "Point({0._x!r}, {0._y!r})".format(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
