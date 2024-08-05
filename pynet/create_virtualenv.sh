#!/bin/bash

# This code needs to be executed in the root directory of 'pynet'.

virtualenv --python=3 "telEnv"
source "telEnv/bin/activate"
pip3 install -r requirements.txt

