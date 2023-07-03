# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install the project dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port your Flask app is running on (default is 5000)
EXPOSE 5000

# Set the entry point to run your Flask app
CMD ["python", "app.py"]
