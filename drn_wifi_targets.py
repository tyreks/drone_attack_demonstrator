#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Listing of the potential targets in the available WiFi networks
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################

#import pandas
from drn_nw_utils import *
from pwn import *


# managed and monitoring interfaces
MNG_INTERF  = 'wlan0'
MON_INTERF  = MNG_INTERF+'mon'
TARGET_BSSID = '66:DC:12:D2:3C:1F'
TARGET_CHAN = '11'


# CSV dumping input file
CSV_DUMP    ='tst2-01.csv'

# import and sort the CSV dumping input file
#df = pandas.read_csv(CSV_DUMP, usecols=[' Power', ' ESSID', 'BSSID', ' channel'])
#df.sort_values([" Power"], axis=0, ascending=[False], inplace=True)



restore_interf(MNG_INTERF)
"""
for index, row in df.iterrows():
    chan    = str(df[' channel'])
    bssid   = str(df['BSSID'])
    essid   = str(df[' ESSID'])

    start_mon(MNG_INTERF, chan)
    dump_specific_nw(MON_INTERF, bssid, chan, 10, 'tgt')
    restore_interf(MNG_INTERF, MON_INTERF)
"""
start_mon(MNG_INTERF, TARGET_CHAN)
dump_specific_nw(MON_INTERF, TARGET_CHAN, TARGET_BSSID, 10, 'dump_perso')
restore_interf(MNG_INTERF)

# etape 2 : scanner la liste

    # pour chaque wifi dans la liste
        # recuperer le channel
        # passer la carte en mode monitoring sur la frequence adequate
        # monitorer quelques secondes et lister les clients

# En entrée : une liste de réseaux

# En sortie : un fichier contenant toutes les cibles
