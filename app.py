from flask import Flask, render_template, request, redirect, url_for, flash
from forms import MealForm  # Ensure `forms.py` exists with `MealForm`

app = Flask(__name__)
app.config['SECRET_KEY'] = 'k33p-!t-s3cr3t'

meals_list = []  # Temporary storage for meals (renamed from `meals` to avoid conflict)

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
    return render_template('meals.html', meals=meals_list)  # Use `meals_list` (not `meals` function)

@app.route('/check_meals')
def check_meals():
    return render_template('check_meals.html', meals=meals_list)  # Use `meals_list`

@app.route('/add_meal', methods=['GET', 'POST'])
def add_meal():
    form = MealForm()
    if form.validate_on_submit():
        meal_name = form.meal_name.data
        calories = form.calories.data
        meals_list.append({'meal_name': meal_name, 'calories': calories})  # Use `meals_list`
        flash(f'{meal_name} added successfully!', 'success')
        return redirect(url_for('meals'))  # Redirect to `/meals` correctly
    return render_template('add_meal.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
