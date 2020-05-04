#!/usr/bin/python3
from sense_hat import SenseHat
import time

# Set colors
e = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
y = (255, 255, 0)

# Set matrix of colors
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

excl = [
e, e, e, w, w, e, e, e,
e, e, e, w, w, e, e, e,
e, e, e, w, w, e, e, e,
e, e, e, w, w, e, e, e,
e, e, e, w, w, e, e, e,
e, e, e, e, e, e, e, e,
e, e, e, w, w, e, e, e,
e, e, e, w, w, e, e, e
]

# Initiliase SenseHAT
sense = SenseHat()
sense.clear()

while True:
  # Set pixel colors
  sense.set_pixels(pika)
  time.sleep(.75)
  # Rotate
  # 360 degrees = 0 degress
  if (sense.rotation == 270):
    sense.rotation = 0
    time.sleep(.75)
    sense.set_pixels(excl)
    break
  else:
    sense.rotation = sense.rotation + 90

time.sleep(1)
sense.clear()
