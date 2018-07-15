# Check-In-System

A check in system designed in django


# Building versions

To build the docker container run: docker build -t <nameOfBuild>

# Running

To run the bash of the container run: docker run -it <nameOfBuild> bash

# Notes

You can forward the docker image to expose localhost ports on the host machine by using docker run -d -p <port>:<port> .