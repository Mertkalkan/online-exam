#!/bin/bash
export FLASK_APP=./src/main.py
source 'C:\Users\mert\.virtualenvs\backend-a_oBeKNL\Scripts\activate'
export FLASK_ENV=development
flask run


# it sets ./src/main.py as the value of the FLASK_APP environment variable (this is needed by the last command);
# it activates the virtual environment;
# and it runs flask listening on all interfaces (-h 0.0.0.0).