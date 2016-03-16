from app import db

class entry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	dates = db.Column(db.String, index=True, unique=False)
	times = db.Column(db.String, index=True, unique=False)
	pilotage = db.Column(db.String(1000), index=True, unique=False)
	course = db.Column(db.Integer, index=True, unique=False)
	speed = db.Column(db.Integer, index=True, unique=False)
	miles = db.Column(db.Integer, index=True, unique=False)
	comment = db.Column(db.String(500), index=True, unique=False)
	portoforigin = db.Column(db.String(120), index=True, unique=False)
	portofcall = db.Column(db.String(120), index=True, unique=False)


class ports(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	desc = db.Column(db.String, index=True, unique=False)
	notes = db.Column(db.String, index=True, unique=False)
	vists = db.Column(db.String, index=True, unique=False)
	lastvisit=db.Column(db.String, index=True, unique=False)
	name=db.Column(db.String(120), index=True, unique=False) #linked with portoforigin/portofcall..Maybe. I need to read up on that some more
