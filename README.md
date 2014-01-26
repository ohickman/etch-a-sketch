Raspberry Pi powered Etch A Sketch
==========

![Raspberry Pi powered Etch A Sketch](images/whole_thing.jpg "A Raspberry Pi powered Etch A Sketch")

* [Idea](#idea)
* [Software](#software)
  * [Running `draw.py`](#running-draw.py)
  * [Running `manual.py`](#running-manual.py)
  * [Reading the Program](#reading-the-program)
  * [Extending the Program](#extending-the-program)
* [Hardware](#hardware)
* [To Do](#to-do)
* [Links](#links)

Idea
----

As a hobby project to give me something else to think about than work when I'm
not at work (and when I am at work) I decided to automate drawing with an
[Etch A Sketch](http://www.ohioart.com/brands/etch-sketch "Magic Screen").

### Design Requirements

1. Do not modify the Etch A Sketch

   I ended up violating this requirement but in an acceptably minor way: I
   popped the white knobs off and replaced them with synchronous drive pulleys.
   When building the hardware I realized that I was going to substantially
   increase the cost and complexity of my project by trying to keep the white
   plastic knobs in place, and that on the software side there would be no
   difference.

   Most importantly the Etch A Sketch can't be modified to lift up the stylus!

2. The program itself must interpret and draw an image.

   I haven't yet implemented this part of the program.  It quickly became
   obvious that this requirement is a giant black-hole and that I could easily
   get sucked in and then never write the rest of the program.  I've written
   almost everything else and now it is time to go back and work on image
   processing.

3. The code should be clean, professional, and extensible.

   I think I achieved this fairly well!  There are a couple small
   [style inconsistencies](PEP8 http://www.python.org/dev/peps/pep-0008/ "PEP8")
   , but I'll clean those up over time.

Software
--------

### Running `draw.py`

The [draw.py](draw.py) script is the main script used to coordinate everything.
The origin is considered to be the bottom left corner of the Etch A Sketch
screen (this is the math/science convention, rather than the graphics
convention, sorry).  If the stylus is not at (0,0), then you can drive it there
using [manual.py](#running-manual.py)

To talk to the motors you need
[Adafruit's](http://www.adafruit.com/ "Limor 'Ladyada' Fried is awesome!")
[RPi.GPIO library](http://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code)
library.  There are probably other Raspberry Pi GPIO libraries, but I haven't
tried them.

Most Linux distros will require super-user privileges to use the GPIO pins on
the Raspberry Pi, so you'll need to run any program that drives a motor via
them with super-use privileges.  If you are new to Linux, remember that is done
either by running the `su` command to enter super-user mode, or to precede an
entry on the command line with `sudo`.

```
oliver@rpi:~/etch$ sudo python draw.py
```

![Hello World](images/hello_world.jpg "Hello World")


### Running `manual.py`

Just as with `draw.py`, you'll need super-user privileges to run
[`manual.py`](manual.py).

At the `?` prompt you can issue commands composed of a direction and a distance.
Directions are `u`, `r`, `d`, and `l` and are followed immediately (no space) by
the number of steps to take.

This would draw a square approximately 1cm on a side:
```
oliver@rpi:~/etch$ sudo python manual.py
? u150
? r150
? d150
? l150
```

You cannot issue serial commands like `? u50r10u100r90`.  But if you would like
to extend [`manual.py`](manual.py) to do that or anything else I would be
grateful.

### Reading the Program

This program implements a
[strategy pattern](http://en.wikipedia.org/wiki/Strategy_pattern) so all the big
ugly code that creates paths is tucked away to keep the rest of the code and the
[Render()](render.py) relatively clean.

Paths are computed, scaled to fit the screen and then drawn by connecting the
points in order in with straight lines.  The straight lines are computed with
[Bressenham's line algorihm](http://en.wikipedia.org/wiki/Bresenham%27s_algorithm "Wikipedia").
The algorithm is modified so that rather than returning the coordinates of each
point on the line, it returns a list of `Point()` objects where x, y are
-1, 0, 1 and represent single steps by the stepper motor.  With the
configuration I have set-up this produces wonderfully smooth lines as each step
is approximately 0.04mm.

* [draw.py](draw.py) coordinates the everything
* [render.py](render.py) contains the `Render()` class which generates the path
  as a list of `Point()`s and has `width` and `height` data attributes which
  don't necessarily correspond to the maximum values of `x` and `y` as an image
  might not be centered or occupy the entire dimensions of the screen.
* [point.py](point.py) defines a `Point()` class which has `x` and `y`
  attributes that are integers (Bressenham's line algorithm only really makes
  logical sense with integers)
  * `__rmul__` is implemented but not `__mul__` so if `p` is an instance of
  `Point()`, you can say `2*p` but not `p*2`.
  * you can add `+`, subtract `-`, negate `-`, and compare `=` two `Point()`s,
  but not multiply etc. since I don't know what that would mean.
* `Canvas()` is defined in [canvas.py](canvas.py) and is really just a height
  and width of the screen to set the maximum distance that the stylus can travel
  before it won't drive any further.
* `Stepper()` is defined in [stepper_driver.py](#stepper_driver.py).  The
  steppers are driven by powering a sequential pattern of its four coils.
  Those patterns are defined as `forward_sequence` and `reverse_sequence` as
  well as an `error_sequence` that can be sent to the motor to allow the program
  to continue normal operation but not move the stylus - as when the stylus has
  run outside of the limits of `Canvas()`.
* `step_bressenham()` and `compute_bressenham()` functions are defined in
  [bressenham_functions.py](bressenham_functions.py).  These aren't particularly
  long functions, but they are just long enough that pulling them out of
  [draw.py](draw.py) cleaned up the code a lot.  `compute_bressenham()` returns
  a list of `Point()`s representing the two end points and every point
  connecting them, that list can then be sent to `step_bressenham()` which will
  return a list of the moves needed to connect the ends of the line as described
  above.

### Extending the Program

Implementing your own path generator should be fairly straightforward.  A path
generator should [inherit](http://learnpythonthehardway.org/book/ex44.html "perhaps not the best strategy...")
its interface from `PathInterface` in the [path_interface.py](path_interface.py)
module, or re-implement the interface.  Specifically your path generator object
needs these public data attributes:

* `self.width()` returns a non-negative integer
* `self.height()` returns a non-negative integer
* `self.path()` returns an ordered list of [Point()](point.py) objects with
  integer values.

Your path generator then needs to be passed to be set as the
[Render object's](render.py) `path_generator` attribute either when initializing
the Render object, or via the `Render.set_path_generator()` method.

That's it!

Hardware
--------

Here is one hardware list that works:

* [Raspberry Pi](http://www.raspberrypi.org/)
* some stepper motors with control boards - the 28BYJ-48 5V stepper motor is
  pretty common and can be bought for a couple bucks with a motor driver
  included.  Don't be tempted to get the 12v version because its gearing is
  different and it doesn't have enough power.
* [Etch A Sketch](http://www.ohioart.com/brands/etch-sketch "Magic Screen")
* synchronous drive belts and pulleys. I used these:
  * http://www.mcmaster.com/#timing-belt-pulleys/=q4fvzy
  * http://www.mcmaster.com/#timing-belts/=q4fvyq
* A frame to hold it all together I really like [MicroRax](http://www.microrax.com/)

To Do
-----

- [ ] Write a method to center an image on the screen.
- [ ] Make a path simulator to output an `.svg` so that new path generators can
  be quickly tested.
- [ ] Implement path generators that read an image. (That's why I made this
  program!)
- [ ] Build something to automatically clear the screen.
- [ ] Clean up inconsistencies in coding style.

Links
-----
* If you want a little lesson about driving stepper motors with the Raspberry
  Pi, then check out [Adafruit's lessn](http://www.adafruit.com/blog/2013/01/23/adafruits-raspberry-pi-lesson-10-stepper-motors-raspberry_pi-raspberrypi/)
* [Here](http://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/)
  is where I learned about driving stepper motors, though the code isn't the best.
* If you are new to the Rasbperry Pi then check out
 [Adafruit's tutorials](http://learn.adafruit.com/category/raspberry-pi)

  If you need a comprehensive introduction then start with their
  [setup of the Raspberry Pi](http://learn.adafruit.com/adafruit-raspberry-pi-lesson-1-preparing-and-sd-card-for-your-raspberry-pi) and then do the rest of the tutorials.
* For more about the Strategy Pattern in Python check out this
  [Stack Exchange discussion](http://codereview.stackexchange.com/questions/20718/the-strategy-design-pattern-for-python-in-a-more-pythonic-way)
