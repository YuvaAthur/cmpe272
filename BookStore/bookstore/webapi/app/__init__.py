from flask import Flask

app = Flask(__name__)  #configures Flask to load associated files
app.config.from_object('config')

#for testing
from app import routescode

# API Code
from app import routes #app is Flask instance in this package

