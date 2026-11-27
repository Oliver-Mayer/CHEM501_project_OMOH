from paho.mqtt import client as mqtt
from datetime import datetime
import csv
import os
import grapher

current_humidity = None
current_temperature = None

header = ["timestamp", "temperature", "humidity"]

# Create folder if it doesn't exist
os.makedirs("data", exist_ok=True)

filename = os.path.join(
    "data",
    f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
)


if not os.path.exists(filename):
    with open(filename, "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(header)

def on_message(client, userdata, msg):
    global current_temperature
    global current_humidity

    value = float(msg.payload.decode())

    if "temperature" in msg.topic:
        current_temperature = value

    elif "humidity" in msg.topic:
        current_humidity = value

        if current_temperature is not None:
            with open(filename, "a", newline="") as f:
                writer = csv.writer(f)

                writer.writerow([datetime.now(),current_temperature,current_humidity])

client = mqtt.Client()

client.connect("pf-c0uudk9ksjw7kkm9chm5.cedalo.cloud",1883)

client.subscribe("OM-OH/#")

client.on_message = on_message

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("Stopping collection...")
    grapher.scatter_data(filename)