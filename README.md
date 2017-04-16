# Harmonograph
A simple simulation of a harmonograph.

# Requirements
Begin by installing `numpy` and `pygame`.

# How to run it
While standing in the root directory, run

`python3 main.py nicesimulations/s14.in pics/outPicture.jpeg 3 1 0 src/brush.png`

which should result in the following:

![alt text](https://github.com/imarkstrom/Harmonograph/tree/master/pics/outPicture.jpeg "Result of simulation")

If this works, good.
`main.py` is the root program, then we have the input simulation settings file (please write your own ones), then the location where to save the outputed image.
The first number is which of the coordination generators to use, where `0` is the simplest one.
The second number is the color scheme used, where some exists already (like.. 0..8 or something. The first one is white, then red, green, and then some more advanced ones).
The third number is how long part-lines should be, where a value of zero gives continuous lines. Worth noting !If you add your custom coordinate or color to the user_defined file, you can access those by placin a "u" in front of the number!.
The last one is if you want to have a custom brush. Remember, it is roughly a 8x8 pixel sized png with transperency, but you can create your own. Some different brushes exist in the folder, which will be moved later.

The simulation runs to the end, and is exited via the terminal. Crude, but it works.
Only one color scheme is available for now. Will be customizeable later on (it is now, in the userdefined_coordinate_creators file!).

`python3 main.py nicesimulations/s14.in pics/newPicture1.jpeg 3 u0 0 src/brush.png`

This would run a simulation with the third coordinate generator, with a user defined color scheme (number 0).