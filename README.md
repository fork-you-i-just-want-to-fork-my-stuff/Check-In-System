# Check-In-System

A check in system designed in flask

# Running locally
to run locally simply make sure you meet the requirements; run: pip install --trusted-host pypi.python.org -r requirements.txt

and then use: python routes.py

to start, by default youll be able to view it in browser by navigating to http://localhost:5000

# Docker info

If your so inclined this will run on docker, follow instructions below

# Building versions

To build the docker container run: docker build -t nameOfBuild

# Running

To run the bash of the container run: docker run -it nameOfBuild bash

# Notes

You can forward the docker image to expose localhost ports on the host machine by using docker run -d -p port:port .
