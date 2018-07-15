#!/bin/bash
docker build -t check-in .
docker run -it check-in bash
