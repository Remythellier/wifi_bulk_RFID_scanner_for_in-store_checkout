Wifi bulk RFID scanner for in-store checkout

Project Trolley is a standalone, mobile, RFID-based, bulk item scanning device that feeds on request the cart of a payment mobile app used in-store. 
It targets stores with mobile smartphone-based requiring one by one item scanning and having RFID tagged products.
It allows instant scanning of a large number of items speeding-up drastically the checkout process from anywhere in the store.

First a basket full of products needs to be entirely inserted in the trolley
 // the trolley’s embedded RFID reader  scans all the products and stores the information
Secondly the QR code located on the trolley should be scanned by sales-rep’s phone using the checkout app.
  // On scan the checkout app asks the trolley to feed its cart with the item scanned
The all the basket’s items now appear in the checkout app, the payment process can now start


--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------


// SETUP  //

pip install pynput
pip install flask
pip install flask_restful

This works on a private network, the computer needs to be connected to a network and to have a static IP
The static IP needs to be set in the server.py module

--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------


// START //

run the application:
python app.js

run the tests:
python test.js


--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------

// MODULES //

Libraries
---------

pynput is the library used to monitor the keyboard inputs (in that case the RFID reader that acts as a keyboard)

flask and flask_restful allows us to build a lightweight RESTfull API

time allows us to use the current time

import datetime allows us to easily do operations on dates

threading allows us to separate our program with:
- the webserver runing independently on one thread
- the rest the main thread 
/ please note that the key listener's library (pynput) already uses threading so other threads are generated from it, this is why the listener can't be put in a separate thread

unittest - allows us to set and run unit tests

Custom modules
--------------

app.py - starts the program

EPCreader.py - listen to the inputs from the reader and detect EPC codes

basketManager.py - fill in a virtual cart with the unique EPCs, the buffer is time sensitive

EPCconverter.py - convert EPCs into EAN13 and Serial codes

server.py - API allowing communication with app 

tests.py - unit tests 

--------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------
