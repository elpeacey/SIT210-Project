#include "Particle.h"
const int signalpin = A0;

bool chickensHome = false; 
int chickens;
int count = 0;


void setup() 
{
    Serial.begin(9600);
    
    pinMode(signalpin, INPUT); //Set pin as input
    
    Wire.begin(0x40); //Initialise argon on slave address 40
    Wire.onReceive(observeEvent); //When master device sends signal, call observeEvent
    
    Particle.variable("Returned", &chickensHome, BOOLEAN); //IFTTT
}


void loop() 
{
    if (digitalRead(signalpin) == HIGH) //If sensor detects motion add 1 to count
    {
        count += 1;
    }
    
    if (count == chickens) //If count is equal to number of chickens in flock than all chickens home
    {
        chickensHome = true;
    }

    delay(3500); //Average time it takes a chicken to walk through the door
}


void observeEvent(int bytes) {
    chickens = Wire.read(); //read value from RPi
    Serial.println("The number of chickens has been updated to: " + chickens);
}
