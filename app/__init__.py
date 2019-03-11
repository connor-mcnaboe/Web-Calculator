# Created: 03/11/19
# Author: Connor McNaboe
# Initalizes flask web applicaiton 


from flask import Flask

app = Flask(__name__)

from app import routes