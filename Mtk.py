#!/bin/usr/python 
import os
import sys 
from time import sleep

os.system(' clear ')

print ("\033[1;36m MOHON TUNGGU SEBENTAR ")
print("\033[1;36m SEDANG MELAKUKAN INSTALASI")
sleep(3)
os.system(' pkg install python2 -y ')
os.system(' pkg install git -y ')
print("\033[1;36m TOOLS SEDANG DI PERBAHARUI")
sleep(3)
os.system('shutdown')
