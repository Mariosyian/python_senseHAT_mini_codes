#!/usr/bin/python3
from sense_hat import SenseHat
import dis

sense = SenseHat()

fahrenheit = sense.get_temperature()
celsius = (fahrenheit - 32) * 5 / 9

message = "Temp: %.2f" % (fahrenheit)
sense.show_message(message)
