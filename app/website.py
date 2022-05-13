from flask import Flask, Blueprint
from flask import render_template
import os

bp = Blueprint('website', __name__)


@bp.route('/')
def hello_world():
    return render_template('index.html')


@bp.route('/resume/')
def resume():
    return render_template('resume.html')


@bp.route('/about/')
def about():
    return render_template('about.html')
