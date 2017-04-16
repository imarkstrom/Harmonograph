# Harmonograph
A simple simulation of a harmonograph.

# Requirements
Begin by installing `numpy` and `pygame`.

# How to run it
While standing in the root directory, run
`python3 main.py nicesimulations/s12.in pics/newPicture1.jpeg 1 0 src/yellowbrush.png`

If this works, good.
`main.py` is the root program, then we have the input simulation settings file (please write your own ones), then the location where to save the outputed image. The first number is which of the coordination generators to use, where `0` is the simplest one. The second number is how long part-lines should be, where a value of zero gives continuous lines. The last one is if you want to have a custom brush. Remember, its an 8x8 pixel sized png with transperency. The size of the generated image is for now set in the input file, which will be moved later.

