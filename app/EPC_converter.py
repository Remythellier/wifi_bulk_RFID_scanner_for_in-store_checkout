#!/usr/bin/env python

# EPC converter
# __ Description: Converts the EPC hexadecimal code of RFID-identified merchandize to its EAN13 and Serial decimal code.
# __ Status: Prototype
# __ Author: Remy Thellier
# __ Email: remythellier@gmail.com
# __ Licence: MIT

def hex_to_bin(hex):
    bin = "".join(reversed( [i+j for i,j in zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+hex)][n::2] for n in [1,0] ] ) ] ))
    return bin

def bin_to_dec(bin):
    dec = int(bin, 2)
    return dec

def add_missing_zeros(string, normal_length):
    while len(string) < normal_length:
        string = "0" + string
    return string

def checksum_calculator(EAN13_without_checksum):
    total_odds = 0
    total_evens = 0
    for x in range (6):
        total_odds = total_odds + int(EAN13_without_checksum[2*x:2*x+1])
        total_evens = total_evens + int(EAN13_without_checksum[2*x+1:2*x+2])
    result = (total_evens*3) + total_odds
    last_digit = str(result)[len(str(result))-1:len(str(result))]
    if last_digit == "0":
        checksum = "0"
    else:
        checksum = str(10 - int(last_digit))
    return checksum

def EPC_decode_company_prefix(EPCbin):
    EPCbin_part1 = EPCbin[15:34]
    company_prefix = bin_to_dec(EPCbin_part1)
    return str(company_prefix)

def EPC_decode_EAN13_part2_without_checksum(EPCbin):
    EPCbin_part2 = EPCbin[35:58]
    EAN13_part2_without_checksum = bin_to_dec(EPCbin_part2)
    return str(EAN13_part2_without_checksum)

def EPC_decode_EAN13(company_prefix, EAN13_part2_without_checksum):
    company_prefix = add_missing_zeros(company_prefix, 6)
    EAN13_part2_without_checksum = add_missing_zeros(EAN13_part2_without_checksum, 6)
    EAN13_without_checksum = str(company_prefix) + str(EAN13_part2_without_checksum)
    checksum = checksum_calculator(EAN13_without_checksum)
    EAN13 = EAN13_without_checksum + checksum
    return EAN13

def EPC_decode_serial(EPCbin):
    EPCbin_part3 = EPCbin[59:96]
    serial = str(bin_to_dec(EPCbin_part3))
    return serial

def EPC_decoder(EPC):
    EPCbin = hex_to_bin(EPC)
    company_prefix = EPC_decode_company_prefix(EPCbin)
    EAN13_without_checksum_part2 = EPC_decode_EAN13_part2_without_checksum(EPCbin)
    EAN13 = EPC_decode_EAN13(company_prefix, EAN13_without_checksum_part2)
    serial = EPC_decode_serial(EPCbin)
    decoded_EPC = {"EAN13": EAN13, "serial": serial}
    return decoded_EPC
