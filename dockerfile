# Use a lightweight official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script into the container
COPY Main.py .

# Command to run your script
CMD ["python", "Main.py"]