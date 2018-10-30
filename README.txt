README.TXT


This is the README.txt for the Weather Station
Created by Austin Salois, Sonoma State SCI220, Fall 2018


This project was created in collaboration Chris Halle for the Science 220
partner project. The purpose of this project was to create a portable
easy to use Weather Station to collect local data on Fairfield Osborn Preserve.
While there is a weather station on said preserve, it is useful to have
data specified for the exact area you are working in. The end product
was designed to be modular, easily adaptable for more sensors, easy to use and
low cost so multiple could be made for use during research on the preserve.
Some guides used for this build are linked below for future use in
troubleshooting any issues with the portable weather station.


•Language(s) Used:
  Python
  Linux (Raspbian Jessie Lite)


•Software Needed:
  Filezilla (https://filezilla-project.org)
    *Guide for Filezilla can be found below
  WeatherStation.py


•Hardware:
  Raspberry Pi 3B+
  DHT11 - Temperature and Humidity sensor
  DS3231 - Real Time Clock module
  Various switches, LEDS and buttons


•Online Guides Used for Sensors:
  https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/

  https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/overview


•FileZilla Guide:
  Filezilla is used for pulling the collected data in CSV format off of the
  raspberry pi used for collecting the data. This program is known as a
  an FTP client. FTP stands for 'File Transfer Protocol' and it is a way to
  connect remotely and be able to transfer the file to your computer. This way,
  no external keyboard and screen is required to save and transfer the data.

  Opening FileZilla, you will be greeted with a window sectioned off into
  3 main windows. The top section, that stretches across the top, is where
  information pertaining to your connection will be displayed, we wont be
  worry about it. The next section down is 1 window, split down the middle.
  These windows are the important ones. The window on the left is your local
  machine. It acts like a normal file explorer, like how you would browse
  for files on your computer. The window on the right side is where you will
  browse for files on the Raspberry Pi once we connect to it. The bottom window
  that stretches across the bottom we will ignore as well.

  At the top there is multiple boxes labeled, 'Host', 'Username', 'Password'
  and 'Port'.

  Enter the following inputs into these fields.
  Host = '...'
  Username = '...'
  Password = '...'
  Port = '...'

  Click 'Quickconnect'

  The top banner with network information displayed, we can ignore.
  Once connected, in the middle window on the right, you will see a file
  explorer for the Raspberry Pi you are now connected to.

  Navigate to the Weather Station folder located on the Pi. In this folder
  is all the files associated with the Weather station. The data is
  stored inside the folder labeled "OutputData"

  Inside this folder will be all the data that is collected. The program
  names the files in the following format:
  WeatherData;yyyy-mm-dd.csv

  The date that corresponds the file name is only the date on which the
  data collection was started. If data was collected over multiple days,
  then the date in the name will contain the name of which the collection
  was started. There will not be a file for every new day of data collection,
  if the data was collected continuously.

  To transfer the data to your local machine, you can click and drag the file
  to the left, into the folder you would like to put it in. This is exactly how
  you would move files normally. The file will transfer and will now be on your
  local machine.

  It is important to keep the data on the Pi organized and cleaned up. While
  you can keep the data on there, it is a good idea to delete older files you
  have already transferred as to decrease clutter.

  You can close FileZilla when you are done without worrying about having to
  disconnect. You can reconnect at anytime to transfer future data in the same
  way outlined above.
