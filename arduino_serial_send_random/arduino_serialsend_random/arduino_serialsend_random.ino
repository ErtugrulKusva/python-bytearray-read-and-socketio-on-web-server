#include <SoftwareSerial.h>
//Machover
SoftwareSerial Xbee = SoftwareSerial(0,1);
byte sensordeger[1]={};
byte gonData[19]={};
int counter = 0;
int incomingByte;
byte dizi[3]={};


void setup()
{ 
  //setting baudrate
  Xbee.begin(9600);
  
} 

void loop()
{  
  sendArray();   
}


void sendArray(){
  Xbee.flush();
  byte gonData[20] ={};
  float temperature = random(-400,850)/10.00;
  if(temperature < 0){gonData[2] = 0; temperature = temperature* (-1);} else{gonData[2]=1;}  
  int temperatureH = (temperature*10) /256;
  gonData[0] = temperatureH;
  int temperatureL = (temperature*10) - (temperatureH * 256);
  gonData[1] = temperatureL;
  float height =random(0,50000)/10.0;
  int heightH= (height*10)/256;
  gonData[3]=heightH;
  int heightL= (height*10)-(heightH*256);
  gonData[4]=heightL;
  float humidity=random(0,1000)/10.0;
  int humidityH = (humidity*10)/256;
  gonData[5]=humidityH; 
  int humidityL = (humidity*10) -(humidityH*256);
  gonData[6]=humidityL;
  float pressure=random(8000,12000)/10.0;
  int pressureH= (pressure*10)/256;
  gonData[7]=pressureH;
  int pressureL= (pressure*10)-(pressureH*256);
  gonData[8]=pressureL;
  int hiz=random(0,200);
  gonData[9]=hiz;
  float gyroX=random(-2500,2500)/10.0;
  if(gyroX < 0){gonData[12]=0; gyroX = gyroX * (-1);} else{gonData[12]=1;}
  int gyroXH=(gyroX*10)/256;
  gonData[10]=gyroXH;
  int gyroXL=(gyroX*10)-(gyroXH*256);
  gonData[11]=gyroXL;
  float gyroY=random(-2500,2500)/10.0;
  if(gyroY < 0){gonData[15]=0; gyroY = gyroY *(-1);} else{gonData[15]=1;}
  int gyroYH=(gyroY*10)/256;
  gonData[13]=gyroYH;
  int gyroYL=(gyroY*10)-(gyroYH*256);
  gonData[14]=gyroYL;
  float gyroZ=random(-2500,2500)/10.0;
  if(gyroZ < 0){gonData[18]=0; gyroZ = gyroZ *(-1);} else{gonData[18]=1;}
  int gyroZH=(gyroZ*10)/256;
  gonData[16]=gyroZH;
  int gyroZL=(gyroZ*10)-(gyroZH*256);
  gonData[17]=gyroZL;
  int sumD = 0;
  for(int i=0; i<sizeof(gonData)-1;i++){    
    sumD += gonData[i];    
    }
    int meanD;
    meanD=sumD / 19;
    //Serial.println(meanD);    
    gonData[19] = meanD;
    
    //Serial.println(sizeof(gonData));
    Xbee.write(gonData,sizeof(gonData));
    delay(200);
    
 
  }
