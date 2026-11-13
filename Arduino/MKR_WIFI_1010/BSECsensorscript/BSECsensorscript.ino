#include "Arduino_BHY2Host.h"

SensorBSEC bsec(SENSOR_ID_BSEC);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  BHY2Host.begin();
  bsec.begin();
  delay(5000);
}

void loop() {
  // put your main code here, to run repeatedly:
  BHY2Host.update();
  Serial.println(bsec.begin());
  Serial.println(String("BSEC info: ") + bsec.toString());
  delay(1000);
}
