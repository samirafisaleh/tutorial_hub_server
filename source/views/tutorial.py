

from flask import Blueprint

bp = Blueprint("tutorial", __name__, url_prefix='/tutorial')

@bp.route("/", methods=['POST'])
def create():
    return "<p> Create Tutorial </p>"


@bp.route("/<int:id>/", methods=['GET'])
def retrieve(id):
    return f"<p> Get tutorial: {id} </p>"


@bp.route("/", methods=['GET'])
def list():
    return f"<p> List tutorials </p>"


@bp.route("/", methods=['DELETE'])
def delete():
    return f"<p> Delete tutorials </p>"