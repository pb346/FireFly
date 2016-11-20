FireFly Version 0.1
Included:
	MainWindowDriver.py
	FireFly1.ino
	README.txt
	LEDSchematic.png

Brief: 
	This program is designed to control LED's that are connected from a PC
	to an arduino which controls strings of LED's. A pivotal feature of the 
	program is one of the included light sequences will take mouse position 
	and superimpose it onto a color gradient wheel which will display on the 
	LED's in realtime. The program also has the capability to load predefined
	light sequences without the need to alter the code within the program.  

History: 
	This program is a further development of a program written for CSE321. Issues 
	with the previous version included being commandline driven, there was no way to 
	stop a sequence once it started, there was no timeout, the brightness could not 
	be changed, and any newly downloaded light sequences would have to be manually 
	coded into the GUI.

Minimum Requirements PC:
	AMD A4 (or greater)
	2 GB RAM (or greater)
	Windows 7 Service Pack 1, 2, or 3
	
Hardware:
	Adafruit NeoPixels (any length)
	Generic 50 Watt (5V/10A) AC to DC Power Supply 
	1000uF Capacitor
	Female DC Power Jack Connector
	Arduino Mega
	4 Jumper Wires
	2-pin JST SM In-line power wire connectors
	USB Cable type A to B
	RTV Silicon (Recommended for mounting)

Software:
	Python 3.4
	Pyserial 3.1
	QtCreator 5.4
	Arduino IDE 1.6
	PyQt5
	sip4.18.1
	win32gui
	Adafuit_Neopixel

Installation:
(Hardware)
	It is recommended to connect the hardware before mounting, but be sure to verify
	the length of jumper wires will reach. Multiple LED strips can be used but they 
	must be connected to each other using 2-pin JST SM In-line power wire connectors.
	Each connector must be soldered onto each of the Neopixel strips. Refer to 
	Adafruit's documentation material on the Neopixels.
	
	Use the LEDSchematic for reference for the next part. Place a jumper to a ground
	pin on the Arduino Mega. The other end will be soldered to the negative terminal 
	of the Neopixels. Connect a jumper to the Pulse Width Modulated(PWM) pin 6. This 
	pin will be denoted as '~6'. Solder this jumper to the 'data' terminal of the first 
	strand. Connect the USB cable to the Arduino and a USB port on the computer. 

	Connect the Female DC power connector the the end of the power supply. Place the
	1000uF into the corresponding positive and negative terminals of the connector. 
	Connect a jumper from the positive terminal of the connector and solder it the
	corresponding terminal of the first Neopixel strand. Connect another jumper to 
	the negative terminals of the connector and strand. 

(Software)
	Note: all downloads can be found by searching for the software names.

	Download and install python3.4. Add python3.4 to Windows PATH Enviroment Variable.
	Download and install pyserial3.1. Using Window's cmd, in the pyserial3.1 directory, 
		issue 'python setup -install'.
	Download and install QTCreator5.4.
	Download and install sip4.18.1. Using Window's cmd, in the sip4.18.1 directory,
		issue 'python configure.py'
	Download and install PyQt5.
	Download and install win32gui library
	Download and install Arduino IDE 1.6.
	Download Adafruit_Neopixel library. Place the library in 
		C:\Users\<User>\Documents\Arduino\libraries
	
	Open Arduino IDE 1.6 and select Tools from the menu. Change the 'Board' setting to
	Arduino/Genuino Mega or Mega 2560. Change the port to the 'COM' that the arduino
	is plugged into. Change the 'Programmer' setting to ArduinoISP. Open FireFlyX.ino and change 
	line 3 '#define NUMLEDS1 <value>' to denote the number of LED's to be used. The code can 
	then be compiled and flashed/uploaded to the Arduino Mega.

	Open MainWindowDriver and change the COM number on line 24, 
	'arduino = serial.Serial('COM3', 9600)', to the Arduino Mega COM port and save.

Usage:
	The program can be run by double clicking the MainWindowDriver.pyw script.
	To display the available presets, either click import to load the default
	configuration file or chose to a load a different configuration file.

	After loading, select the desired preset. The duration is inputted as
	minutes. If no input for duration is detected, the system will default to 
	10 minutes. The brightness slider takes an input from 0 to 100. The 
	default is 100%. The program will being after clicking 'start'. Click 'stop' 
	to end the current light sequence. It is possible to select a new preset 
	while any light sequence is currently running. The previous sequence will 
	stop and the desired selection will start shortly after. 

TroubleShooting:
(LEDS)
	Refer to LEDSchematic.png to verify correct installation.
(Arduino)
	Refer to LEDSchematic.png to verify correct installation.
(Python)
	Interactive mode doesn't light or freezes after a few seconds:
		
		This is an issue with the computer passing data too
		quickly	to the Arduino and it is inaccurately parsing 
		the data. On line 82 of MainWindowDriver change the time 
		delay. Note that increasing the delay too much will result 
		in the LED color changes to be 'choppy' during Interactive mode.

	 
	
	
	 
