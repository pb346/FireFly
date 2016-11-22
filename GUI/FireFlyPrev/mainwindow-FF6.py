# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import time
import os
import math
import win32gui
import serial
from win32api import GetSystemMetrics

qtCreatorFile = "mainwindow.ui"

class window(QDialog):
    def __intit__(self, *args):
        super(window, self).__init__(*args)

        loadUi(qtCreatorFile, self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
  #  widget = window()
  #  widget.show()
    ready = 0
PPM = 0
#arduino = serial.Serial('COM3',9600)            #open selected COM, Arduino Uno is connected
time.sleep(2)
os.system('cls')
print("Connection to COM3 established\n")
print("0) Reset\n"
      "1) Interactive\n"
      "2) Ocean Waves\n"
      "3) Sunset\n"
      "4) Rainbow\n"
      "5) Toxicity\n"
      "6) 'Murica\n")
choice=input("Please make a selection: ")
choice=int(choice)
os.system('cls')
strChoice=str(choice)
arduino.write(strChoice.encode())
print("Program running...")        
maxX = GetSystemMetrics(0)              #max X screen resolution
maxY = GetSystemMetrics(1)              #max Y screen resolution
exitFlag = 0
counter = 0
if choice == 0:
    print("Resetting and Exiting")
    arduino.close()
if choice == 1:
    time.sleep(2);
    while True:
        while True:
            counter = 0
            exitFlag = 0
            red = 0
            blue = 0
            green = 0
            option = 0
            currentX,currentY = win32gui.GetCursorPos() #get X,Y coordinates of cursor
            x = currentX-maxX/2     #sets (0,0) to be the center of the screen
            y = (currentY-maxY/2) * -1 #changes it so that quadrants III and IV have negative y values
           #                                    int(y)
            if currentX <= 10 and currentY <=10: #exit sequence, if cursor is in the top left corner
                newX,newY = win32gui.GetCursorPos()
                while newX == currentX and newY == currentY: #while the cursor doesn't move in the corner
                    counter += 1;
                    time.sleep(1);
                    newX,newY = win32gui.GetCursorPos()
                    if counter == 5:    #if the cursor has been "exiting" for 5 seconds
                        exitFlag = 1
                        break
            if exitFlag == 1:
                exitResponse = raw_input("Would you like to exit? [y/n]\n") #prompt them incase it was a mistake
                if exitResponse == 'y':
                    print("Exiting\n")
                    break
                if exitResponse == 'n':
                    exitFlag = 0
            #start of interactive mode
            option=0    
            if option == 0 and x > 0 and y > 0:         #cursor in QUAD I
                radAngle = math.asin(y/math.sqrt(math.pow(x,2)+math.pow(y,2)))
                angle = math.degrees(radAngle)
                #print(angle)
                option = 1 
                QUAD = 1
            if option == 0 and x <= 0 and y > 0:         #cursor in QUAD II
                radAngle = math.asin(y/(math.sqrt(math.pow(x,2)+math.pow(y,2))))
                angle = 180 - math.degrees(radAngle)
               # print(angle)
                option = 1
                QUAD = 2   
            if option == 0 and x <= 0 and y <= 0: #cursor in QUAD III***********************
                if(x==0):
                    x=.001
                radAngle = math.asin((abs(y)/math.sqrt(math.pow(x,2)+math.pow(y,2))))
                #radAngle=math.asin((y)/(math.sqrt(math.pow(x,2)+math.pow(y,2))))
                angle = math.degrees(radAngle) + 180
               # print(angle)
                option =1
                QUAD = 3
            if option == 0 and x > 0 and y <= 0:         #cursor in QUAD IV
                radAngle = math.acos(x/(math.sqrt(math.pow(x,2) + math.pow(y,2))))
                angle = 360 - math.degrees(radAngle)
               # print(angle)
                option = 1
                QUAD = 4
            if option == 0 and (x == 0 or y == 0):   #at this point, if either x or y are 0, then angle is undefined so restart evaluation
                break
            #if angle >= 0 and angle <= 90:              #QUAD I
            if QUAD == 1:
                if angle <= 60:
                    red = 100
                    blue = 100*(angle/ 60) #debug
                    break
                else:
                    blue = 100 
                    red = 100*(45/angle) ##
                    break     
            #if angle >= 90 and angle <= 180:
            if QUAD == 2:
                if angle <= 120:
                    red = 100 * (1-(angle/120))               
                    blue = 100
                    break
                else:
                    blue = 100
                    green = 100*((angle/180)-((180-angle)/90))
                    break    
            #if angle >= 180 and angle <= 270:
            if QUAD == 3:
                if angle <= 240:
                    green = 100
                    blue = 100 *((180/angle)-((angle-180)/80))
                    break
                else:
                    green = 100
                    red = 100*((angle/60)-4)
                    break
            #if angle >= 270 and angle <= 360:
            if QUAD == 4:
                if angle < 300:
                    green = 100
                    red = 100*((angle/300) - ((300-angle)/75))
                    break
                else:
                    red = 100
                    green = 100*((angle/300)-((angle-300)/50))
                    break
            break
        if exitFlag == 1:
            red = int(0)
            green = int(0)
            blue = int(0)

            redStr = str(red)
            greenStr = str(green)
            blueStr = str(blue)

            ledDisplayInfo = redStr+','+greenStr+','+blueStr+'\n'
            arduino.flush()
            arduino.write(ledDisplayInfo.encode())
            print("Closing connection with COM4\n")
            arduino.close()
            print("Firefly is closing...\n")
            break
        print("Red",red)
        print("Blue",blue)
        print("Green",green)
        red = int(red*2.55)
        green = int(green*2.55)
        blue = int(blue*2.55)

        redStr = str(red)
        greenStr = str(green)
        blueStr = str(blue)

        ledDisplayInfo = redStr+','+greenStr+','+blueStr+'\n'
        arduino.flush()
        arduino.write(ledDisplayInfo.encode())
       # print(ledDisplayInfo);
        #time.sleep(.5)
        time.sleep(.01)#directly controls the amount of data sent to arduino
  


    sys.exit(app.exec_())


