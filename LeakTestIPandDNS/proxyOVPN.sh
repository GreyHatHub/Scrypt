#!/bin/bash

echo ############# |sudo -S echo ''
sudo iptables-restore < './iptables-OVpn.ip4'
