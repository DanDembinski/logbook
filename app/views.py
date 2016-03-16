from flask import render_template
from app import app, db
from .models import entry
from .settings import *

@app.route('/')
@app.route('/index')
def index():
	entries = entry.query.all()
	return render_template('index.html',
				title=shipname+'- Home',
				shipname=shipname,
				entry=entries)

@app.route('/add')
def add():
	return render_template('add.html',
				title=shipname+'- Add',
				shipname=shipname)
#@app.route('/port/<PoO>')
@app.route('/port/<misc>')
def port(misc):

	PoO = entry.query.filter_by(portoforigin=misc).all()
	PoC = entry.query.filter_by(portofcall=misc).all()
	return render_template('port.html',
				port=misc,
				PoO=PoO,
				PoC=PoC,
				shipname=shipname)
