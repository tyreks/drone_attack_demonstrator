#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Listing of the available Wifi networks
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################

# devices
from drn_nw_utils import *

# managed and monitoring interfaces
MNG_INTERF  = 'wlan0'
MON_INTERF  = MNG_INTERF+'mon'

def main():
    restore_interf(MNG_INTERF)
    start_mon(MNG_INTERF)
    dump_all_nw(MON_INTERF, 10, 'dump_nw_list')
    restore_interf(MNG_INTERF)

if __name__ == "__main__":
    main()