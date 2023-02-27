# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Upgrade pip
RUN python -m pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8001"]