import math # used for math.copysign(1, delta_x)
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

def step_bressenham(point_0 = Point(0,0), point_1 = Point(0,0)):
    """ Given two Point objects this will compute the individual steps needed to 
    travel from the first to the second.
    In the event that no steps need to be taken then a list with one zero Point
    will be returned.
    Returning a list of the zero point may not be necessary and might not be
    supported in the future.
    >>> print step_bressenham(Point(0,0), Point(0,0))
    [(0, 0)]
    >>> print step_bressenham(Point(), Point(7,4))
    [(1, 1), (1, 0), (1, 1), (1, 0), (1, 1), (1, 0), (1, 1)]
    >>> print step_bressenham(Point(7,4), Point())
    [(-1, -1), (-1, 0), (-1, -1), (-1, 0), (-1, -1), (-1, 0), (-1, -1)]
    """
    bressenham_points = compute_bressenham(point_0, point_1)
    steps = []
    for n in range(0, len(bressenham_points)-1):
        steps.append(bressenham_points[n + 1] - bressenham_points[n])
    return steps


def compute_bressenham(point_0 = Point(0,0), point_1 = Point(0,0)):
    """ Creates a type="list" of Points that connect point_0 to point_1 and
    includes BOTH of those end points.
    >>> compute_bressenham(Point(4,7), Point())
    [(4, 7), (3, 6), (3, 5), (2, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    >>> compute_bressenham(Point(0, 0), Point(7, -4))
    [(0, 0), (1, -1), (2, -1), (3, -2), (4, -2), (5, -3), (6, -3), (7, -4)]
    >>> compute_bressenham(Point(), Point())
    [(0, 0), (0, 0)]
    >>> compute_bressenham(Point(4,-7), Point(4,-7))
    [(4, -7), (4, -7)]"""

    # computing the deltas - if both points aren't of type int, then I'll get
    # errors when generating a range using the deltas.
    delta_x = point_1.x - point_0.x
    delta_y = point_1.y - point_0.y

    # compute slope of line to be drawn:
    # this part of the function feels like a hack job.  I should sit down, 
    # do some math, and figure out what the functions should actually look
    # like rather than just changing things almost at random until the tests
    # work.
    if point_0.x == point_1.x:
        slope = 0
        #print "dx = dy"
    elif abs(delta_x) >= abs(delta_y):
        slope = (float(delta_y)) / (float(delta_x))
        #print "dx > dy"
    else:
        # this is actually the inverse slope, but that will reduce the division
        # by zero errors that would be generated when computing the inverse
        # slope below.
        slope = (float(delta_x)) / (float(delta_y))
        #print "dx < dy"
    
    #print slope

    list_of_points = []

    if delta_x == delta_y == 0:
        list_of_points = [point_0, point_1]

    elif abs(delta_x) >= abs(delta_y):
        start = point_0.x
        increment = int(math.copysign(1, delta_x))
        stop = point_1.x + increment
        x_values = range(start, stop, increment)
        for n in x_values:
            list_of_points.append(Point(n, int(round(slope * (n - point_0.x) + point_0.y,0))))

    else:
        start = point_0.y
        increment = int(math.copysign(1, delta_y))
        stop = point_1.y + increment
        y_values = range(start, stop, increment)
        for n in y_values:
            # in the line below, slope is the inverse of the normal math
            # definition of slope and should have been computed that way above.
            # This helps avoid division-by-zero errors.
            list_of_points.append(Point(int(round(slope * (n - point_0.y) + point_0.x,0)), n))

    return list_of_points


if __name__ == '__main__':
    import doctest
    doctest.testmod()
