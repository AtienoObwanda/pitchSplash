from flask import Blueprint

'''
Application Blue print
'''

main = Blueprint ('main', __name__)

from . import views, error

