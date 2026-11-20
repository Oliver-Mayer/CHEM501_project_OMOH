import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def scatter_data(filename):
    # Read the CSV
    df = pd.read_csv(filename)

    # Convert timestamps
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Create figure with 2 graphs side-by-side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Temperature graph
    ax1.scatter(df["timestamp"], df["temperature"], color="red")
    ax1.set_title("Temperature vs Time")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Temperature (°C)")

    # Humidity graph
    ax2.scatter(df["timestamp"], df["humidity"], color="blue")
    ax2.set_title("Humidity vs Time")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Humidity (%)")

    graph_name = f"graph_for_{filename.replace('.csv', '.png')}"

    plt.tight_layout()
    plt.savefig(graph_name, dpi=300)
    plt.show()