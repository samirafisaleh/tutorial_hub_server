
from logging.config import dictConfig

from flask import Flask 

from source.views.tutorial import bp as tutorial_bp 


''' Configure logging '''
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
            'filename' : '../logs/some_logging.log',
            'maxBytes' : 10485760,
            'backupCount' : 3
        }
    },
    'root' : {
        'handlers' : ['console']
    }


})


app = Flask(__name__)


app.register_blueprint(tutorial_bp)



@app.route('/')
def root():
    return "<p>Hello World</p>"




