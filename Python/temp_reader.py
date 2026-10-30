import serial
import time
import csv
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


dev = 'COM3'

# Open serial connection
mkr = serial.Serial(dev, 115200, timeout=1)

def send(cmd):
    mkr.write((cmd + "\n").encode())

# Tell Arduino to start streaming
send("START")

runtime = 10
start_time = time.time()
data_dict = {"time": [], "temp": []}

# read the data and append it to a list while within the time bound
while time.time() - start_time < runtime:
    line = mkr.readline().decode("utf-8").strip()
    print(line)
    parts = line.split(",")
    if len(parts) == 2:
        t = parts[0]
        temp = parts[1]
        if float(temp) <= 1:
            pass
        elif float(temp) > 50:
            pass
        try:
            data_dict["time"].append(float(t)/1000)
            data_dict["temp"].append(float(temp))
        except ValueError:
            pass

# Tell Arduino to stop streaming
send("STOP")
meta = {
    "sensor": "Nicla Vision Temp",
    "runtime": runtime,
    "sampling_rate": "50ms",
    "start_time": start_time
}

# convert dictionary to dataframe
df = pd.DataFrame(data_dict)

filename = f"temp_data_{datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss')}.csv"
with open(filename, "w", newline = "") as f:
    for key, value in meta.items():
        f.write(f"# {key}: {value}\n")

    df.to_csv(f, index = False)