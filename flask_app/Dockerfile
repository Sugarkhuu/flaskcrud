# Use the official Python image as the base image
FROM python:3.9.13

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the Flask app code into the container
COPY . .

# Expose port 5000
EXPOSE 5000

ENV FLASK_APP=bookshop.py

# Run the Flask app
CMD flask run --host=0.0.0.0