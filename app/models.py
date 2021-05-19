from app import db
from datetime import datetime
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collaborate = db.Column(db.Integer, unique=False)
    username = db.Column(db.String, nullable=False, unique=False)
    email = db.Column(db.String(32), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), unique=False)

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    content = db.relationship('Task', backref='author', lazy='dynamic' )
    category = db.relationship('Category', backref='author', lazy='dynamic')
    event = db.relationship('Event', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def check_username(self, username):
        if username != self.username:
            return False
        return True
    def __repr__(self):
        return '<User {}>'.format(self.username)    
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Posts {}>'.format(self.body)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String, unique=False, nullable=False)
    complete = db.Column(db.Boolean, default=False)
    estimatehr = db.Column(db.Integer, nullable = True)
    estimatemin = db.Column(db.Integer, nullable = True)
    priority = db.Column(db.Integer, nullable=False)
    collaborate_id = db.Column(db.Integer, nullable=True, unique=False)
    assign_user = db.Column(db.String,unique=False, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('categories', lazy=True))
    subtask = db.relationship('Subtask', backref = 'subtasks', lazy = 'dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   
    # def __init__(self, content, priority, user_id):
    #     self.content = content
    #     self.priority = priority
    #     self.user_id = user_id
    #     self.done = False

    def __repr__(self):
        return f'<Task: {self.content}>'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=False, nullable=False)
    date = db.Column(db.DateTime, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Event: {self.title}>'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Category: {self.category}>'

class Subtask(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subtask = db.Column(db.String(30), unique=False, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))

    def __repr__(self):
        return f'<Subtask: {self.subtask}>'

    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
db.create_all()
db.session.commit()

'''
The code above will store the dictrionaries into their appropriate columns in the database.
This allows for the other files in this app to return the objects. 
'''
