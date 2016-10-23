#include <Adafruit_NeoPixel.h>
#define APIN 6
#define NUMLEDS1 131
Adafruit_NeoPixel stripA = Adafruit_NeoPixel(NUMLEDS1, APIN, NEO_GRB + NEO_KHZ800);
int choice = -1;
uint32_t red = stripA.Color(255, 0, 0);
uint32_t white = stripA.Color(255, 255, 255);
uint32_t cyan = stripA.Color(0, 255, 255);
uint32_t blue = stripA.Color(0, 0, 255);
void setup()
{
 Serial.begin(9600); //initialize serial COM
 while (choice == -1)
  {
    while (Serial.available() > 0)
    {
      choice = Serial.parseInt();
    }
  }
  stripA.begin();
  stripA.show();

}

void loop()
{
  int i;
  int j;
  int adjustColor;
  if ( choice > 9) //Invalid Mode
  {
    //choice is not valid
  }//end of Invalid
 /* if(choice == 5){
        for(i=0; i<256; i++){
      for(j=0; j<NUMLEDS1; j++){
        stripA.setPixelColor(j,0,i,0);
      }
      stripA.show();
    }
  }*/
  if(choice == 0)
  {
    for(j=0; j<NUMLEDS1; j++)
    {
      stripA.setPixelColor(j,0,0,0);
    }
  }
  if ( choice == 1) //Interactive Mode
  {
    while (Serial.available() > 0)
    {
      int red = Serial.parseInt();
      int green = Serial.parseInt();
      int blue = Serial.parseInt();
      if (Serial.read() == '\n')
      {
        for (j = 0; j < NUMLEDS1; j++)//set all pixels, show when done 
        {
          stripA.setPixelColor(j, red, green, blue);

        }
        stripA.show(); 
      }
    }
  }

  if (choice == 2) //Ocean Waves Mode
  {
    for (i = 0; i < 256; i++) //brightness values
    {
      for (j = 0; j < NUMLEDS1; j++) //LED locations
      {
        adjustColor = i;
        stripA.setPixelColor(j, 0, i, 255);
        //stripB.setPixelColor(j,0,i,255);
      }//end LEDS
      delay(117);
      stripA.show();
      //stripB.show();
    }//end Blue to Cyan
    for (i = 0; i < 256; i++) //Cyan to Blue
    {
      for (j = 0; j < NUMLEDS1; j++) //LED locations
      {
        stripA.setPixelColor(j,0, 255-i, 255);
      }
      delay(117);
      stripA.show();
      //stripB.show();
    }// end Cyan to Blue
  }
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
          //stripB.setPixelColor(j,255,adjustColor,0);
        }
        delay(117);
        stripA.show();         //show each time after a .117s delay and when all lights are set to the same color

      }//end of Yellow to Red
      for (i = 0; i < 256; i++) //Start Red to Yellow
      {
        for (j = 0; j < NUMLEDS1; j++) //Adjust all LED's to same color
        {
          stripA.setPixelColor(j, 255,i, 0);
          //stripB.setPixelColor(j,255,i,0);
        }
        delay(117);
        stripA.show();

      }//end Red to Yellow
    }//end of While Loop
  } //end of Sunset

  if (choice == 4) //Rainbow Mode
  {
    for(i=0; i<256; i++)
    {//red to magenta
      for(j=0; j<NUMLEDS1; j++){
        stripA.setPixelColor(j,255,0,i);
      }
        stripA.show();
        delay(19);
      }
    
    for(i=0; i<256; i++)
    {//magenta to blue
      for(j=0; j<NUMLEDS1; j++){
        stripA.setPixelColor(j,255-i,0,255);  
      }
      stripA.show();
      delay(19);
    }
      for(i=0; i<256; i++)
    {//blue to cyan
      for(j=0; j<NUMLEDS1; j++){
        stripA.setPixelColor(j,0,i,255);   
      }
      stripA.show();
      delay(19);
    }
    for(i=0; i<256; i++)
    {//cyan to green
      for(j=0; j<NUMLEDS1; j++){
       stripA.setPixelColor( j,0,255,255-i);
      }
      stripA.show();
      delay(19);
    }
      for(i=0; i<256; i++)
    {//green to yellow
      for(j=0; j<NUMLEDS1; j++){
      stripA.setPixelColor(j,i,255,0);  
      }
      stripA.show();
      delay(19);
    }
    for(i=0; i<256; i++)
    {//yellow to red
      for(j=0; j<NUMLEDS1; j++){
        stripA.setPixelColor(j,255,255-i,0);
      }
      stripA.show();
      delay(19);
    }
    }
  

  if (choice == 5) //Toxicity Mode
  {
    for(i=0; i<256; i++){
      for(j=0; j<NUMLEDS1; j++){
        stripA.setPixelColor(j,0,i,0);
      }
      stripA.show();
    }
      for(i=0; i<256; i++){
      for(j=0; j<NUMLEDS1; j++){
        stripA.setPixelColor(j,0,255-i,0);
      }
      stripA.show();
    }
  }
  if(choice == 6)//comet
  {
    for(j=1; j<131; j++){
      if(j<125){
        stripA.setPixelColor(j-1,0,0,0);
        stripA.setPixelColor(j, blue);
        stripA.setPixelColor(j+1, blue);
        stripA.setPixelColor(j+2,blue);
        stripA.setPixelColor(j+3,cyan);
        stripA.setPixelColor(j+4,cyan);
        stripA.setPixelColor(j+5, white);
        stripA.setPixelColor(j+6,red);

        stripA.setPixelColor(j-67-1,0,0,0);
        stripA.setPixelColor(j-67, blue);
        stripA.setPixelColor(j-1+67, blue);
        stripA.setPixelColor(j-2+67,blue);
        stripA.setPixelColor(j-3+67,cyan);
        stripA.setPixelColor(j-4+67,cyan);
        stripA.setPixelColor(j-5+67, white);
        stripA.setPixelColor(j-6+67,red);
        
      }
      stripA.show();
      delay(10);
      stripA.setPixelColor(130,0,0,0);
      stripA.setPixelColor(129,0,0,0);
      stripA.setPixelColor(128,0,0,0);
      stripA.setPixelColor(127,0,0,0);
      stripA.setPixelColor(126,0,0,0);
      stripA.setPixelColor(125,0,0,0);
      stripA.setPixelColor(124,0,0,0);
      stripA.show();
       
    }
  }
  }
  




