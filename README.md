# ledEmulator

An initial attempt at a 64x64 bit emulator for an LED screen

The functions include:

## drawGrid()
This refreshes the entire grid with the contents of the 2D list called ledscreen.grid

## drawPixel(row,col, colour)
This draws a single pixel and updates the internal grid array for future reference.
It also stores a list of changes, so that updates are optimised.
Colour can be either names like "red", [r,g,b] or "#FF0000" style hex strings 

## refresh()
This draws the display, only altering the areas for updated pixels.

## endWait()
Makes the program pause until Esc is pressed

## tick(fps)
Slows down the program to the desired fps

