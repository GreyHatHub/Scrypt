#!/bin/bash

echo 'Omegared.#' |sudo -S echo ''
sudo iptables-restore < './Default.v4'
