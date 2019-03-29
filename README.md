# Wifi bulk RFID scanner for in-store checkout

Project Trolley is a standalone, mobile, RFID-based, bulk item scanning device that feeds on request the cart of a payment mobile app used in-store. 
It targets retail stores whose salesmen are using smartphone-based for checkout. Those mobile applications require one by one item scanning. Some store having already RFID tagged all their products.
This project allows the salesmen of those stores to instantly scan a large number of items, speeding-up drastically the checkout process from anywhere in the store.

First, a cart full of products needs to be entirely inserted in the trolley
- The trolley's embedded RFID reader scans all the products and stores the information
Secondly, the QR code located on the trolley should be scanned by the salesman’s smartphone using the checkout app.
- On scan, the checkout app asks the trolley to feed its cart with all the items previously scanned
All the cart’s items now appear in the checkout app, the payment process can now start.

--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------

# Requirements

- Raspberry Pi (with wifi connectivity)
- a USB RFID reader, that acts as a keyboard,  sending EPC codes continuously

--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------

# SETUP

sudo pip install pynput
sudo pip install flask
sudo pip install flask_restful

This works on a private network, the computer needs to be connected to a network and to have a static IP

--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------

# START

run the application:
python app.js

run the tests:
python -m unittest discover


--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------

# MODULES

## Libraries

pynput is the library used to monitor the keyboard inputs (in that case the RFID reader that acts as a keyboard)

flask and flask_restful allows us to build a lightweight RESTfull API

time allows us to use the current time

import datetime allows us to easily do operations on dates

threading allows us to separate our program with:
- the web server running independently on one thread
- the rest the main thread 
/ please note that the key listener's library (pynput) already uses threading so other threads are generated from it, this is why the listener can't be put in a separate thread

unittest - allows us to set and run unit tests

## Custom modules

app.py - starts the program

EPC_reader.py - listen to the inputs from the reader and detect EPC codes

cart_manager.py - fill in a virtual cart with the unique EPCs, the buffer is time sensitive

EPC_converter.py - convert EPCs into EAN13 and Serial codes

server.py - API allowing communication with app 

test_**.py - unit tests 

--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------

# EPC converter explanation

EAN (European Article Number) check digits (administered by GS1) are calculated by summing each of the odd position numbers multiplied by 3 and then by adding the sum of the even position numbers. 
Numbers are examined going from right to left, so the first odd position is the last digit in the code. 
The final digit of the result is subtracted from 10 to calculate the check digit (or left as-is if already zero).

ex.
checksum for 360843956563
((3+5+5+3+8+6)*3+(6+6+9+4+0+3)) 
10 - 8 = 2

--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------


