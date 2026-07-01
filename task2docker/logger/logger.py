import time
import os

file_path = "/data/sensor_data.txt"

print("Logger service started. Waiting for data...", flush=True)

# Wait until the sensor container creates the file
while not os.path.exists(file_path):
    time.sleep(0.5)

# Open the file and start reading from the end
with open(file_path, "r") as f:
    # Go to the end of the file
    f.seek(0, 2)
    
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)  # Sleep briefly if no new data
            continue
        print(f"[Logger Recieved] {line.strip()}", flush=True)