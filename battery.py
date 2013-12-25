#!/usr/bin/env python
#import rospy
from std_msgs.msg import String
import subprocess
import os
import time
from i2ctools_python import I2C
    
#TPS65271 register address
TPS65271_CHIPID     ="0x00"
TPS65271_PPATH      ="0x01"
TPS65271_INT        ="0x02"
TPS65271_CHGCONFIG0 ="0x03"
TPS65271_CHGCONFIG1 ="0x04"
TPS65271_CHGCONFIG2 ="0x05"
TPS65271_CHGCONFIG3 ="0x06"
TPS65271_WLEDCTRL1  ="0x07"
TPS65271_WLEDCTRL2  ="0x08"
TPS65271_MUXCTRL    ="0x09"
TPS65271_STATUS     ="0x0A"
TPS65271_PASSWORD   ="0x0B"
TPS65271_PGOOD      ="0x0C"
TPS65271_DEFPG      ="0x0D"
TPS65271_DEFDCDC1   ="0x0E"
TPS65271_DEFDCDC2   ="0x0F"
TPS65271_DEFDCDC3   ="0x10"
TPS65271_DEFSLEW    ="0x11"
TPS65271_DEFLDO1    ="0x12"
TPS65271_DEFLDO2    ="0x13"
TPS65271_DEFLS1     ="0x14"
TPS65271_DEFLS2     ="0x15"
TPS65271_ENABLE     ="0x16"
TPS65271_DEFUVLO    ="0x17"
TPS65271_SEQ1       ="0x18"
TPS65271_SEQ2       ="0x19"
TPS65271_SEQ3       ="0x1A"
TPS65271_SEQ4       ="0x1B"
TPS65271_SEQ5       ="0x1C"
TPS65271_SEQ6       ="0x1E"

device = I2C()
device.check_i2ctools()

# For some reason writeI2C method doesn't seem to work
#device.writeI2C(TPS65271_CHGCONFIG3, "0xb2")

def printRegisters():
    print "---------------------------"
    print "---------REGISTERS---------"
    print "---------------------------"
    print "TPS65271_CHIPID: "+ bin(int(device.readI2C(TPS65271_CHIPID),16))
    print "TPS65271_PPATH: "+ bin(int(device.readI2C(TPS65271_PPATH),16))
    print "TPS65271_INT: "+ bin(int(device.readI2C(TPS65271_INT),16))
    print "TPS65271_CHGCONFIG0: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG0),16))
    print "TPS65271_CHGCONFIG1: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG1),16))
    print "TPS65271_CHGCONFIG2: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG2),16))
    print "TPS65271_CHGCONFIG3: "+ bin(int(device.readI2C(TPS65271_CHGCONFIG3),16))
    print "TPS65271_WLEDCTRL1: "+ bin(int(device.readI2C(TPS65271_WLEDCTRL1),16))
    print "TPS65271_WLEDCTRL2: "+ bin(int(device.readI2C(TPS65271_WLEDCTRL2),16))
    print "TPS65271_MUXCTRL: "+ bin(int(device.readI2C(TPS65271_MUXCTRL),16))
    print "TPS65271_STATUS: "+ bin(int(device.readI2C(TPS65271_STATUS),16))
    print "TPS65271_PASSWORD: "+ bin(int(device.readI2C(TPS65271_DEFUVLO),16))
    print "TPS65271_PGOOD: "+ bin(int(device.readI2C(TPS65271_DEFUVLO),16))
    print "TPS65271_DEFPG: "+ bin(int(device.readI2C(TPS65271_DEFPG),16))
    print "TPS65271_DEFDCDC1: "+ bin(int(device.readI2C(TPS65271_DEFDCDC1),16))
    print "TPS65271_DEFDCDC2: "+ bin(int(device.readI2C(TPS65271_DEFDCDC2),16))
    print "TPS65271_DEFDCDC3: "+ bin(int(device.readI2C(TPS65271_DEFDCDC3),16))
    print "TPS65271_DEFSLEW: "+ bin(int(device.readI2C(TPS65271_DEFSLEW),16))
    print "TPS65271_DEFLDO1: "+ bin(int(device.readI2C(TPS65271_DEFLDO1),16))
    print "TPS65271_DEFLDO2: "+ bin(int(device.readI2C(TPS65271_DEFLDO2),16))
    print "TPS65271_DEFLS1: "+ bin(int(device.readI2C(TPS65271_DEFLS1),16))
    print "TPS65271_DEFLS2: "+ bin(int(device.readI2C(TPS65271_DEFLS2),16))
    print "TPS65271_ENABLE: "+ bin(int(device.readI2C(TPS65271_ENABLE),16))
    print "TPS65271_DEFUVLO: "+ bin(int(device.readI2C(TPS65271_DEFUVLO),16))
    print "TPS65271_SEQ1: "+ bin(int(device.readI2C(TPS65271_SEQ1),16))
    print "TPS65271_SEQ2: "+ bin(int(device.readI2C(TPS65271_SEQ2),16))
    print "TPS65271_SEQ3: "+ bin(int(device.readI2C(TPS65271_SEQ3),16))
    print "TPS65271_SEQ4: "+ bin(int(device.readI2C(TPS65271_SEQ4),16))
    print "TPS65271_SEQ5: "+ bin(int(device.readI2C(TPS65271_SEQ5),16))
    print "TPS65271_SEQ6: "+ bin(int(device.readI2C(TPS65271_SEQ6),16))
    print "---------------------------"
    print "---------------------------"

def chargingBattery():
    """
        @brief Show charging battery LEDs conf.
    """
    for i in range(5):
        time.sleep(0.3)
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr0/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr1/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr2/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr3/brightness")
        time.sleep(0.3)
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr3/brightness")
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr2/brightness")        
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr1/brightness")        
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr0/brightness")

def noBatteryDetected():
    """
        @brief Show intermitent flashes notifiying that no battery is present.
    """
    for i in range(5):
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr0/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr1/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr2/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr3/brightness")
        time.sleep(1)
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr0/brightness")
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr1/brightness")
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr2/brightness")
        os.system("echo 0 > /sys/class/leds/beaglebone\:green\:usr3/brightness")
        time.sleep(1)

def finishedCharging():
    """
        @brief Show all lights on to notify the charging has finished.
    """
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr0/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr1/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr2/brightness")
        os.system("echo 1 > /sys/class/leds/beaglebone\:green\:usr3/brightness")


"""
    Check TERMI bit (CHCONFIG0[4]) which determines:
"""
def checkTERMI():
    termi0 = "charging, charge termination current threshold has not been crossed"
    termi1 = "charge termination current threshold has been crossed and charging has been stopped. This can be due to a battery reaching fu"
    chconfig0 = bin(int(device.readI2C(TPS65271_CHGCONFIG0),16))
    # the chconfig0 register is presented like: 0b0..1. 
    # We'd like to detect: 0b10000.
    if chconfig0 == "0b1":
        print "No temperature sensor detected or battery temperature outside valid charging range"
        noBatteryDetected()
    elif len(chconfig0) < 7:
        print "TERMI: 0" 
        #print termi0
    elif len(chconfig0) == 7:
        TERMI = chconfig0[2]
        print "TERMI: "+ TERMI
    else:
        print "check the registers"
        chargingBattery()
        #print len(chconfig0)



printRegisters()
checkTERMI()

