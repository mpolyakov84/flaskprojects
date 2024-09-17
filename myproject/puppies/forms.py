from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField('Specify name of puppy: ', validators=[DataRequired()])
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField('Specify id of puppy yuo want to delete: ', validators=[DataRequired()])
    submit = SubmitField('Delete Puppy')