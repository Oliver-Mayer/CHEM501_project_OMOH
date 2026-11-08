#include "Arduino_BHY2Host.h"

Sensor temp(SENSOR_ID_TEMP);
Sensor gas(SENSOR_ID_GAS);
Sensor baro(SENSOR_ID_BARO);
Sensor hum(SENSOR_ID_HUM);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  BHY2Host.begin();
  temp.begin();
  gas.begin();
  baro.begin();
  hum.begin();
}

void loop() {
  BHY2Host.update();

  Serial.print(temp.value());
  Serial.print(",");

  Serial.print(gas.value());
  Serial.print(",");

  Serial.print(baro.value());
  Serial.print(",");
  
  Serial.println(hum.value());
  delay(50);
}
