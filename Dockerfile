# Use an official Python runtime as a parent image for Windows
FROM python:3.8-slim

# Set the working directory to C:\app
WORKDIR /app

# Copy the current directory contents into the container at C:\app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "app.py"]
