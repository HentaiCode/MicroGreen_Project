from flask import render_template, redirect, Blueprint

bp = Blueprint('MicroGreen', __name__, url_prefix='/MicroGreen')


@bp.route('/')
def index():
    pass
