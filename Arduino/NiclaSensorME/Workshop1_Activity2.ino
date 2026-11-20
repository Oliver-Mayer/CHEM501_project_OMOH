// Add libraries - these are bits of code that other people have used for us.
#include "Arduino.h"
#include "Arduino_BHY2.h"

void setup(){
  // Open the serial port - communicate at 115200 bits per second.
  Serial.begin(115200);

  // Use inter-integrated cirtuit (I2C) to communicate with MKR.
  // Communicate using the ESLOV cable.
  BHY2.begin(NICLA_I2C, NICLA_VIA_ESLOV);
}

void loop(){
  // Update and then sleep
  BHY2.update(1);
}
