#!/usr/bin/env python

# Cart Manager
# __ Description: Manages the virtual cart filled with the items scanned
# __ Status: Prototype
# __ Author: Remy Thellier
# __ Email: remythellier@gmail.com
# __ Licence: MIT

import time
import datetime

import EPC_converter

items_EPCs_in_cart = []
last_unique_item_timestamp = datetime.datetime.now()

def empty_cart():
    items_EPCs_in_cart = []
    return True

def get_cart():
    global items_EPCs_in_cart
    if len(items_EPCs_in_cart) > 0:
        cart = EPC_list_to_EAN13_and_Serial(items_EPCs_in_cart)
        return cart
    else:
        print('cart is already empty, try again...')
        return []

def EPC_list_to_EAN13_and_Serial(EPC_list):
    EAN13_and_serial_list = []
    for EPC in EPC_list:
        EAN13_and_serial = EPC_converter.EPC_decoder(EPC)
        EAN13_and_serial_list.append(EAN13_and_serial)
    return EAN13_and_serial_list

def is_EPC_not_in_cart(EPC):
    global items_EPCs_in_cart
    if EPC in items_EPCs_in_cart:
        print('Item already in the cart')
        return False
    else:
        return True

def add_new_EPC_to_cart(EPC):
    global last_unique_item_timestamp
    global items_EPCs_in_cart
    if is_EPC_not_in_cart(EPC):
        items_EPCs_in_cart.append(EPC)
        last_unique_item_timestamp = datetime.datetime.now()
        return True
    else:
        return False

def empty_cart_if_old(max_in_seconds):
    global last_unique_item_timestamp
    if last_unique_item_timestamp < datetime.datetime.now() - datetime.timedelta(seconds=max_in_seconds):
        empty_cart()
        print('The cart just got erased because it was too old')
        return True
    else:
        return False