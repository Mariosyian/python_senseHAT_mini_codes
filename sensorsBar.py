
#!/usr/bin/python3
from sense_hat import SenseHat
import time

# Set colors
e = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)     # temperature
g = (0, 255, 0)     # pressure
b = (0, 0, 255)     # humidity

# Set matrix of colors
data = [
  # Temperature
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
  # Humidity
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e,
  # Pressure
e, e, e, e, e, e, e, e,
e, e, e, e, e, e, e, e
]

def get_temp_bar():
  t = []
  if -5.0 <= celsius and celsius <= 15.0:
    t = [
      r, r, r, e, e, e, e, e,
      r, r, r, e, e, e, e, e,
      r, r, r, e, e, e, e, e
    ]
  elif 15.0 < celsius and celsius <= 45.0:
    t = [
      r, r, r, r, r, r, e, e,
      r, r, r, r, r, r, e, e,
      r, r, r, r, r, r, e, e
    ]
  else:
    t = [
      r, r, r, r, r, r, r, r,
      r, r, r, r, r, r, r, r,
      r, r, r, r, r, r, r, r
    ]
  
  return t

def get_humi_bar():
  h = []
  if -5.0 <= humid and humid <= 10.0:
    h = [
      b, b, b, e, e, e, e, e,
      b, b, b, e, e, e, e, e,
      b, b, b, e, e, e, e, e
    ]
  elif 10.0 < humid and humid <= 20.0:
    h = [
      b, b, b, b, b, b, e, e,
      b, b, b, b, b, b, e, e,
      b, b, b, b, b, b, e, e
    ]
  else:
    h = [
      b, b, b, b, b, b, b, b,
      b, b, b, b, b, b, b, b,
      b, b, b, b, b, b, b, b
    ]
  
  return h

def get_press_bar():
  t = []
  if 0 <= pressure and pressure <= 600.0:
    p = [
      g, g, g, e, e, e, e, e,
      g, g, g, e, e, e, e, e
    ]
  elif 600.0 < pressure and pressure <= 1150.0:
    p = [
      g, g, g, g, g, g, e, e,
      g, g, g, g, g, g, e, e
    ]
  else:
    p = [
      g, g, g, g, g, g, g, g,
      g, g, g, g, g, g, g, g
    ]
  
  return p

sense = SenseHat()
sense.clear()

while True:
  celsius = sense.get_temperature()
  humid = sense.get_humidity()
  pressure = sense.get_pressure()

  message = "Temp: %.1f C, Humidity: %.2f, Pressure: %f" % (celsius, humid, pressure)
  print(message)

  data = get_temp_bar() + get_humi_bar() + get_press_bar()
  sense.set_pixels(data)
  time.sleep(1)