#!/usr/bin/env python3

import subprocess
import time
#import pyrcrack

from subprocess import PIPE, check_output
#from pwn import log # https://docs.pwntools.com/en/stable/install.html
from threading import Timer
import uu 

# adresses mac des drones Parrot, conformement au lien suivant :
# http://standards.ieee.org/develop/regauth/oui/oui.txt
parrot_macs_prefixes = [
    "90:03:B7", "00:12:1C", "90:3A:E6",
    "A0:14:3D", "00:12:1C", "00:26:7E"]

# variables globales
mng_device = ""


def getDeviceName():
    return syscmd("iwconfig").split(" ")[0]



# fonction qui liste les reseaux Wifi disponibles
# passe la carte en mode monitoring puis la repasse en mode managed
# renvoie la liste des reseaux
def getWifiNetworksList():

    # determine the wifi device to use
    print("Using device ", mng_device, ".\n")

    # scan the wifi networks list
    print("Scanning the wifi network list....")
    networks_list = []


    #cmd = "sudo airodump-ng "+mon_device+" > res.txt"
    cmd = ['sudo', 'iwlist', mng_device, 'scanning']

    # ouput capturing
    res_output = subprocess.check_output(cmd, universal_newlines= True).split("\n")
    
    # output processing
    for line in res_output:
        networks_list.append(line)
        print(line)

    #print("Network list : \n", networks_list)



# fonction qui liste les reseaux Wifi disponibles
# passe la carte en mode monitoring puis la repasse en mode managed
# renvoie la liste des reseaux
def wifiList():

    # determine the wifi device to use
    print("Using device ", mng_device, ".\n")

    # set the device in monitoring mode
    print("Setting the device in monitoring mode....")
    syscmd("sudo airmon-ng start "+mng_device)

    time.sleep(2)

    # scan the wifi networks list
    print("Scanning the wifi network list....")
    networks_list = []

    mon_device = getDeviceName()


    cmd = ['sudo', 'airodump-ng', mon_device]
    #cmd = ['sudo', 'iwlist', mng_device, 'scanning']

    # ouput capturing
    res_output = ""
    o_airodump = ""
    unused_stderr = ""
    airodump = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    airodump.wait()

    try:
        o_airodump, unused_stderr = airodump.communicate(timeout=3)
        airodump.kill()

    except subprocess.TimeoutExpired:
        print("capture finished, list = ", networks_list, o_airodump)

    print( airodump, o_airodump, res_output)

    #print("Network list : \n", networks_list)
    # repasser la carte en mode managed
    print("setting back the device to managed mode")
    syscmd("sudo airmon-ng stop "+mon_device)

    # redemarrer le networkmanager
    syscmd("sudo systemctl restart NetworkManager")

    # restart the device
    syscmd("sudo ip link set "+mng_device+" up")




# deconnect target from their drone's access point
def deauth_targets():

    # set the device in monitoring mode
    print("Setting the device in monitoring mode....")
    syscmd("sudo airmon-ng start "+mng_device)
    
    mon_device = getDeviceName()
    
    print(mng_device+" set to monitoring mode. New name : ", mon_device)

    time.sleep(2)

    # repasser la carte en mode managed
    print("setting back the device to managed mode")
    syscmd("sudo airmon-ng stop "+mon_device)

    # redemarrer le networkmanager
    syscmd("sudo systemctl restart NetworkManager")

    # restart the device
    syscmd("sudo ip link set "+mng_device+" up")



# etape 1 : scanner le reseau et lister tous les wifis
    # passer la carte en mode monitoring


    # repasser la carte en statut up (au cas ou)

# etape 2 : pour chacun des wifis, vérifier s'il contient un client de type 
# drone grâce à l'adresse mac

# etape 3 : si le réseau possède un client de type drone, récupérer le nom 
# du réseau, l'essid et le bssid de l'access point (adresse ip possible ou pas)




# Controler le drone
    # faire décoller le drone
    # faire atterrir le drone

def jam_target():
    return 0

def take_off():
    return 0

def land():
    return 0

# execute a system command
def syscmd(cmd):
    return subprocess.run(cmd,shell=True, universal_newlines = True
        , capture_output=True).stdout


# main function
def main():

    # TODO : check prerequites    

    global mng_device
    mng_device = getDeviceName()

    #getWifiNetworksList()
    wifiList()
    return 0


if __name__ == "__main__":
    main()
