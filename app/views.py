from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
# Testing Material
	entry = [
	{
		'dates':'03-15-2016',
		'times':'21:34',
		'pilotage':'Here',
		'course':'360',
		'speed':'6 kts',
		'miles':'5',
		'comment':'First Entry',
		'portoforigin':'East 55th',
		'portofcall':'Lorain'},
		{
                'dates':'03-15-2016',
                'times':'21:50',
                'pilotage':'There',
                'course':'0',
                'speed':'6 kts',
                'miles':'5',
                'comment':'Second Entry',
                'portoforigin':'Lorain',
                'portofcall':'East 55th'}
]
	return render_template('index.html',
				title='Logbook - Home',
				entry=entry)
