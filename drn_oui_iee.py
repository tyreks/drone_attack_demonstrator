#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Get correspondance between mac adress and constructor
#             according to the IEE's Organizationally Unique Identifiers list
#             https://standards-oui.ieee.org/
#
#             Not found Vendors : Abot, Autel Robotics, Chasing innovation,
#             Eachine, Hobbico, Hubsan, iBubble, JJRC,PJN /AEE, Powervision,
#             Star Wars Drones, SwellPro, Yuneec
#
#             O.U.I to confirm, because their vendor contains the "drone" word
#             in their name : 
#             Vimodrone (000ECE), Teal Drones(B030C8)
#
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################


# Dictionnary containing the list of the OUI MAC prefixes for each know vendor
VENDOR_MAC_OUI = {}
VENDOR_MAC_OUI["PARROT"]    = {"90:3A:E6", "00:12:1C", "90:03:B7", "A0:14:3D", "00:26:7E"}
VENDOR_MAC_OUI["DJI"]       = {"60601F","34D262"}
VENDOR_MAC_OUI["GOPRO"]     = {"2474F7", "D89685", "044169"}
VENDOR_MAC_OUI["XIAOMI"]    = {"488759", "AC1E9E", "64DDE9"}


def get_vendor(mac_oui:str) -> str:
    """
    returns the vendor's name matching the OUI MAC prefix 
    or an empty string if no match
    """
    for vendor in VENDOR_MAC_OUI:
        if mac_oui in VENDOR_MAC_OUI[vendor]:
            return vendor
    return ""


def get_mac_oui_list(vendor:str) -> list[str]:
    """
    returns the list of OUI MAC prefixes corresponding to the vendor name
    or an empty list in case of unknown vendor
    """
    try:
        return VENDOR_MAC_OUI[vendor]
    except KeyError:
        return []