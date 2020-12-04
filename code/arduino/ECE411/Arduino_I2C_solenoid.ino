#include <Wire.h>
#define RELAY 4 //relay pin 
//////////////////////////
// Add in void setup
////////////////////////////
void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  pinMode(RELAY, OUTPUT);
  digitalWrite(RELAY, LOW);
}

//////////////////////////
// Just a function 
///////////////////////////
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    digitalWrite(ledPin, c);
  }
}
