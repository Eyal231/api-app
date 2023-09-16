# Use an official Python runtime as a parent image
FROM alpine:3.17

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN apk update && apk add py3-pip  # Install pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy the current directory contents into the container at /app
COPY app/main.py /app
COPY app/book-dict.json /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3001"]  