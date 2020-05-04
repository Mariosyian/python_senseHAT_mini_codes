#!/usr/bin/python3
from sense_hat import SenseHat
import time
import math

sense = SenseHat()

while True:
  #orientation = sense.get_orientation()
  #print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

  raw = sense.get_gyroscope_raw()
  print("x: {x}, y: {y}, z: {z}".format(**raw))
  time.sleep(0.5)
