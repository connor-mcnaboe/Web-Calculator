# Created: 03/11/19
# Author: Connor McNaboe
# Purpose: Defines fields needed for calculator arithemtic

from flask_wtf import FlaskForm
from wtforms import IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CalcFields(FlaskForm):
    integer1 = IntegerField('Enter Integer 1', validators=[DataRequired()])
    integer2 = IntegerField('Enter Integer 2', validators=[DataRequired()])
    add = SubmitField('+')
    subtract = SubmitField('-')
    multiply = SubmitField('X')
    divide = SubmitField('/')
    clear = SubmitField('Clear')