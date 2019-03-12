# Created: 03/11/19
# Author: Connor McNaboe
# Purpose: Sets routes/urls to be requested by usesrs

from flask import render_template, flash, request, redirect, url_for
from app import app
from app.fields import CalcFields

# Set routes and allowed methods
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

# Configure functions/procedures allowed on /index page
def index():
    form = CalcFields()
    answer = ''
    if form.validate_on_submit():
        int1 = form.integer1.data
        int2 = form.integer2.data
        # Evaluate input integers
        if form.add.data:
            # Addition
            answer = str(int1 + int2)
        elif form.subtract.data: 
            # Subtraction
            answer = str(int1 - int2)
        elif form.multiply.data: 
            # Multiplicaiton
            answer = str(int1*int2)
        elif form.divide.data:
            # Division
            answer = str(int1 / int2)
        elif form.clear.data: 
            # Clear results and integers
            answer = ''
            form.integer1.data = ''
            form.integer2.data = ''
            return redirect(url_for('index'))
    return render_template('index.html', title='Web Calc Home', form=form, answer=answer)