from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    app_name = 'Diet Tracker App'
    return render_template('index.html', app_name=app_name) # app_name is a variable that can be used in the template

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/meals')
def meals():
    meal_list = ['Rice & Beans', 'Plantain', 'Pasta', 'Egusi Soup', 'Fried Rice']
    return render_template('meals.html', meals=meal_list)

@app.route('/check_meals')
def check_meals():
    meals_available = []
    return render_template('check_meals.html', meals=meals_available)

if __name__ == '__main__':
    app.run(debug=True)
