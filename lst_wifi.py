#!/usr/bin/env python3

# devices
import subprocess
from subprocess import PIPE


mng_device      = 'wlan0'
mon_device      = 'wlan0mon'

# commands
cmd_check_kill  = ['sudo', 'airmon-ng', 'check', 'kill']
cmd_start_mon   = ['sudo', 'airmon-ng', 'start', mng_device]
cmd_dump        = ['sudo', 'airodump-ng', mon_device]
cmd_stop_mon    = ['sudo', 'airmon-ng', 'stop', mon_device]
cmd_restart_nw  = ['sudo', 'systemctl', 'restart', 'NetworkManager']
cmd_set_dev_up  = ['sudo', 'ip', 'link', 'set', mng_device, 'up']

networks = ""

# check and kill processes that could cause troubles
subprocess.run(cmd_check_kill, capture_output=True)

# set device to monitoring mode
subprocess.run(cmd_start_mon, capture_output=True)

# dump the available networks
try:
    networks = subprocess.run(cmd_dump, stdout=PIPE, timeout=3).stdout
except subprocess.TimeoutExpired:
    print("")

print (networks)

# set back device to managed mode
subprocess.run(cmd_stop_mon, capture_output=True)

# restart NetworkManager
subprocess.run(cmd_restart_nw, capture_output=True)

# reactivate the device
subprocess.run(cmd_set_dev_up, capture_output=True)
