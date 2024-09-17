from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Specify name of puppy`s owner: ', validators=[DataRequired()])
    id = IntegerField('Specify id of the puppy: ', validators=[DataRequired()])
    submit = SubmitField('Add owner ')