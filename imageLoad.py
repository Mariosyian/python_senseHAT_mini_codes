#!/bin/usr/python3

from sense_hat import SenseHat
import time

sense = SenseHat()

sense.clear()

while True:
  sense.load_image("images/ghost.png")
  time.sleep(2)
  sense.load_image("images/strawberry.png")
  time.sleep(2)
