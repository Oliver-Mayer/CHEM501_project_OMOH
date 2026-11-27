import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

if os.path.exists("sensor_data.db"):
    os.remove("sensor_data.db")

conn = sqlite3.connect("sensor_data.db")
cursor = conn.cursor()
csv_folder = "data"
experiment_id = 1

cursor.execute("""
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    experiment_id INTEGER,
    timestamp TEXT,
    temperature REAL,
    humidity REAL
)
""")

conn.commit()

for file in os.listdir(csv_folder):
    if file.endswith(".csv"):
        path = os.path.join(csv_folder, file)

        df = pd.read_csv(path)

        df["experiment_id"] = experiment_id

        df.to_sql(
            "readings",
            conn,
            if_exists="append",
            index=False
        )

        experiment_id += 1
        

df = pd.read_sql("""
SELECT *
FROM readings
""", conn)


conn.close()
print(df)