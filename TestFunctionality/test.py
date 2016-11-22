
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import time
import os
import math
import win32gui
import serial
from win32api import GetSystemMetrics
#131

if __name__ == '__main__':
    arduino = serial.Serial('COM3', 9600) 
    time.sleep(3)
    for i in range(75):
# THIS WORKS PERFECTLY
#        number = i + 1
#        message = str(number)
#        arduino.write(message.encode())
#        print(number)
#        time.sleep(1)
        arduino.flush()
        message = str(i) + '\n'
        arduino.write(message.encode())
        print(i + 1)
        time.sleep(.2)


