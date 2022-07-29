#!/usr/bin/env bash

# build the script name, check for extension
scriptName=$1

# kill all outputs on the pins
sudo pkill -f scriptName && python3 killRGB.py