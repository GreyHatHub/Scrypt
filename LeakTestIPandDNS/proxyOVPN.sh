#!/bin/bash

echo 'Omegared.#' |sudo -S echo ''
sudo iptables-restore < './iptables-OVpn.ip4'
