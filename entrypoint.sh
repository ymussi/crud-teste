#!/bin/bash

cd /app/crud

uwsgi --ini /app/crud/app.ini
