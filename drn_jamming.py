#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Radio jamming using Yardstick and rfcatlib
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################

# https://fccijammer.io site qui reference les FCC ID (10 char qui caractérisent un terminal réseau 
# notamment le mode de modulation et la fréquence)

import signal

from rflib import *
from pwn import *

jammer = RfCat(idx=0)

def prepare_jam(
    mod=MOD_2FSK
    , chan_spc=24000, d_rate=1.0/0.0006, pkt_flen=255
    , RFRegister0=0xFF, RFRegister1=0xFF):
    """
    set parameters before jamming with rfcat
    """
    global jammer
    jammer.setMdmModulation(mod)#MOD_ASK)
    jammer.setMdmChanSpc(chan_spc)
    jammer.setMdmDRate(d_rate)
    jammer.makePktFLEN(pkt_flen)
    jammer.setRFRegister(PA_TABLE0, RFRegister0)
    jammer.setRFRegister(PA_TABLE1, RFRegister1)
    jammer.setMaxPower()


def start_jam(duration:int=10):
    global jammer
    #signal.signal(signal.SIGALRM, handler)
    signal.alarm(duration)
    try:
        jammer.setModeTX()
    except rflib.chipcon_usb.ChipconUsbTimeoutException:
        pass
    

def stop_jam():
    global jammer
    jammer.ping()
    #jammer.setModeIDLE()

"""
progress_state = log.progress("Jamming in progress...")
try:
except rflib.chipcon_usb.ChipconUsbTimeoutException:
    progress_state.failure("USB timeout")
except Exception as e:
    progress_state.failure(e.traceback.format_exc())

log.success()

jammer.setModeIDLE()
"""

def main():
    prepare_jam()
    print("ok")
    #start_jam()
    #stop_jam


if __name__ == "__main__":
    main()