# Created: 03/11/19
# Author: Connor McNaboe
# Prupose: Configuration settings for flask application

import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'defualt-string-to-change'
    FLASK_ENV=development