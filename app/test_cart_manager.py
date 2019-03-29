import unittest

import cart_manager
import time
import datetime



class TestGetcart(unittest.TestCase):
    
    def test_returning_empty_cart(self):
        cart_manager.items_EPCs_in_cart = []
        self.assertEqual(cart_manager.empty_cart(), True, "It should return an empty list")
        self.assertEqual(cart_manager.items_EPCs_in_cart, [], "The current cart should be empty")

    def test_returning_full_cart(self):
        cart_manager.items_EPCs_in_cart = ['30396062C3A624C0006328ED']
        self.assertEqual(cart_manager.get_cart(), [{'EAN13': '3608439565632', 'serial': '6498541'}], "It should return a list")

class TestEPCsToEAN13andSerial(unittest.TestCase):
   
    def test_return_right_values(self):
        self.assertEqual(cart_manager.EPC_list_to_EAN13_and_Serial(['30396062C3A624C0006328ED']), [{'EAN13': '3608439565632', 'serial' : '6498541' }], "This is not the right Serial and EAN13")
        #add test with multiple items in the cart

class TestCheckUnique(unittest.TestCase):

    def test_empty_cart(self):
        cart_manager.items_EPCs_in_cart = []
        self.assertEqual(cart_manager.is_EPC_not_in_cart('30396062C3A62F4C000630DAF3'), True, "Should be Added")

    def test_item_already_in_cart(self):
        cart_manager.items_EPCs_in_cart = ['30396062C3A62F4C000630DAF3']
        self.assertEqual(cart_manager.add_new_EPC_to_cart('30396062C3A62F4C000630DAF3'), False, "Should not be Added")
        self.assertEqual(cart_manager.items_EPCs_in_cart, ['30396062C3A62F4C000630DAF3'], "cart should not contain those items")

    def test_item_already_in_big_cart(self):
        cart_manager.items_EPCs_in_cart = ['30396062C3A62F4C000630DAF3', '30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3' ]
        self.assertEqual(cart_manager.add_new_EPC_to_cart('30396062C3A62F4C000630DAF3'), False, "Should not be Added")
        self.assertEqual(cart_manager.items_EPCs_in_cart, ['30396062C3A62F4C000630DAF3', '30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3'], "cart should not contain those items")

    def test_item_not_already_in_big_cart(self):
        cart_manager.items_EPCs_in_cart = ['30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3' ]
        self.assertEqual(cart_manager.add_new_EPC_to_cart('30396062C3A62F4C000630DAF3'), True, "Should be Added")
        self.assertEqual(cart_manager.items_EPCs_in_cart, ['30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3', '30396062C3A62F4C000630DAF3'], "cart should not contain those items")
        #the new item is added at the end of the cart


class TestEmptycartIfOld(unittest.TestCase):

    def test_cartIsNotOld(self):
        cart_manager.items_EPCs_in_cart = ['30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3' ]
        cart_manager.last_unique_item_timestamp = datetime.datetime.now() - datetime.timedelta(seconds=200)  
        self.assertEqual(cart_manager.empty_cart_if_old(300), False, "cart should not be empty")
        self.assertEqual(cart_manager.items_EPCs_in_cart, ['30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3' ], "The cart should be unchanged")

    def test_cartIsOld(self):
        cart_manager.items_EPCs_in_cart = ['30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3' ]
        cart_manager.last_unique_item_timestamp = datetime.datetime.now() - datetime.timedelta(seconds=800)  
        self.assertEqual(cart_manager.empty_cart_if_old(300), True, "cart should be empty")
        self.assertEqual(cart_manager.items_EPCs_in_cart, [], "There should not be any item in the cart")


class TestEmptycartIfOld(unittest.TestCase):

    def test_cartIsNotOld(self):
        cart_manager.items_EPCs_in_cart = ['30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3' ]
        cart_manager.last_unique_item_timestamp = datetime.datetime.now() - datetime.timedelta(seconds=200)  
        self.assertEqual(cart_manager.empty_cart_if_old(300), False, "cart should not be empty")
        self.assertEqual(cart_manager.items_EPCs_in_cart, ['30396062C8A62F4C000630DAF3', '30396062C3A62F4C900630DAF3' ], "The cart should be unchanged")

if __name__ == '__main__':
    unittest.main()