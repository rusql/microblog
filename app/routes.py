from flask import render_template
from app import app_instance

@app_instance.route('/')
@app_instance.route('/index')
def index():
    user  = {'username': 'Bob'} #creating a mock user
    return render_template('index.html', title='Home', user=user)