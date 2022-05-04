#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Get correspondance between Wifi channels and frenquencies
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################

def get_chan_frenquency(chan_number):
    """
    return the frequency associeted to the wifi channel number
    """
    switcher = { 
        1: 2.412, 
        2: 2.417, 
        3: 2.422,
        4: 2.427,
        5: 2.432, 
        6: 2.437, 
        7: 2.442,
        8: 2.447,
        9: 2.452, 
        10: 2.457, 
        11: 2.462,
        12: 2.467,
        13: 2.472,
        14: 2.484
    }
    return switcher.get(chan_number, "void")


def get_chan_number(freq):
    """
    return the frequency associeted to the wifi channel number
    """
    switcher = { 
        2.412:1, 
        2.417:2, 
        2.422:3,
        2.427:4,
        2.432:5, 
        2.437:6, 
        2.442:7,
        2.447:8,
        2.452:9, 
        2.457:10, 
        2.462:11,
        2.467:12,
        2.472:13,
        2.484:14
    }
    return switcher.get(freq, "void")