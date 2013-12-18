#!/bin/bash
echo "******************************************"
echo "Configuring the PMIC to work with a battery"
echo "******************************************"

echo "charge current to 400 mAh"
yes | i2cset -f 0 0x24 0x06 0x72 # change ICHRG[1:0] to 400 mAh 

