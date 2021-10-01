####################################
# File name: models.py             #
# Author: Joe Abbate               #
####################################
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, FormField, DateTimeField, SelectField, Form
from wtforms.validators import DataRequired, Length
from wtforms.widgets.html5 import ColorInput

class EventForm(FlaskForm):
    name = StringField(('What is the name of the event?'), validators=[DataRequired(), Length(min=1, max=140)])
    address = StringField(('Where is the event?'), validators=[DataRequired()])
    start_date_time = DateTimeField(label="Start", validators=[DataRequired()], format='%Y-%m-%d %H:%M')
    end_date_time = DateTimeField(label="End", validators=[DataRequired()], format='%Y-%m-%d %H:%M')
    submit = SubmitField(('Submit'))

    def validate(self, extra_validators=None):
        if not Form.validate(self, extra_validators=extra_validators):
            return False
        if self.start_date_time.data > self.end_date_time.data:
            self.end_date_time.errors.append('End time must be after start time.')
            return False
        return True


class SizeForm(FlaskForm):
    capacity_choice = []
    for i in range(1, 11):
        capacity_tuple = (str(i), str(i))
        capacity_choice.append(capacity_tuple)
    max_capacity = SelectField((""), choices=capacity_choice,
    validators=[DataRequired()], default=2, render_kw={"class":"form-control"})


class CarForm(FlaskForm):
    max_capacity = FormField(SizeForm)
    departure_date_time = DateTimeField(label="Departure", validators=[DataRequired()], format='%Y-%m-%d %H:%M')
    return_date_time = DateTimeField(label="Return", validators=[DataRequired()], format='%Y-%m-%d %H:%M')
    comments = TextAreaField("Any Comments?")
    submit = SubmitField(('Submit'))

    def validate(self, extra_validators=None):
        if not Form.validate(self, extra_validators=extra_validators):
            return False
        if self.departure_date_time.data > self.return_date_time.data:
            self.return_date_time.errors.append('Return time must be after departure time.')
            return False
        return True

class ColorForm(FlaskForm):
    style = SelectField(u'RGB Style', 
        choices=[
            ("SOLID", "Solid"),
            ("PULSE", "Pulse"),
            ("LINE", "Moving Line"),
            ("RAINBOW", "Full Color Cycle")
        ], 
        validators=[DataRequired()]
    )
    numcolors = SelectField(u'Number of Colors', 
        choices=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3")
        ], 
        validators=[DataRequired()]
    )
    color1 = StringField(widget=ColorInput(), validators=[DataRequired()])
    color2 = StringField(widget=ColorInput(), validators=[DataRequired()])
    color3 = StringField(widget=ColorInput(), validators=[DataRequired()])
    submit = SubmitField(('Submit'), validators=[DataRequired()])
    def validate(self, extra_validators=None):
        if not Form.validate(self, extra_validators=extra_validators):
            return False
        return True