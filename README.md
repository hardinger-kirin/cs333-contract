# cs333-contract
Kirin Hardinger, Spring 2023

# Welcome to your new life as a boba tea café owner! :tea:

## Description

Enjoy a small memory game based in a world where you own a boba tea café! Play for as many days as you want, unlock exciting new ingredients to expand your shop's selections, and reload your game at any time later!

## How to run
To most reliably run this code and ensure all dependencies are included, a Docker image can be pulled at this repository: https://hub.docker.com/repository/docker/khardinger/cs333-contract/general

The main program can be executed using Docker by pulling the latest image from Dockerhub, then running it using the following command:

`docker run -i khardinger/cs333-contract:latest`

__It is important that the `-i` is included so that it is run interactively!__

## Testing information
Testing is executed using Python's `unittest` and measured using `Coverage.py`

Documentation for both can be found here:  
https://docs.python.org/3/library/unittest.html  
https://coverage.readthedocs.io/en/7.2.4/

This test suite includes <u>4</u> unit tests and <u>10</u> integration tests for over 75% code coverage.

## Deployment information

The workflow for this GitHub repository is set up such that a Docker image is only pushed to DockerHub if test suite passes with 75%+ code coverage. The latest image can be pulled from: https://hub.docker.com/repository/docker/khardinger/cs333-contract/general

# Thank you for stopping by!
