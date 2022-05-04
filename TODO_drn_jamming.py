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
# notamment le mode de modulation et la fréquence   )

from rflib import *
import subprocess

d = RfCat(idx=0)

d.setMdmChanSpc(24000)

d.setMdmModulation(MOD_2FSK)#MOD_ASK)

d.setMdmDRate(1.0/0.0006)

d.setMaxPower()

d.setRFRegister(PA_TABLE0, 0xFF)

d.setRFRegister(PA_TABLE1, 0xFF)

d.makePktFLEN(255)

try:
    subprocess.run("d.setModeTX()", timeout=5)
except subprocess.TimeoutExpired:
    progress_state.success()
except Exception as e:
    progress_state.failure(e.traceback.format_exc())

d.setModeIDLE()


