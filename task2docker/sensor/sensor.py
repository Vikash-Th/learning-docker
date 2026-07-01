import random
import time
import os

# Define path inside the shared volume mount point
data_dir = "/data"
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "sensor_data.txt")

print("Sensor simulator started...", flush=True)

while True:
    reading = random.uniform(10.0, 50.0)
    # Open in append mode ('a') and flush immediately to ensure the logger can read it instantly
    with open(file_path, "a") as f:
        f.write(f"Sensor Reading: {reading:.2f}\n")
    
    print(f"[Sensor Info] Wrote: {reading:.2f}", flush=True)
    time.sleep(2)