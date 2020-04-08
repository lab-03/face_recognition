#!/bin/sh

if [ "$FLASK_ENV" == "development" ]; then
        python3 app.py
else
        gunicorn  app:app  -b 0.0.0.0:$PORT -w 3
fi

