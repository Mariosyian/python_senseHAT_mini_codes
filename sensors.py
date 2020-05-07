
#!/usr/bin/python3
from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
  celsius = sense.get_temperature()
  humid = sense.get_humidity()
  pressure = sense.get_pressure()

  message = "Temp: %.1f C, Humidity: %.2f, Pressure: %f" % (celsius, humid, pressure)
  print(message)
  time.sleep(1)
