from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.get('/')
def get_homepage():
    return render_template("homepage.html")

@routes.get('/document')
def get_document():
    return render_template("document.html")

@routes.get('/about')
def get_about():
    return render_template("about.html")