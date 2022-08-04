#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# Owner     : Expleo Group
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Demonstrator home page
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
##############################################################################

import os
import sys
import time

import src.wifi.wifi_availables_nw as nw
import src.views.targeted_wifi_nw as tgt
""" has to be the last import because of a bug in 'click' external lib """
from src.views.view_tools import *



# the menus list
menus = ["Detect potential targets", "Settings", "Quit"]


def main():

    """ Main function. """
    new_page()
    # menu selection
    value = choose_menu(menus)
    if (value=='1'): # "detect targets" choice
        # detect all availables targets
        nw.detect_nw()
        time.sleep(3)
        new_page()

        # detect targets : networks hosted by drones
        tgt.main()

if __name__ == "__main__":
    main()