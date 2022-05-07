from flask import render_template
from app import app


Pitches = [
    {
        'author': 'Atieno Obwanda',
        'pitchContent': 'Here and now... Today and always',
        'date_posted': 'April 20, 2022'
    },
    {
       
        'author': 'Mishie Gee',
        'pitchContent': 'As above, as Below',
        'date_posted': 'June 20, 2022'
    }
]











# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html', Pitches=Pitches)