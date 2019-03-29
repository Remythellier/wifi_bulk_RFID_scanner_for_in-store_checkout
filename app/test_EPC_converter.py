import unittest

import EPC_converter
import time
import datetime

class TestHexToBin(unittest.TestCase):

    def test_hex_to_bin(self):
        hex = "30396062C3A624C0006328ED"
        bin = "001100000011100101100000011000101100001110100110001001001100000000000000011000110010100011101101"
        self.assertEqual(EPC_converter.hex_to_bin(hex), bin, "There is a mistake in the hexadecimal to binary conversion")

class TestBinToDec(unittest.TestCase):

    def test_bin_to_dec(self):
        bin = "1011000000110001011"
        dec = 360843
        self.assertEqual(EPC_converter.bin_to_dec(bin), dec, "There is a mistake in the binary to decimal conversion")

class TestCheckSum(unittest.TestCase):

    def test_checksum(self):
        EAN13preCheckSum = "360843956563"
        checksum = "2"
        self.assertEqual(EPC_converter.checksum_calculator(EAN13preCheckSum), checksum, "The checkSum computation is wrong")

class TestEPCdecoder(unittest.TestCase):

    def test_EPCdecoder(self):
        EPC = "30396062C3A624C0006328ED"
        decoded = {'EAN13': '3608439565632', 'serial': '6498541'}
        self.assertEqual(EPC_converter.EPC_decoder(EPC), decoded, "The converter is not working properly")


if __name__ == '__main__':
    unittest.main()