#!/bin/bash

echo ############## |sudo -S echo ''
sudo iptables-restore < './Default.v4'
