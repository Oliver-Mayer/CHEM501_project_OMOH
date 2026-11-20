import numpy as np
import serial
import time
import pandas as pd
from datetime import datetime

runtime = 300
start_time = time.time()
# initial empty dictionary  to store data in
data_dict = {"timestamp": [],
             "temp": [], 
             "gas": [], 
             "pressure": [], 
             "humidity": []}

# define which com port is used
dev = "COM3"
mkr = serial.Serial(dev, 115200, timeout = 1)

while time.time() - start_time < runtime:
    # read the incoming data
    print(time.time() - start_time)
    line = mkr.readline().decode("utf-8").strip()
    print(line)
    # split the data at commas
    parts = line.split(",")
    #only append the data when there is the expected number of values.
    if len(parts) == 4:
        data_dict["timestamp"].append(datetime.now())
        data_dict["temp"].append(float(parts[0]))
        data_dict["gas"].append(float(parts[1]))
        data_dict["pressure"].append(float(parts[2]))
        data_dict["humidity"].append(float(parts[3]))       
    else:
        pass

#convert dictioary to dataframe with pandas
df = pd.DataFrame(data_dict)
meta = {
    "environment": "normal",
    "sensor": "Nicla Vision Temp",
    "runtime": runtime,
    "sampling_rate": "50ms",
    "start_time": start_time
}

# convert dictionary to dataframe
df = pd.DataFrame(data_dict)

# define file for it to be stored into
filename = rf"C:\Users\olima\OneDrive\Documents\GitHub\CHEM501_project\Data\Raw\normal\sensor_data{datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss')}.csv"
with open(filename, "w", newline = "") as f:
    for key, value in meta.items():
        f.write(f"# {key}: {value}\n")

    df.to_csv(f, index = False)