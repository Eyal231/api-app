# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app/main.py /app
COPY app/book-dict.json /app
COPY app/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt  # Corrected path to requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3001"]  # Changed host to 0.0.0.0
