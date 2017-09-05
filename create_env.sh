#!/bin/bash

## Create a virtualenv, and activate this:
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python run.py
