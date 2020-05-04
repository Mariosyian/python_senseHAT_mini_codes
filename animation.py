#!/bin/usr/python3
from sense_hat import SenseHat
import time

sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)
y = (255, 255, 0)
b = (0, 0, 255)
gr = (200, 200, 200)

frame1 = [
gr, gr, e, e, e, e, gr, gr,
gr, e, y, y, y, y, e, gr,
e, y, y, w, b, y, y, e,
e, y, y, w, b, y, y, y,
e, y, y, y, y, y, y, y,
e, y, y, y, y, y, y, e,
gr, e, y, y, y, y, e, gr,
gr, gr, e, e, e, e, gr, gr
]


frame2 = [
gr, gr, e, e, e, e, gr, gr,
gr, e, y, y, y, y, e, gr,
e, y, y, b, w, y, y, e,
e, y, y, b, w, y, y, y,
e, y, y, y, y, y, y, y,
e, y, y, y, y, y, y, e,
gr, e, y, y, y, y, e, gr,
gr, gr, e, e, e, e, gr, gr
]

frame3 = [
gr, gr, e, e, e, e, gr, gr,
gr, e, y, y, y, y, e, gr,
e, y, y, b, w, y, y, e,
y, y, y, b, w, y, y, e,
y, y, y, y, y, y, y, e,
e, y, y, y, y, y, y, e,
gr, e, y, y, y, y, e, gr,
gr, gr, e, e, e, e, gr, gr
]

frame4 = [
gr, gr, e, e, e, e, gr, gr,
gr, e, y, y, y, y, e, gr,
e, y, y, w, b, y, y, e,
y, y, y, w, b, y, y, e,
y, y, y, y, y, y, y, e,
e, y, y, y, y, y, y, e,
gr, e, y, y, y, y, e, gr,
gr, gr, e, e, e, e, gr, gr
]

# Set upright
sense.rotation = 90

while True:
  sense.set_pixels(frame1)
  time.sleep(1)
  sense.set_pixels(frame2)
  time.sleep(1.5)
  sense.set_pixels(frame3)
  time.sleep(1)
  sense.set_pixels(frame4)
  time.sleep(1.5)
