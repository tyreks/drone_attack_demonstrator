#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Raodio jamming
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################

# https://fccid.io site qui reference les FCC ID (10 char qui caractérisent un terminal réseau 
# notamment le mode de modulation et la fréquence)

import subprocess
import time

from rflib import *
from pwn import *



d = RfCat(idx=0)
#d.ping()
time.sleep(.300)
d.setMdmChanSpc(24000)

time.sleep(.300)
d.setMdmModulation(MOD_2FSK)#MOD_ASK)

time.sleep(.300)
d.setMdmDRate(1.0/0.0006)

time.sleep(.300)
d.setMaxPower()

time.sleep(.300)
d.setRFRegister(PA_TABLE0, 0xFF)

time.sleep(.300)
d.setRFRegister(PA_TABLE1, 0xFF)

time.sleep(.300)
d.makePktFLEN(255)

start = time.time()
try:
    time.sleep(.300)
    d.setModeTX()
    
    time.sleep(300)
    
    d.setModeIDLE()
except :#rflib.chipcon_usb.ChipconUsbTimeoutException:
    d.setModeIDLE()

d.cleanup()


"""
progress_state = log.progress("Jamming in progress...")
try:
except rflib.chipcon_usb.ChipconUsbTimeoutException:
    progress_state.failure("USB timeout")
except Exception as e:
    progress_state.failure(e.traceback.format_exc())

log.success()

d.setModeIDLE()
"""

