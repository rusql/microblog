from flask import render_template
from app import app_instance

@app_instance.route('/')
@app_instance.route('/index')
def index():
    user  = {'username': 'Russell'} #creating a mock user

    posts = [
        {
            'author': {'username':'Russell'},
            'body': 'Cool, clear day in Cape Town'
        },
        {
            'author': {'username':'Susan'},
            'body': 'Camps bay is great'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
