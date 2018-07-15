# pull in official python version 3.7
from python:3.7  

# Create a working directory
WORKDIR /check-in

# Add everytthing from working directory to install
ADD . /check-in

#Install Python Dependencies through pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt


