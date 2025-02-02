from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, NumberRange

class MealForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    meal_name = StringField('Meal Name', validators=[DataRequired(), Length(min=2, max=100)])
    calories = IntegerField('Calories', validators=[DataRequired(), NumberRange(min=1, max=1000)])
    submit = SubmitField('Add Meal')