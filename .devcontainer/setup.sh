#! /bin/sh

sudo apt-get update && sudo apt-get install ffmpeg libsm6 libxext6  -y
pip install -r ../requirements.txt
