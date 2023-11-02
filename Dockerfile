# Using the Ubuntu image (our OS)
FROM ubuntu:latest

USER root
# Update package manager (apt-get) 
# and install (with the yes flag `-y`)
# Python and Pip
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip

RUN pip install django pytils Pillow

# =====
# The new stuff is below
# =====

# Install our Python dependencies
# RUN pip install Requests Pygments

ADD . /workspaces/en_master

WORKDIR /workspaces/en_master