# Created: 03/11/19
# Author: Connor McNaboe
# Purpose: Sets routes/urls to be requested by usesrs

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"