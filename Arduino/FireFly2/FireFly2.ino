#include <Adafruit_NeoPixel.h>

#define APIN 6
#define NUMLEDS1 131
#define ERROR   (-1)
Adafruit_NeoPixel stripA = Adafruit_NeoPixel(NUMLEDS1, APIN, NEO_GRB + NEO_KHZ800);
int choice = 0;
int brightness;
long duration;
uint32_t red = stripA.Color(255, 0, 0);
uint32_t white = stripA.Color(255, 255, 255);
uint32_t cyan = stripA.Color(0, 255, 255);
uint32_t blue = stripA.Color(0, 0, 255);

int poll()
{
  int status = 0;
  int readIn = -1;
  int garbage = 0;
  while (Serial.available() > 0)
  {
    readIn = Serial.parseInt();
  }
  if(readIn == -1)
  {
    Serial.flush();
    return 0;
  }
  else
  {
    choice = 0;
    delay(100);
    Serial.println(garbage);
    Serial.flush();
    return 1;
  }  
}

void input()
{
  int flag = 0;
  int counter = 0;
  int index;
  int dur;
  String strChoice;
  String strDuration;
  String strBrightness;
  String pythonInput;
  while (true) {
    while (Serial.available() > 0)
    {
      pythonInput = Serial.readString();
    }
    if (pythonInput[0] > 0)
      break;
  }
  for (int i = 0; i < pythonInput.length(); i++)
  {
    if (pythonInput[i] == ',' || pythonInput[i] == '\n')
    {
      if (flag == 0)
      {
        strChoice = pythonInput.substring(0, counter);
        flag = 1;
        counter++;
        index = counter;
        continue;
      }
      if (flag == 1)
      {
        strDuration = pythonInput.substring(index, counter);
        counter++;
        index = counter;
        flag = 2;
        continue;
      }
      if (flag == 2)
      {
        strBrightness = pythonInput.substring(index, counter);
        break;
      }
    }
    counter++;
  }
  choice = strChoice.toInt();
  dur = strDuration.toInt();
  duration = dur * 60000;
  brightness = strBrightness.toInt();
 // Serial.println(choice);
 // Serial.println(duration);
 // Serial.println(brightness);
}
void setup()
{
  Serial.begin(9600); //initialize serial COM
  stripA.begin();
  stripA.show();
}

int readFromSerial()
{
  int newChoice;
  while (Serial.available() > 0)
  {
    newChoice = Serial.parseInt();
    return newChoice;
  }
  return ERROR;
}

void loop() {
reset:
  int i;
  int j;
  float calcDelay;
  int castDelay;
  int adjustColor;
  int newchoice;
  long start = millis();
  if (duration - start <= 0)
    choice = 0;
  if (choice == 0)
  {
    for (j = 0; j < NUMLEDS1; j++)
    {
      stripA.setPixelColor(j, 0, 0, 0);
    }
    stripA.show();
    input();
  }

  if ( choice == 1) //Interactive Mode
  {
    while (Serial.available() > 0)
    {
      int red = Serial.parseInt();
      int green = Serial.parseInt();
      int blue = Serial.parseInt();
      if (red == -1 && green == -1 && blue == -1)
      {
        stripA.setPixelColor(25, 150, 150, 150);
        stripA.show();
        choice = 0;
        goto reset;
      }
      if (Serial.read() == '\n')
      {
        for (j = 0; j < NUMLEDS1; j++)//set all pixels, show when done
        {
          stripA.setPixelColor(j, red, green, blue);
        }
        stripA.show();
      }
    }
  }//end choice1
  
  if (choice == 2) //Ocean Waves Mode
  {
    for (i = 0; i < 256; i++) //brightness values
    {
      for (j = 0; j < NUMLEDS1; j++) //LED locations
      {
        adjustColor = i;
        stripA.setPixelColor(j, 0, i, 255);
        if(poll())
          return;
      }//end LEDS
      delay(117);
      stripA.show();
      //stripB.show();
    }//end Blue to Cyan
    for (i = 0; i < 256; i++) //Cyan to Blue
    {
      for (j = 0; j < NUMLEDS1; j++) //LED locations
      {
        stripA.setPixelColor(j, 0, 255 - i, 255);
        if(poll())
          return;
      }
      delay(117);
      stripA.show();
      //stripB.show();
    }// end Cyan to Blue
  }//end Choice2
  
  if (choice == 3) //Sunset Mode
  {
    while (true)
    {
      for (i = 0; i < 256; i++) //adjust hues from Yellow to Red
      {
        for (j = 0; j < NUMLEDS1; j++) //Adjust all LED's to same color
        {
          adjustColor = 255 - i; //Red is auto 255 so this starts as yellow and fades to Red
          stripA.setPixelColor(j, 255, adjustColor, 0);
          if(poll())
            return;
        }
        delay(117);
        stripA.show();         //show each time after a .117s delay and when all lights are set to the same color

      }//end of Yellow to Red
      for (i = 0; i < 256; i++) //Start Red to Yellow
      {
        for (j = 0; j < NUMLEDS1; j++) //Adjust all LED's to same color
        {
          stripA.setPixelColor(j, 255, i, 0);
          if(poll())
            return;
        }
        delay(117);
        stripA.show();

      }//end Red to Yellow
    }//end of While Loop
  } //end of choice 3

  if (choice == 4) //Rainbow Mode
  {
    for (i = 0; i < 256; i++)
    { //red to magenta
      for (j = 0; j < NUMLEDS1; j++) {
        stripA.setPixelColor(j, 255, 0, i);
        if(poll())
          return;
      }
      stripA.show();
      delay(19);
    }

    for (i = 0; i < 256; i++)
    { //magenta to blue
      for (j = 0; j < NUMLEDS1; j++) {
        stripA.setPixelColor(j, 255 - i, 0, 255);
        if(poll())
          return;
      }
      stripA.show();
      delay(19);
    }
    for (i = 0; i < 256; i++)
    { //blue to cyan
      for (j = 0; j < NUMLEDS1; j++) {
        stripA.setPixelColor(j, 0, i, 255);
        if(poll())
          return;
      }
      stripA.show();
      delay(19);
    }
    for (i = 0; i < 256; i++)
    { //cyan to green
      for (j = 0; j < NUMLEDS1; j++) {
        stripA.setPixelColor( j, 0, 255, 255 - i);
        if(poll())
          return;        
      }
      stripA.show();
      delay(19);
    }
    for (i = 0; i < 256; i++)
    { //green to yellow
      for (j = 0; j < NUMLEDS1; j++) {
        stripA.setPixelColor(j, i, 255, 0);
        if(poll())
          return;
      }
      stripA.show();
      delay(19);
    }
    for (i = 0; i < 256; i++)
    { //yellow to red
      for (j = 0; j < NUMLEDS1; j++) {
        if(poll() == 1)
        {
          return;
        }
        stripA.setPixelColor(j, 255, 255 - i, 0);
      }
      stripA.show();
      delay(19);
    }
  }

  if (choice == 5) //Toxicity Mode
  {
    for ( i = 0; i < brightness; i++)
    {
      for (j = 0; j < NUMLEDS1; j++)
      {
        stripA.setPixelColor(j, 0, i, 0);
        if(poll())
          return;
      }
      /*
      calcDelay = (1.0 -(brightness/256.0)) * 100.0;
      castDelay = static_cast<int>(calcDelay);
      delay(castDelay);
      */
      stripA.show();
    }
    for (i = 0; i < brightness; i++)
    {
      for (j = 0; j < NUMLEDS1; j++) {
        stripA.setPixelColor(j, 0,  brightness - 1 -i, 0);
        if(poll())
          return;
      }
      /*
      calcDelay = (1.0 -(brightness/256.0)) * 100.0;
      castDelay = static_cast<int>(calcDelay);
      delay(castDelay);
      */
      stripA.show();
    }
  }
  if (choice == 6) //comet
  {
    for (j = 1; j < 131; j++) {
      if(poll())
        return;
      if (j < 125) {
        stripA.setPixelColor(j - 1, 0, 0, 0);
        stripA.setPixelColor(j, blue);
        stripA.setPixelColor(j + 1, blue);
        stripA.setPixelColor(j + 2, blue);
        stripA.setPixelColor(j + 3, cyan);
        stripA.setPixelColor(j + 4, cyan);
        stripA.setPixelColor(j + 5, white);
        stripA.setPixelColor(j + 6, red);

        stripA.setPixelColor(j - 67 - 1, 0, 0, 0);
        stripA.setPixelColor(j - 67, blue);
        stripA.setPixelColor(j - 1 + 67, blue);
        stripA.setPixelColor(j - 2 + 67, blue);
        stripA.setPixelColor(j - 3 + 67, cyan);
        stripA.setPixelColor(j - 4 + 67, cyan);
        stripA.setPixelColor(j - 5 + 67, white);
        stripA.setPixelColor(j - 6 + 67, red);

      }
      stripA.show();
      delay(10);
      stripA.setPixelColor(130, 0, 0, 0);
      stripA.setPixelColor(129, 0, 0, 0);
      stripA.setPixelColor(128, 0, 0, 0);
      stripA.setPixelColor(127, 0, 0, 0);
      stripA.setPixelColor(126, 0, 0, 0);
      stripA.setPixelColor(125, 0, 0, 0);
      stripA.setPixelColor(124, 0, 0, 0);
      stripA.show();

    }
  }
  // put your main code here, to run repeatedly:


  if (choice == 7)
  {
    if (brightness == -1)
    {
      for (int i = 0; i < NUMLEDS1; i++)
      {
        stripA.setPixelColor(i, 0, 0, 150);
      }
      stripA.show();
      return;
    }
    float fl = NUMLEDS1 * brightness / 256.0;
    int val = NUMLEDS1 * brightness / 256.0;
    for (int i = 0; i < val; i++)
    {
      stripA.setPixelColor(i, 150, 150, 150);
    }
    stripA.show();
  }


}//end of program

