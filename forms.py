from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


class ModelForm(FlaskForm):
    x1 = FloatField('x1', validators=[DataRequired()])
    x2 = FloatField('x2', validators=[DataRequired()])
    x3 = FloatField('x3', validators=[DataRequired()])
    predict = SubmitField('predict')
