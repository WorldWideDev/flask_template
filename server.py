from flask import Flask, render_template, redirect, flash, request as req, session
from apps.logreg import logreg

app = Flask(__name__)
app.register_blueprint(logreg)
app.secret_key = 'secrettts'

app.run(debug=True)
