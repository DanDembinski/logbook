from flask.ext.wtf import Form
from wtforms import StringField, IntegerField

class LogData(Form):
	dates = StringField('dates')
	times = StringField('times')
	pilotage = StringField('pilotage')
	course = StringField('course')
	speed = IntegerField('speed')
	miles = IntegerField('miles')
	comments = StringField('comments')
	portoforigin = StringField('portoforigin')
	portofcall = StringField('portofcall')
