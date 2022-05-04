#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Forensic
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################


import pandas
from drn_nw_utils import *
from pwn import *

# ouvrir le fichier en entree
# parcourir chaque ligne

df = pandas.read_csv('tst-01.csv', usecols=[' Power', ' ESSID', 'BSSID', ' channel'])
df.sort_values([" Power"], axis=0, ascending=[False], inplace=True)

# printing all columns of the dataframe
print(df)

mng_interf      = 'wlan0'
mon_interf      = 'wlan0mon'

try:
    prg = log.progress("test")
    restore_interf(mng_interf, mon_interf)
    prg.success("preparation complete")
    
    #for index, row in df.iterrows():
    start_mon(mng_interf, str(df[' channel']))
    print(df[' channel'], df['BSSID'], df[' ESSID'])
    dump_specific_nw(mon_interf, str(df['BSSID']), str(df[' channel']), 10, 'tgt')
    restore_interf(mng_interf, mon_interf)

except Exception as e:
    prg.failure(e.traceback.format_exc())
finally:
    restore_interf(mng_interf, mon_interf)



# etape 2 : scanner la liste

    # pour chaque wifi dans la liste
        # recuperer le channel
        # passer la carte en mode monitoring sur la frequence adequate
        # monitorer quelques secondes et lister les clients

# En entrée : une liste de réseaux

# En sortie : un fichier contenant toutes les cibles
