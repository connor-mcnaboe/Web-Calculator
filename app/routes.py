# Created: 03/11/19
# Author: Connor McNaboe
# Purpose: Sets routes/urls to be requested by usesrs

from flask import render_template
from app import app
from app.fields import CaclFields

@app.route('/')
@app.route('/index')
def index():
    form = CaclFields()
    result = '' 
    if form.validate_on_submit():
        
    return render_template('index.html', title='Web Calc Home', form=form)