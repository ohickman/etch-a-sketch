etch-a-sketch
=============
Robot control for Etch-a-sketch.
This program controls stepper motors to draw on an Etch-a-sketch.

If you want to build your own computer controlled Etch-a-sketch you'll need:
* a Raspberry Pi (http://www.raspberrypi.org/)
* some stepper motors with control boards
* an Etch-a-sketch
* synchronous drive belts and pulleys.  I used these:
** http://www.mcmaster.com/#timing-belt-pulleys/=q4fvzy
** http://www.mcmaster.com/#timing-belts/=q4fvyq
* a frame to hold it all together: I used this system:
** http://www.microrax.com/ (there are other options too)

If you want to extend the program by writing your own path generator here is some info:

I'm implementing a strategy pattern (http://en.wikipedia.org/wiki/Strategy_pattern, and http://codereview.stackexchange.com/questions/20718/the-strategy-design-pattern-for-python-in-a-more-pythonic-way) so that the big ugly path generators are all stuck in the "render_strategy.py" file, leaving the Render() object relatively clean.

When paths are drawn points are followed in order and connected by straight lines computed with Bressenham's line algorihm (http://en.wikipedia.org/wiki/Bresenham%27s_algorithm).  The algorithm is modified so that rather than returning the coordinates of each point on the line, it returns a list of Point() objects where x, y are -1, 0, 1 and represent single steps by the stepper motor.

The RPi.GPIO library is from Adafruit and available via GitHub.  (https://github.com/adafruit).

If you are new to the Rasbperry Pi then checkout Adafruit's tutorials (http://learn.adafruit.com/category/raspberry-pi), starting with their setup of the Raspberry Pi if you need a comprehensive introduction (http://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi).

Enjoy,
Oliver
