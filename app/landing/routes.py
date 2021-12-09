from flask import render_template
from flask import Blueprint

# create instance of blueprint
landing = Blueprint('landing', __name__, template_folder='landing_templates')

@landing.route('/landing/main')
def landingHome():
    return render_template('landing.html')