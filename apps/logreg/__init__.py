from flask import Flask, render_template, redirect, flash, request as req, session, Blueprint
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'the_wall')

logreg = Blueprint('logreg', __name__, template_folder = '../templates', static_folder='static')
bcrypt = Bcrypt(app)

@logreg.route('/')
def index():
    return render_template('index.html')
