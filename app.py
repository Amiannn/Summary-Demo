from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

# # add config
# from cfg import config

# # server
# app.config['SERVER_NAME'] = config.SERVER_NAME

# add router
from router import *