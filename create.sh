#!/bin/bash

##move into the build context
cd docker;

##perform the build
docker build -t physics .;
