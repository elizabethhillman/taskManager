from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Optional
from wtforms.fields.html5 import DateField, TimeField


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class ChangePasswordForm(FlaskForm):
    oldpassword = PasswordField('Old Password', validators=[DataRequired()])
    newpassword = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Save Change')

class NewTask(FlaskForm):
    addtask = StringField('New Task', validators=[DataRequired()])
    estimatehr = SelectField('Hours:', choices = [0,1,2,3])
    estimatemin = SelectField('Minutes:', choices =[0,5,10,15,20,25,30,25,40,45,50,55])
    priority = SelectField('Priority', choices=[(1, '1'),(2, '2'),(3, '3')], validators=[DataRequired()])
    category = SelectField('Category', choices=[], validators=[DataRequired()])
    submit = SubmitField('Add')
    
class EditTask(FlaskForm):
    edittask = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Save Changes')
    cancel = SubmitField('Cancel')

class CreateCategory(FlaskForm):
    addcategory = StringField('Create Category', validators=[DataRequired()])
    submit = SubmitField('Create')

class Reminder(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    selectTime = SelectField('Want Chose a Time for reminder',choices=[(1, 'yes'),(2, 'none')], validators=[DataRequired()])
    time = TimeField('Time', validators=[Optional()])
    startorcomplet = SelectField('Select', choices=[(1, 'Start'),(2, 'Need to complete'),(3, 'Both')], validators=[DataRequired()])
    submit = SubmitField('Done')

class Addsubtask(FlaskForm):
    addsubtask = StringField('New Subtask', validators=[DataRequired()])
    submit = SubmitField('Add')

class Addcollaborator(FlaskForm):
    addcollaborator = StringField('Collaborator', validators=[DataRequired()])
    submit = SubmitField('Add')
    
class AssignUser(FlaskForm):
    assignuser = StringField('Assign Task to User', validators=[DataRequired()])
    submit = SubmitField('Assign')

class AddEvent(FlaskForm):
    addtitle = StringField('Title', validators=[DataRequired()])
    adddate = DateField('Date', validators=[DataRequired()])
    submit = SubmitField('Add')