#!/usr/bin/env bash

pip install --upgrade pip setuptools && pip install -r requirements.txt

flask run --host 0.0.0.0
