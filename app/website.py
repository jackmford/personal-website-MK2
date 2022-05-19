from flask import Blueprint
from flask import render_template

bp = Blueprint('website', __name__)


@bp.route('/')
def hello_world():
    return render_template('index.html')


@bp.route('/resume/')
def resume():
    return render_template('resume.html')
