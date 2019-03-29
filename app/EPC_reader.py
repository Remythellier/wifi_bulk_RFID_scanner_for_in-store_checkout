#!/usr/bin/env python

# EPC reader
# __ Description: Listens to keyboard inputs and parses EPC code
# __ Status: Prototype
# __ Author: Remy Thellier
# __ Email: remythellier@gmail.com
# __ Licence: MIT

from pynput import keyboard # this library genetates multiple threads when listening to the key so it need to run in the main thread

import cart_manager

keys_buffer = ""
     
def on_press(key):
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener
    hexa_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if k in hexa_keys:
        # the key "k" just got pressed
        add_to_EPC_parser(k)

def add_to_EPC_parser(key):
    global keys_buffer
    keys_buffer = keys_buffer + key
    if len(keys_buffer) >= 24:
        EPC = keys_buffer[:24]
        print('EPC Detected: ' + EPC)
        cart_manager.empty_cart_if_old(300)
        cart_manager.add_new_EPC_to_cart(EPC)
        if len(keys_buffer) >= 26 and keys_buffer[len(keys_buffer)-2:] == "30":
            keys_buffer = keys_buffer[len(keys_buffer)-2:]

def run():
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread
    lis.join() # no this if main thread is polling self.keys