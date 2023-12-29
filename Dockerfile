
# Start with a Python 3.9 base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary libraries for GUI support
RUN apt-get update && apt-get install -y python3-tk x11-apps curl iputils-ping net-tools dnsutils

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for visualizer/app.py
EXPOSE 8000

# gui test
RUN apt update -y &&\
    apt-get install x11-apps -y;

# Set an entry point that runs a shell for interactive mode
ENTRYPOINT ["/bin/bash"]
