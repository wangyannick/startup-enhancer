# Docker file for the python server in 3.8.3-slim
FROM python:3.8.3-slim
# Set the working directory to /server
WORKDIR /server

# Copy the current directory contents into the container at /server
COPY . /server

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 3333

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "3333"]
