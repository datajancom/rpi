# raspberry pi sense hat

from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Define colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
magenta = (226, 0, 116)
black = (0, 0, 0)

# Take readings from all three sensors
t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

# Round the values to one decimal place
t = round(t, 1)
p = round(p, 1)
h = round(h, 1)

message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

# Get accelerometer data
acceleration = sense.get_accelerometer_raw()
x = acceleration['x']
y = acceleration['y']
z = acceleration['z']

x=round(x, 0)
y=round(y, 0)
z=round(z, 0)

#print("x={0}, y={1}, z={2}".format(x, y, z))

while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":

      # Check which direction
      if event.direction == "up":       # Up arrow
        sense.show_message(str(t), text_colour=magenta, back_colour=black, scroll_speed=0.1)
      elif event.direction == "down":   # Down arrow
        sense.show_message("x={0}, y={1}, z={2}".format(x, y, z), text_colour=magenta, back_colour=black, scroll_speed=0.1)
      elif event.direction == "left":   # Left arrow
        sense.show_message(str(p), text_colour=magenta, back_colour=black, scroll_speed=0.1)
      elif event.direction == "right":  # Right arrow
        sense.show_message(str(p), text_colour=magenta, back_colour=black, scroll_speed=0.1)
      elif event.direction == "middle": # Enter key
        sense.show_message(message, text_colour=magenta, back_colour=black, scroll_speed=0.1)

      # Wait a while and then clear the screen
      sleep(1)
      sense.clear()

sense.clear()
