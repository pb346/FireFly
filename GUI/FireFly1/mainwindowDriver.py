
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

COMPORT = 'COM3'
choice = str(-1)
programList = []
brightness = 256
startupFile = 'startupFiles/startup.txt'
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        global arduino
        global choice
        global programList
        global file
        choice = str(-1)
        #self.timer = QTimer(self)
        #self.timer.interval(1000)            
#       mainwindow size restrictions      
        self.setMinimumSize(500, 380)
        self.setMaximumSize(500, 380)
        self.menuBar = QMenuBar(self)
        
#       create frame around for Preset Settings        
        self.frame = QScrollArea(self)
        self.frame.setGeometry(195,90,290,255)
        self.frame.setStyleSheet("background-color:transparent")

#       create frame and scrollArea for selecting presets 
        self.scroll = QScrollArea(self)
        self.scroll.setMinimumSize(150, 360)
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.inner = QFrame(self.scroll)
        self.scroll.move(5, 20)
        self.inner.setLayout(QVBoxLayout(self))                               
        self.inner.setMaximumSize(150, 1000)
        self.scroll.setWidget(self.inner)

#       create mainwindow widgets   
        self.menuBar.addMenu('Presets')
        self.menuBar.addMenu('Customizer')
        self.buttonStart = QPushButton('Start', self)
        self.buttonStop = QPushButton('Stop', self)
        self.buttonImport = QPushButton('Import', self)
        self.buttonExport = QPushButton('Export', self)
        self.labelPresetList = QLabel('Preset List File:', self)
        self.labelSettings = QLabel('Preset Settings', self)
        self.labelSelect = QLabel('Selection:', self)
        self.labelDuration = QLabel('Duration:', self)
        self.labelBrightness = QLabel('Brightness:', self)
        self.labelUser = QLabel('User Command:', self)
        self.lineImport = QLineEdit(self)
        self.lineExport = QLineEdit(self)
        self.userInput = QLineEdit(self)
        self.selection = QLineEdit(self)
        self.duration = QLineEdit(self)
        self.brightness = QSlider(1, self)
        self.debugBrowser = QTextBrowser(self)

#       set size of widgets/move them   
        self.lineImport.setGeometry(275, 30, 210, 20)
        self.lineExport.setGeometry(275, 60, 210, 20)
        self.buttonStart.setGeometry(400,110, 80, 40)
        self.buttonStop.setGeometry(400, 160, 80, 40)
        self.debugBrowser.setGeometry(200, 230, 280,110)
        self.brightness.setGeometry(200, 205, 190, 20)
        self.selection.setGeometry(200, 125, 190, 20)
        self.duration.setGeometry(200, 165, 190, 20)
        self.userInput.setGeometry(280, 350, 200, 20)
        self.buttonImport.move(195, 30)
        self.buttonExport.move(195, 60)
        self.labelSettings.move(300, 90)
        self.labelPresetList.move(200, 15)
        self.labelSelect.move(200, 105)
        self.labelDuration.move(200, 145)
        self.labelBrightness.move(200,185)
        self.labelUser.move(200,350)

        self.brightness.setRange(0, 256)
        self.brightness.setValue(256)
        self.selection.setReadOnly(True)
        self.lineImport.setText(startupFile)
        self.lineExport.setText("startupFiles/")
#       read preset list and connect
        self.userInput.returnPressed.connect(self.readInput)
        self.buttonExport.clicked.connect(self.exportFile)
        self.buttonImport.clicked.connect(self.processStartup)
        self.buttonStart.clicked.connect(self.handleButtonStart)
        self.buttonStop.clicked.connect(self.handleButtonStop)
        self.show()
        self.debugBrowser.append("Connected to " + COMPORT)
        arduino = serial.Serial(COMPORT, 9600)
        time.sleep(1)

    def readInput(self):
        global user
        user = self.userInput.text()
        self.debugBrowser.append("USER>> " + user)
        
    def processStartup(self):
        global programList
        self.buttonList = []
        startupFile = self.lineImport.text()
        try:
            file = open(startupFile, '+r')
        except:
            self.debugBrowser.append("ERROR: Could not open file " + startupFile)
            return
        self.debugBrowser.append("Imported presets from " + startupFile)
        programNum = int(file.readline())
        for i in range(programNum):
            entry = file.readline()
            programList.append(entry)
            self.buttonList.append(QPushButton(entry, self.inner))
            self.buttonList[i].setStyleSheet("Text-align:left")
            self.inner.layout().addWidget(self.buttonList[i])
            presetText = self.buttonList[i].text()
            self.buttonList[i].clicked.connect(lambda old, i=i: self.handleButton(i+1)) #index was overwritten before

    def exportFile(self):
        self.debugBrowser.append("Feature does not work")
    #    file = self.lineExport.text()
    #    global user
    #    try:
     #       open(file,'r+')
    #        self.debugBrowser.append("File already exists. Overwrite? (y/n)")
    #        while True:
     #           line = user

     #           if line == 'n':
     #               self.debugBrowser.append("Export Cancelled")
     #               return
     #           if line == 'y':
     #               self.debugBrowser.append("Exporting " + file)
      #              break
      #          else:
       #             self.debugBrowser.append("ERROR: Invalid option. Select 'y' or 'n'")          
      #  except:
      #      self.debugBrowser.append("Exporting " + file)
      #  open(file, 'w')
        
    def handleButtonStart(self):
        global choice
        global brightness
        if choice == '-1':
            self.debugBrowser.append("No program Selected")
        else:
            print(self.brightness.value()) 
            arduino.write(choice.encode())
            bright = str(brightness)
            #arduino.write(bright.encode())
            program = programList[int(choice)-1].rstrip()       
            self.debugBrowser.append("Starting Program " + program)
            if choice == '1':
                self.handleInteractive()
                
        
    def handleButtonStop(self):
        global choice
        choice = str(0)
        arduino.write(choice.encode())
        self.debugBrowser.append("Program Stopped")
        choice = str(-1)
        self.selection.setText('')

    def handleInteractive(self):
        global choice
        time.sleep(2);
        maxX = GetSystemMetrics(0)              #max X screen resolution
        maxY = GetSystemMetrics(1)              #max Y screen resolution
        red = 0
        blue = 0
        green = 0
        counter = 0
        exitFlag = 0
        while True:
            QCoreApplication.processEvents()
            if choice == '0':
                ledDisplayInfo = "0,0,0\n"
                arduino.write(ledDisplayInfo.encode())
                ledDisplayInfo = "-1,-1,-1\n"
                arduino.write(ledDisplayInfo.encode())
                break
            #start of interactive mode
            option = 0
            red = int(red*2.55)
            green = int(green*2.55)
            blue = int(blue*2.55)
            redStr = str(red)
            greenStr = str(green)
            blueStr = str(blue) 
            ledDisplayInfo = redStr+','+greenStr+','+blueStr+'\n'
            arduino.flush()
            arduino.write(ledDisplayInfo.encode())
            time.sleep(.015)#directly controls the amount of data sent to arduino

            red = 0
            blue = 0
            green = 0
            currentX,currentY = win32gui.GetCursorPos() #get X,Y coordinates of cursor
            x = currentX-maxX/2     #sets (0,0) to be the center of the screen
            y = (currentY-maxY/2) * -1 #changes it so that quadrants III and IV have negative y values    
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
                continue
            #if angle >= 0 and angle <= 90:              #QUAD I
            if QUAD == 1:
                if angle <= 60:
                    red = 100
                    blue = 100*(angle/ 60) #debug
                    continue
                else:
                    blue = 100 
                    red = 100*(45/angle) ##
                    continue    
            #if angle >= 90 and angle <= 180:
            if QUAD == 2:
                if angle <= 120:
                    red = 100 * (1-(angle/120))               
                    blue = 100
                    continue 
                else:
                    blue = 100
                    green = 100*((angle/180)-((180-angle)/90))
                    continue     
            #if angle >= 180 and angle <= 270:
            if QUAD == 3:
                if angle <= 240:
                    green = 100
                    blue = 100 *((180/angle)-((angle-180)/80))
                    continue 
                else:
                    green = 100
                    red = 100*((angle/60)-4)
                    continue 
            #if angle >= 270 and angle <= 360:
            if QUAD == 4:
                if angle < 300:
                    green = 100
                    red = 100*((angle/300) - ((300-angle)/75))
                    continue 
                else:
                    red = 100
                    green = 100*((angle/300)-((angle-300)/50))
                    continue

    def handleButton(self, string):
        global choice
        global programList
        choice = str(string)
        self.selection.setText(programList[string-1])
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
