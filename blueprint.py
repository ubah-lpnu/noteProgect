from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/start')
STUDENT_ID = 2

@api_blueprint.route("/hello-world")
def hello_world_def():
    return f"Hello world!!!"

@api_blueprint.route(f"hello-world-{STUDENT_ID}")
def hello_world():
    return f"Hello world {STUDENT_ID}"