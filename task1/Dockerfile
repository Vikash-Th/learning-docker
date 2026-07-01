# Use the requested slim Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the script from your host machine to the container
COPY robot_info.py .

# Run the script when the container starts
CMD ["python", "robot_info.py"]
