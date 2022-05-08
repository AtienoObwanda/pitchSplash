from flask import render_template
from . import main


pitches = [
    {
        'author': 'Atieno Obwanda',
        'content': 'Here and now... Today and always',
        'date_posted': 'April 20, 2022'
    },
    {
       
        'author': 'Mishie Gee',
        'content': 'As above, as Below',
        'date_posted': 'June 20, 2022'
    },
    {
       
        'author': 'Mishie Gee',
        'content': 'As above, as Below',
        'date_posted': 'June 20, 2022'
    },
    {
       
        'author': 'Mishie Gee',
        'content': 'As above, as Below',
        'date_posted': 'June 20, 2022'
    },
    {
       
        'author': 'Mishie Gee',
        'content': 'As above, as Below',
        'date_posted': 'June 20, 2022'
    },
    {
       
        'author': 'Mishie Gee',
        'content': 'As above, as Below',
        'date_posted': 'June 20, 2022'
    }
]











# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html', pitches=pitches)