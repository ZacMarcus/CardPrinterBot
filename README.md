# CardPrinterBot

Prints the RFID tag onto the card to make signing up to HSBNE easier. Made mostly by ChatGPT 4.

# Setup
Made to run on a Rasberry PI 4
* Install Python

Run the following:
* pip install pyserial
* pip install Pillow
* pip install pycups

Ensure I2C is enabled on the Rasberry PI
* Run sudo raspi-config
* Go to "Interfacing Options" and select "Serial"
* Choose "No" for "Would you like a login shell to be accessible over serial?"
* Choose "Yes" for "Would you like the serial port hardware to be enabled?"
* Exit the configuration tool and reboot your Raspberry Pi

# Printer
* Set the card printer to be the default printer

# Running
* Copy CardPrinterBot.py and arial.ttf into the home directory on the Rasberry PI 4
* Ensure CardPrinterBot.py is run on startup
  * Edit /home/<user>/.bashrc
  * Go to the last line of the script and add:
    * echo Running CardPrinterBot at boot
    * python /home/pi/CardPrinterBot.py

# Rasberry PI pinout
* VCC PIN 2
* Ground PIN 6
* Tx PIN 10
