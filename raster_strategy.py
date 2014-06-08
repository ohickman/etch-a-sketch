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

class RasterPath( PathInterface ):
    """
    This schema breaks an image into large pixels (on my etch a sketch these
    would be on the order of ~1cm) and then draws a predefined pattern in 
    each pixel rastering across the image drawing each pixel in succession.
    This is a very simple naive approach to making the Etch a sketch draw
    an image.
    
    Things to do:
    1) import an image
    2) find the height and width of the image
    3) divide the image into some number of macro-pixels (maxels)
    4) find the average value of each maxel
    5) find the coord of the top left corner of each maxel
    6) 
    """

    values = {} # create a dict with the various values pre-defined.
    values[4] = [Point(0,0), Point(1,4), Point(0,4), Point(1,0), Point(2,4),
            Point(1,4), Point(2,0), Point(3,4), Point(2,4), Point(3,0),
            Point(4,4), Point(3,4), Point(4,0)]
    values[3] = [Point(0,0), Point(0,4), Point(1,0), Point(1,4), Point(2,0),
            Point(2,4), Point(3,0), Point(3,4), Point(4,0)]
    values[2] = [Point(0,0), Point(1,4), Point(2,0), Point(3,4), Point(4,0)]
    values[1] = [Point(0,0), Point(2,4), Point(4,0)]
    values[0] = [Point(0,0), Point(4,0)]


    
    def open_image():

        from PIL import Image
        im = Image.open("dolphin.jpg")

        """use the correct methods to set these attributes"""
        self.width, self.height = im.size

    def close_image():
        im.close()


    def generate_path()
        import ImageStat # Stat and mean functions for value of maxel
        
        for x in range(0, self.width/50):
            for y in range(0, self.height/50):
                
                # these maxels are not sized very well:
                maxel = im.crop(x*50, y*50, x*50+50, y*50+50)
                stat = ImageStat.Stat(maxel)

                # value of maxel, normalized to the values of the
                # pixels we have:
                value = floor(stat.mean[0]/(255/maxels.len())))
                
                # grab the pre-defined pixel
                subpath = values[value]

                # add the x, y of the current maxel to it
                for point in subpath:
                    point *= 12 # value is only 4 wide, needs to be up to 50
                    point += Point(x,y)

                # append those to path
                self.path.extend(subpath)



    """break the image into big pixels - like one cm square to start
    compute the average brightness of each pixel
    sequentially find the value of the top left corner of each pixel
    add that coordinate to each point in a raster path list Point
    append that list to the path list
    now trace all those points.
    """


