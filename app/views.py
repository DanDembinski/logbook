from flask import render_template,flash,redirect,url_for
from app import app, db
from .models import entry
from .settings import *
from .forms import LogData, removeForm

@app.route('/')
@app.route('/index')
def index():
	entries = entry.query.all()
	return render_template('index.html',
				title=shipname+'- Home',
				shipname=shipname,
				entry=entries)

@app.route('/add', methods=['GET', 'POST'])
def add():
	form = LogData()

	if form.validate_on_submit():
		log=entry(dates=form.dates.data,times=form.times.data,pilotage=form.pilotage.data,course=form.course.data,speed=form.speed.data,miles=form.miles.data,comment=form.comments.data,portoforigin=form.portoforigin.data,portofcall=form.portofcall.data)
		db.session.add(log)
		db.session.commit()
		return redirect(url_for('index'))
		flash('Navigation data added')
	return render_template('add.html',
				title=shipname+'- Add',
				form=form,
				shipname=shipname)

@app.route('/remove', methods=['GET', 'POST'])
def remove():
	form = removeForm()
	if form.validate_on_submit():
		remove=form.number.data
		entry.query.filter_by(id=remove).delete()
		db.session.commit()

	entries = entry.query.all()
	return render_template('remove.html',
				title=shipname+'-Remove',
				entry=entries,
				shipname=shipname,
				form=form)
				

@app.route('/port/<misc>')
def port(misc):

	PoO = entry.query.filter_by(portoforigin=misc).all()
	PoC = entry.query.filter_by(portofcall=misc).all()
	return render_template('port.html',
				port=misc,
				PoO=PoO,
				PoC=PoC,
				shipname=shipname)
