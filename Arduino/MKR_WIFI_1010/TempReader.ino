#include "Arduino_BHY2Host.h"

Sensor temp(SENSOR_ID_TEMP);
unsigned long startMillis = 0;
bool streaming = false;

void setup() {
  Serial.begin(115200);

  // Start communication with Nicla
  BHY2Host.begin();
  temp.begin();
  while (!Serial) {
    ;
  }
}

void loop() {

  // Update BHY2 data
  BHY2Host.update();

  // Process commands from Python
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "START") {
      streaming = true;
      startMillis = millis();
    }

    if (cmd == "STOP") {
      streaming = false;
    }
  }

  if (streaming) {
    Serial.print(millis() - startMillis);
    Serial.print(",");
    Serial.println(temp.value(), 2);
  }
}