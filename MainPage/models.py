from datetime import datetime
from MainPage import db, login_manager,app
from flask_login import UserMixin
import pytz
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer



# used to load logged in user on load of page
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model,UserMixin):
	# backref allows us to access the user who created the post
	# and will have one or many post so one to many relationship
	# db.reltionship references class Post
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(20),unique = True,nullable = False)
	email = db.Column(db.String(120),unique = True,nullable = False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60),nullable = False)
	posts = db.relationship('Post',backref = 'author',lazy = True) 
	
	
	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	# Foreign key is referencing table name and column name so lower case characters

	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(100),nullable = False)
	date_posted = db.Column(db.DateTime(), nullable=False, default=datetime.now(pytz.timezone('Asia/Kolkata')))
	content = db.Column(db.Text,nullable = False)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False) 

	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}','{self.content}')"

