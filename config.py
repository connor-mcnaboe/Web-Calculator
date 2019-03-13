# Created: 03/11/19
# Author: Connor McNaboe
# Prupose: Configuration settings for flask application

import os 
from dotenv import load_dotenv

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'defualt-string-to-change'
    dotenv_path = str.join(os.path.dirname(__file__), '.flaskenv') 
    load_dotenv(dotenv_path)