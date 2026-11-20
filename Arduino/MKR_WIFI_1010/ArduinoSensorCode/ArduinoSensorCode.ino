#include "ArduinoMqttClient.h"
#include "Arduino.h"
#include "Arduino_BHY2Host.h"
#include "WiFiNINA.h"
#include "arduino_secrets.h"

Sensor temp(SENSOR_ID_TEMP);
Sensor hum(SENSOR_ID_HUM);
unsigned long startMillis = 0;

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = SECRET_SERVER;
int        port     = 1883;
const char topic1[] = "OM-OH/room1/temperature";
const char topic2[] = "OM-OH/room1/humidity";

//set interval for sending messages (milliseconds)
const long interval = 5000;
unsigned long previousMillis = 0;

int count = 0;

void setup() {
  //Initialize serial:
  Serial.begin(9600);
  BHY2Host.begin();

  temp.begin();
  hum.begin();

  // attempt to connect to Wifi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();
}

void loop() {
  // call poll() regularly to allow the library to send MQTT keep alive which
  // avoids being disconnected by the broker
  mqttClient.poll();

  unsigned long currentMillis = millis();

  BHY2Host.update();

  if (currentMillis - previousMillis >= interval) {
    // save the last time a message was sent
    previousMillis = currentMillis;

    //record random value from A0, A1 and A2
    float temperature = temp.value();
    float humidity = hum.value();

    Serial.print("Sending message to topic1: ");
    Serial.println(topic1);
    Serial.println(temperature);

    Serial.print("Sending message to topic2: ");
    Serial.println(topic2);
    Serial.println(humidity);

    // send message, the Print interface can be used to set the message contents
    mqttClient.beginMessage(topic1);
    mqttClient.print(temperature);
    mqttClient.endMessage();

    mqttClient.beginMessage(topic2);
    mqttClient.print(humidity);
    mqttClient.endMessage();

    Serial.println();
  }
}
