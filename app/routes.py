from app import db
from app import app
from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, SignupForm, ChangePasswordForm, NewTask, EditTask
from werkzeug.security import check_password_hash
from app.models import User, Post, Task, Category


@app.route('/')
def index():
    return render_template('base.html')
@app.route('/taskboard',methods=['GET', 'POST'])

def taskboard():
    # user = current_user
    # taskList = (db.session.query(User, Task)
    #     .join(User)
    #     ).all()

    tasks = Task.query.all()
    # for item in taskList:
    #     #Add the item in the message list into the posts
    #     tasks.append(item.Task.content)
    return render_template('taskboard.html', tasks=tasks)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # User.query.filter_by() returns a list from the User table
        # first() returns first element of the list
        # the form.username.data is getting the info the user submitted in the form
        user = User.query.filter_by(username=form.username.data).first()
        # if no user found or password for user incorrect
        # user.check_password() is a method in the User class
        if user is None or not user.check_password(form.password.data):
            return f'''<html><body>
                        {form.username.data} Invalided username or password</b>
                        <a href="/login">Login</a>
                        </body>
                        </html>'''
        # let flask_login library know what user logged int
        # it also means that their password was correct
        login_user(user)
         # return to page before user got asked to login
        # for example, if user tried to access a wedpage called profile, but since they
        # weren't logged in they would get redirected to login page. After they log in
        # the user will be redirected to their previous request, which would be the profile
        # page in this case.
#        next_page = request.args.get('next')
#        if not next_page or url_parse(next_page).netloc != '':
#            next_page = url_for('index')
        return redirect("/")

    return render_template('login.html', title='Log In', form=form)

@app.route("/req")
# user needs to be logged in to see this page
# needs to be user route!
@login_required
# called view function
def req():
    return '''<html><body>
    User needs to be logged in
    </body>
    </html>'''

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        exiting_user = User.query.filter_by(username=form.username.data).first()
        if exiting_user is None or not exiting_user.check_username(form.username.data):
            password = generate_password_hash(form.password.data)
            newuser = User(username=form.username.data, email=form.email.data, password = password )
            db.session.add(newuser)
            db.session.commit()
            return f'''<html><body>
                        {form.username.data} Successfully Signed Up </b>
                        <a href="/login">Login</a>
                        </body>
                        </html>'''
        else:
            return f'''<html><body>
                        {form.username.data} already exixt </b>
                        <a href="/login">Login</a>
                        </body>
                        </html>'''
                        
    return render_template('signup.html', title='Sign up', form=form)

@app.route('/changepassword', methods = ['GET', 'POST'])
@login_required
def changepassword():
    user = current_user
    #print("current pass:" +user.password)
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not check_password_hash(user.password,form.oldpassword.data):
            #print(form.oldpassword.data)
            flash('Invalid password')
            return redirect('/changepassword')
        if check_password_hash(user.password,form.oldpassword.data):
            
            #print(form.newpassword.data)
            user.password = generate_password_hash(form.newpassword.data)
            db.session.add(user)
            db.session.commit()
            flash('Successful Change Password')
            return redirect('/changepassword')
    return render_template('changepassword.html', title = 'Change password', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/profile")
@login_required
def profile():
    user = current_user
    return render_template ('profile.html', title = 'My Account')

@app.route('/addtask', methods = ['GET', 'POST'])
@login_required
def newtask():
    user = User.query.filter_by(username=current_user.username).first()
    form = NewTask()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    #print(user.id)
    if form.validate_on_submit():
        task = Task(content=form.addtask.data, priority=form.priority.data, author=user)
        db.session.add(task)
        db.session.commit()
        print(task.user_id)
        return redirect('/taskboard')
    return render_template('addtask.html', title= 'Add task',form = form)
    
@app.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task_delete = Task.query.get(task_id)
    db.session.delete(task_delete)
    db.session.commit()
    return redirect("/taskboard")

@app.route('/edittask/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    form = EditTask()
    task = Task.query.get(task_id)
    
   

    if request.method == 'POST':
#        if request.form['cancel']:
#            return redirect('/taskboard')
        if form.validate_on_submit():
            task.content=form.edittask.data
            db.session.commit()
            return redirect('/taskboard')
        if request.form['cancel']:
            return redirect('/taskboard')
    return render_template('edittask.html', task = task.content, form=form)

@app.route('/priority')
@login_required
def filter_priority():

    tasks = Task.query.order_by(Task.priority.asc())

    return render_template('taskboard.html', tasks=tasks)

'''
Routes.py build on the files forms.py and their html templates. 
The forms are imported and this code specifies what is a valid input for the forms. 
This also includes where the user can navigate from each form. 
'''

# @app.route('/done/<int:task_id>')
# @login_required
# def complete(task_id):
#     task = Task.query.get(task_id)
#     user = current_user
#     if not task:
#         return redirect('/')
#     if task.done:
#         task.done = False
#     else:
#         task.done = True

#     db.session.commit()
#     return redirect('/')
