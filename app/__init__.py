# Created: 03/11/19
# Author: Connor McNaboe
# Initalizes flask web applicaiton/configuration settings


from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes