from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange, AnyOf


class LuckyForm(FlaskForm):

    name = StringField('Name', validators=[InputRequired()])

    email = StringField('Email', validators=[InputRequired()])

    year = IntegerField('Year', validators=[InputRequired(), NumberRange(
        min=1900, max=2000, message="Error - year must be between 1900 and 2000.")])

    color = StringField('Color', validators=[
                        InputRequired(), AnyOf(['red', 'green', 'orange', 'blue'], message="Error - color must be one of: red, green, orange, blue.")])
