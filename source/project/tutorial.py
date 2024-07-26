''' Module '''

from flask import Blueprint

bp = Blueprint("tutorial", __name__, url_prefix='/tutorial')

@bp.route("/", methods=['POST'])
def create():
    ''' Function '''
    return "<p> Create Tutorial </p>"


@bp.route("/<int:id>/", methods=['GET'])
def retrieve(_id):
    ''' Function '''
    return f"<p> Get tutorial: {_id} </p>"


@bp.route("/", methods=['GET'])
def list():
    ''' Function '''
    return "<p> List tutorials </p>"


@bp.route("/", methods=['DELETE'])
def delete():
    ''' Function '''
    return "<p> Delete tutorials </p>"
