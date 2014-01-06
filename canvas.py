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

class Canvas(object):
    """ The Canvas object will hold all the particulars about the screen that
    will be displaying an image.  It is intended to be an etch-a-sketch as I 
    write this, but could morph into something else in the future."""
    def __init__(self, height=1900, width=2800, wrap=False):
        self._height = int(height)
        self._width = int(width)
        self._wrap = wrap

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
