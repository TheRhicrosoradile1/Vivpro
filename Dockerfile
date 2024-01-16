# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the local src directory to the container at /app
COPY app/ /app/

# Expose port 8000 for FastAPI application
EXPOSE 8000

# Define environment variable to run FastAPI with Uvicorn
ENV MODULE_NAME=main
ENV VARIABLE_NAME=app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]