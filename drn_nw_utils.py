#!/usr/bin/env python3

###############################################################################
# Author    : Tarek AZAIZ
# Project   : Drones Attack Demonstrator
# Subject   : Useful tools for monitoring and dumping WiFi networks
# Version   : 0.1
# Created   : 2022/03/31
# Modified  : 2022/05/04
###############################################################################


import subprocess
from pwn import *


def check_kill():
    """
    perform a preventive kill of processes that could cause troubles
    during the monitoring
    """
    subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'], capture_output=True)


def start_mon(interface, channel=''):
    """
    enable monitor mode on <interface> and <channel>
    """
    check_kill()
    subprocess.run(['sudo', 'airmon-ng', 'start', interface, channel], capture_output=True)


def stop_mon(interface):
    """
    disable monitor mode on <interface> and <channel>
    """
    subprocess.run(['sudo', 'airmon-ng', 'stop', interface], capture_output=True)


def dump_all_nw(interface, duration, prefix):
    """
    capture packets using airodump-ng with <interface>
    during <duration> seconds and write the result to a prefixed csv file
    """
    progress_state = log.progress("Dumping all wifi networks with interface '"
        +interface+ "' during "+str(duration)+" seconds...")
    try:
        sp_output = subprocess.run(['sudo', 'airodump-ng', interface, '-w', prefix
            , '--output-format', 'csv', '-M', '-t', 'WEP', '-t', 'WPA',]
            , timeout=duration) #, capture_output=True)
    except subprocess.TimeoutExpired:
        progress_state.success()
    except Exception as e:
        progress_state.failure(e.traceback.format_exc())
        

def dump_specific_nw(interface, channel, bssid, duration, prefix):
    """
    capture packets using airodump-ng with <interface>
    during <duration> seconds and write the result to a prefixed csv file
    """
    progress_state = log.progress("Dumping access point with BSSID = "+str(bssid)
        +" on channel "+str(channel)+ " with interface '" +interface+ "' during "+str(duration)+" seconds...")
    try:
        subprocess.run(['sudo', 'airodump-ng', interface, '-w', prefix
            , '--output-format', 'csv', '-M', '-t', 'WEP', '-t', 'WPA'
            , '-c', channel, '-d', bssid]
            , timeout=duration, capture_output=True)
    except subprocess.TimeoutExpired:
        progress_state.success()
    except Exception as e:
        progress_state.failure(e.traceback.format_exc())


def restart_nw():
    """
    restart the network manager
    """
    progress_state = log.progress("Restarting network...")
    subprocess.run(['sudo', 'systemctl', 'restart', 'NetworkManager'], capture_output=True)
    progress_state.success()


def enable_interf(interface):
    """
    start interface
    """
    progress_state = log.progress("Enabling interface '" + str(interface) + "'...")
    subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], capture_output=True)
    progress_state.success()


def disable_interf(interface):
    """
    stop interface
    """
    progress_state = log.progress("Disabling interface '" + str(interface) + "'...")
    subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'], capture_output=True)
    progress_state.success()


def restore_interf(interf):
    """
    restore interf initial state (set it back to managed mode)
    """
    progress_state = log.progress("Restoring '"+interf+"' initial state...")
    stop_mon(interf+'mon')
    restart_nw()
    enable_interf(interf)
    progress_state.success()



"""
restore_interf('wlan0')
start_mon('wlan0')
dump_all_nw('wlan0mon', 10, 'tst2')
restore_interf('wlan0')
"""
#prepare_dump('wlan0', 'wlan0mon')
