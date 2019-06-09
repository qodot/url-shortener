#!/usr/bin/env bash

source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
alembic upgrade head
python manage.py run
