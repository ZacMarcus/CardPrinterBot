# CardPrinterBot

Prints the RFID tag onto the card to make signing up to HSBNE easier. Made mostly by ChatGPT 4.

Card printer is a Zebra P330i https://www.zebra.com/ap/en/support-downloads/printers/card/p330i.html

# Setup
Made to run on a Rasberry PI 4
* Install Python

Run the following:
* pip install pyserial
* pip install Pillow

# Rasberry PI


# Rasberry PI info (not working)
* pip install pycups --use-pep517

Ensure I2C is enabled on the Rasberry PI
* Run sudo raspi-config
* Go to "Interfacing Options" and select "Serial"
* Choose "No" for "Would you like a login shell to be accessible over serial?"
* Choose "Yes" for "Would you like the serial port hardware to be enabled?"
* Exit the configuration tool and reboot your Raspberry Pi

Rasberry PI pinout
* VCC PIN 2
* Ground PIN 6
* Tx PIN 10
* Card printer connected to USB

Printer
* Set the card printer to be the default printer
  * PI > Preferences > Print Settings > Add > ZEBRA CARD
  * Choose Zebra driver (you have to scroll down)
  * EPL1 Label

Running
* Copy CardPrinterBot.py and arial.ttf into the home directory on the Rasberry PI 4
* Ensure CardPrinterBot.py is run on startup
  * Edit /home/<user>/.bashrc
  * Go to the last line of the script and add:
    * echo Running CardPrinterBot at boot
    * python /home/pi/CardPrinterBot.py
