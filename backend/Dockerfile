# Use an official Python runtime as a parent image
# FROM python:3.9-slim
# FROM python:3.10-slim
FROM mirror.gcr.io/library/python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]