''' Module '''
from logging.config import dictConfig

from flask import Flask, jsonify
# from celery import Celery, Task

# from source.tutorial import bp as tutorial_bp




app = Flask(__name__)


if app.config["DEBUG"] is True:
    LOG_FILENAME = "../../../../Logs/tutorial_hub_server/flask/logging.log"
else:
    LOG_FILENAME = "/logs/tutorial_hub_server/flask/logging.log"




dictConfig({
    "version" : 1,
    'formatters' : {

    },
    'handlers' : {
        'console' : {
            'class' : 'logging.StreamHandler',
            'level' : 'INFO'
        },
        'root_handler' : {
            'class' : 'logging.handlers.RotatingFileHandler',
            'level' : 'INFO',
            'filename' : LOG_FILENAME,
            'maxBytes' : 10485760,
            'backupCount' : 3
        }
    },
    'root' : {
        'handlers' : ['console']
    }


})





# def celery_init_app(app: Flask) -> Celery:
#     ''' celery initialization app '''

#     class FlaskTask(Task):
#         ''' Flask Task '''
#         def __call__(self, *args: object, **kwargs: object) -> object:
#             ''' Call function '''
#             with app.app_context():
#                 return self.run(*args, **kwargs)

#     celery_app = Celery(app.name, task_cls=FlaskTask)
#     celery_app.config_from_object(app.config["CELERY"])
#     celery_app.set_default()
#     app.extensions["celery"] = celery_app
#     return celery_app


# app.config.from_mapping(
#     CELERY=dict(
#         broker_url="redis://localhost",
#         result_backend="redis://localhost",
#         task_ignore_result=True,
#     ),
# )
# celery_app = celery_init_app(app)

app.config.from_prefixed_env()


print("DEBUG: ".ljust(40)                          + str(app.config["DEBUG"]))
print("TESTING: ".ljust(40)                        + str(app.config["TESTING"]))
print("PROPAGATE_EXCEPTIONS: ".ljust(40)           + str(app.config["PROPAGATE_EXCEPTIONS"]))
print("TRAP_HTTP_EXCEPTIONS: ".ljust(40)           + str(app.config["TRAP_HTTP_EXCEPTIONS"]))
print("TRAP_BAD_REQUEST_ERRORS: ".ljust(40)        + str(app.config["TRAP_BAD_REQUEST_ERRORS"]))
print("SECRET_KEY: ".ljust(40)                     + str(app.config["SECRET_KEY"]))
print("SESSION_COOKIE_NAME: ".ljust(40)            + str(app.config["SESSION_COOKIE_NAME"]))
print("SESSION_COOKIE_DOMAIN: ".ljust(40)          + str(app.config["SESSION_COOKIE_DOMAIN"]))
print("SESSION_COOKIE_PATH: ".ljust(40)            + str(app.config["SESSION_COOKIE_PATH"]))
print("SESSION_COOKIE_HTTPONLY: ".ljust(40)        + str(app.config["SESSION_COOKIE_HTTPONLY"]))
print("SESSION_COOKIE_SECURE: ".ljust(40)          + str(app.config["SESSION_COOKIE_SECURE"]))
print("SESSION_COOKIE_SAMESITE: ".ljust(40)        + str(app.config["SESSION_COOKIE_SAMESITE"]))
print("PERMANENT_SESSION_LIFETIME: ".ljust(40)     + str(app.config["PERMANENT_SESSION_LIFETIME"]))
print("SESSION_REFRESH_EACH_REQUEST: ".ljust(40)   + str(app.config["SESSION_REFRESH_EACH_REQUEST"]))
print("USE_X_SENDFILE: ".ljust(40)                 + str(app.config["USE_X_SENDFILE"]))
print("SERVER_NAME: ".ljust(40)                    + str(app.config["SERVER_NAME"]))
print("APPLICATION_ROOT: ".ljust(40)               + str(app.config["APPLICATION_ROOT"]))
print("PREFERRED_URL_SCHEME: ".ljust(40)           + str(app.config["PREFERRED_URL_SCHEME"]))
print("MAX_CONTENT_LENGTH: ".ljust(40)             + str(app.config["MAX_CONTENT_LENGTH"]))
print("TEMPLATES_AUTO_RELOAD: ".ljust(40)          + str(app.config["TEMPLATES_AUTO_RELOAD"]))
print("EXPLAIN_TEMPLATE_LOADING: ".ljust(40)       + str(app.config["EXPLAIN_TEMPLATE_LOADING"]))
print("MAX_COOKIE_SIZE: ".ljust(40)                + str(app.config["MAX_COOKIE_SIZE"]))

# app.register_blueprint(tutorial_bp)



class InvalidAPIUsage(Exception):

    def __init__(self, message, status_code=None, payload=None):
        super.__init__()

        self.message = message

        if status_code is not None:
            self.status_code = status_code 
        self.payload = payload 
    
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message 
        return rv 
    
@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code 

@app.route('/')
def root():
    ''' Root function '''
    return "<p>Hello World</p>"



