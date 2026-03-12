#!/bin/bash

# move into Backend folder
cd Backend

# install dependencies
pip install -r requirements.txt

# start FastAPI app
gunicorn --bind=0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker Backend.app:app