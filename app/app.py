#!/usr/bin/env python

# App
# __ Description: Starts the application with a webserver in one thread and the rest of the app in the main one (command: python app.py)
# __ Status: Prototype
# __ Author: Remy Thellier
# __ Email: remythellier@gmail.com
# __ Licence: MIT

import threading

import server
import EPC_reader

thread = threading.Thread(target=server.run)
thread.start()
EPC_reader.run()
