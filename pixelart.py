#!/usr/bin/python3
from sense_hat import SenseHat
import time

# Set pixel colors
e = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
y = (255, 255, 0)
p = (255,105, 180)

# Set matrix of colors
heart = [
e, e, w, e, e, e, w, e,
e, w, r, w, e, w, r, w,
e, w, r, r, w, r, r, w,
e, w, r, r, r, r, r, w,
e, e, w, r, r, r, w, e,
e, e, e, w, r, w, e, e,
e, e, e, e, w, e, e, e,
e, e, e, e, e, e, e, e
]

p_heart = [
e, e, w, e, e, e, w, e,
e, w, p, w, e, w, p, w,
e, w, p, p, w, p, p, w,
e, w, p, p, p, p, p, w,
e, e, w, p, p, p, w, e,
e, e, e, w, p, w, e, e,
e, e, e, e, w, e, e, e,
e, e, e, e, e, e, e, e
]

pika = [
e, e, y, y, y, y, e, e,
e, y, y, y, y, y, y, e,
y, y, e, y, y, e, y, y,
y, y, y, y, y, y, y, y,
y, r, y, y, y, y, r, y,
y, e, y, y, y, y, e, y,
y, y, e, e, e, e, y, y,
y, y, y, y, y, y, y, y
]

# Initialise SenseHat
sense = SenseHat()
sense.clear()
counter = 0
# Set pixels to matrices
while (counter < 5):
  sense.set_pixels(heart)
  time.sleep(.75)
  sense.set_pixels(p_heart)
  time.sleep(.75)
  sense.set_pixels(pika)
  time.sleep(.75)
  counter = counter + 1

sense.show_message("Goodbye!")
sense.clear()