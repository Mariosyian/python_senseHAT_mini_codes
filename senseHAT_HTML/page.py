#!/usr/bin/python3
from bs4 import BeautifulSoup
from sense_hat import SenseHat

import time

sense = SenseHat()

# Repeat every 10 seconds
while True:
  # load the file
  html = open("index.html").read()
  soup = BeautifulSoup(html, "html.parser")

  # get sensor data
  temp = round(sense.get_temperature(), 2)
  humidity = round(sense.get_humidity(), 2)

  # find html elements
  temp_p = soup.find(id="temp")
  humidity_p = soup.find(id="humidity")

  # rewrite content into tags
  temp_p.string = 'Temperature: ' + str(temp)
  humidity_p.string = 'Humidity: ' + str(humidity)

  # write back to file
  with open("index.html", "w") as file:
    file.write(str(soup))

  time.sleep(10)