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
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

class RasterPath(PathInterface):

    self.value_4 = [Point(0,0),
            Point(1,4)
            Point(0,4)
            Point(1,0)
            Point(2,4)
            Point(1,4)
            Point(2,0)
            Point(3,4)
            Point(2,4)
            Point(3,0)
            Point(4,4)
            Point(3,4)
            Point(4,0)]

    self.value_3 = [Point(0,0),
            Point(0,4)
            Point(1,0)
            Point(1,4)
            Point(2,0)
            Point(2,4)
            Point(3,0)
            Point(3,4)
            Point(4,0)]
    
    self.value_2 = [Point(0,0),
            Point(1,4)
            Point(2,0)
            Point(3,4)
            Point(4,0)]

    self.value_1 = [Point(0,0),
            Point(2,4)
            Point(4,0)]

    self.value_0 = [Point(0,0),
            Point(4,0)]



