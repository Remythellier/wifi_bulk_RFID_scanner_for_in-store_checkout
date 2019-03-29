#!/usr/bin/env python

# Server
# __ Description: Rest server that gives status on GET at /status/ and sends the list of items in the cart before reseting the cart on GET at /42$cart
# __ Status: Prototype
# __ Author: Remy Thellier
# __ Email: remythellier@gmail.com
# __ Licence: MIT

from flask import Flask, request
from flask_restful import Resource, Api

import cart_manager

app = Flask(__name__)
api = Api(app)

class getCart(Resource):
    def get(self):
        cart = cart_manager.get_cart()
        cart_manager.empty_cart()
        return {'cart': cart}

class getStatus(Resource):
    def get(self):
        return {'status': "live"}

api.add_resource(getCart, '/42$cart')
api.add_resource(getStatus, '/status/')

def run():
    app.run(host="0.0.0.0", debug=False)