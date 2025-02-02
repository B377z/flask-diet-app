from flask import Flask, render_template, request, redirect, url_for, flash
from forms import MealForm  # Ensure `forms.py` exists with `MealForm`
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Ensure `config.py` exists with `Config`
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Define the `Meal` model
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Meal {self.name}>'
    
# Create the database
@app.before_request
def before_request():
    if not hasattr(app, 'db_initialized'):
        app.db_initialized = True
        db.create_all()


@app.route('/')
def index():
    app_name = 'Diet Tracker App'
    return render_template('index.html', app_name=app_name) 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/meals')
def meals():
    meals = Meal.query.all()
    return render_template('meals.html', meals=meals)  # Use `meals_list` (not `meals` function)

@app.route('/add_meal', methods=['GET', 'POST'])
def add_meal():
    form = MealForm()
    if form.validate_on_submit():
        existing_meal = Meal.query.filter_by(name=form.meal_name.data).first()
        
        if existing_meal:  # If the meal already exists, show a message
            flash(f'Meal "{existing_meal.name}" already exists!', 'warning')
            return redirect(url_for('meals'))

        new_meal = Meal(name=form.meal_name.data, calories=form.calories.data)
        db.session.add(new_meal)
        db.session.commit()
        flash(f'Meal "{new_meal.name}" added successfully!', 'success')
        return redirect(url_for('meals_list'))
        
    return render_template('add_meal.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
