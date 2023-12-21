#!/bin/bash

# Command for building python image
docker build -t python ./python

# Command for building postgres image
docker build -t postgres ./postgres

# Command for running docker-compose services in a detached mode
docker-compose up #-d