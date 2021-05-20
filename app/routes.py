from app import db
from app import app
from app import mail
import datetime
from app import celery
from datetime import date, timedelta, datetime
from flask import render_template, flash, redirect, request, url_for
from flask_mail import Message
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, SignupForm, ChangePasswordForm, NewTask, EditTask, CreateCategory, Reminder, Addsubtask, Addcollaborator, AssignUser, AddEvent
from werkzeug.security import check_password_hash
from app.models import User, Post, Task, Category, Subtask, Event


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/taskboard',methods=['GET', 'POST'])
def taskboard():
    user = User.query.filter_by(username=current_user.username).first()
    tasks = Task.query.filter_by(user_id=user.id, collaborate_id = None).all()
    assign_tasks = Task.query.filter_by(assign_user=user.username).all()
    categories = Category.query.filter_by(user_id=user.id).all()
    subtask = Subtask.query.all()
    return render_template('taskboard.html', tasks=tasks, categories=categories, subtasks=subtask, assign_tasks=assign_tasks)

@app.route('/collaboratetaskboard',methods=['GET', 'POST'])
def collaboratetaskboard():
    user = User.query.filter_by(username=current_user.username).first()
    tasks = Task.query.filter_by(collaborate_id=user.collaborate).all()
    subtask = Subtask.query.all()
    return render_template('collaboratetask.html', tasks=tasks, subtasks=subtask)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()
        # if no user found or password for user incorrect
        # user.check_password() is a method in the User class
        if user is None or not user.check_password(form.password.data):
            flash('Invalided username or password')
            return redirect('/login')
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
    form.category.choices = [(c.id, c.category) for c in Category.query.all()]
    
    if form.validate_on_submit():
        task = Task(content=form.addtask.data, estimatehr=form.estimatehr.data, estimatemin=form.estimatemin.data, priority=form.priority.data, category_id=form.category.data, author=user)
        db.session.add(task)
        db.session.commit()
        print(task.user_id)
        return redirect('/taskboard')
    return render_template('addtask.html', title= 'Add task',form = form)
    
@app.route('/addcollaboratetask', methods = ['GET', 'POST'])
@login_required
def collaboratenewtask():
    user = User.query.filter_by(username=current_user.username).first()
    form = NewTask()
    form.category.choices = [(c.id, c.category) for c in Category.query.all()]
    
    if form.validate_on_submit():
        task = Task(content=form.addtask.data, estimatehr=form.estimatehr.data, estimatemin=form.estimatemin.data, priority=form.priority.data, category_id=form.category.data, collaborate_id=user.collaborate, author=user)
        db.session.add(task)
        db.session.commit()
        print(task.user_id)
        return redirect('/collaboratetaskboard')
    return render_template('collaborateaddtask.html', title= 'Add task',form = form)

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

@app.route('/priority', methods=['GET', 'POST'])
@login_required
def filter_priority():
    user = User.query.filter_by(username=current_user.username).first()
    tasks = Task.query.filter_by(user_id=user.id).order_by(Task.priority.asc())
    categories = Category.query.filter_by(user_id=user.id).all()
    assign_tasks = Task.query.filter_by(assign_user=user.username).order_by(Task.priority.asc())

    return render_template('taskboard.html', tasks=tasks, assign_tasks = assign_tasks, categories=categories)

@app.route('/collapriority', methods=['GET', 'POST'])
@login_required
def filter_priority_collaborate():
    user = User.query.filter_by(username=current_user.username).first()
    tasks = Task.query.filter_by(collaborate_id=user.collaborate).order_by(Task.priority.asc())
    categories = Category.query.filter_by(user_id=user.id).all()
    assign_tasks = Task.query.filter_by(assign_user=user.username).order_by(Task.priority.asc())

    return render_template('collaboratetask.html', tasks=tasks, assign_tasks = assign_tasks, categories=categories)

@app.route('/createcategory', methods = ['GET', 'POST'] )
@login_required
def createcategory():
    user = User.query.filter_by(username=current_user.username).first()
    form = CreateCategory()
    if form.validate_on_submit():
        category = Category(category=form.addcategory.data, author=user)
        db.session.add(category)
        db.session.commit()
        return redirect('/addtask')
    return render_template('addcategory.html', title= 'Add Category',form = form)

@app.route('/collaboratecreatecategory', methods = ['GET', 'POST'] )
@login_required
def collaboratecreatecategory():
    user = User.query.filter_by(username=current_user.username).first()
    form = CreateCategory()
    if form.validate_on_submit():
        category = Category(category=form.addcategory.data, author=user)
        db.session.add(category)
        db.session.commit()
        return redirect('/addcollaboratetask')
    return render_template('addcategory.html', title= 'Add Category',form = form)

@app.route("/category/<int:category_id>", methods=['GET', 'POST'])
@login_required
def category(category_id):
    user = User.query.filter_by(username=current_user.username).first()
    tasks = Task.query.filter_by(user_id=user.id, category_id=category_id).all()
    assign_tasks = Task.query.filter_by(assign_user=user.username).all()
    categories = Category.query.filter_by(user_id=user.id).all()
    return render_template('taskboard.html', tasks=tasks, assign_tasks= assign_tasks, categories=categories)


#@app.route('/assignuser', methods = ['GET','POST'])
#@login_required
#def assignuser():
    
#    return render_template('assignuser.html', title= 'Assign User',form = form)

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
@celery.task
def send_mail(info):
    with app.app_context():
        msg = Message("Ping!",
                        sender =('SITE' ,'testingemailforsite@gmail.com'),
                        recipients=[info['email']])
        msg.body = info['message']
        mail.send(msg)

@app.route('/reminder/<int:task_id>', methods = ['GET', 'POST'] )
@login_required
def reminder(task_id):
    form = Reminder()
    user = current_user
    if form.validate_on_submit():
        TimeOrDay = int(form.selectTime.data)
        
        startOrcomplete = int(form.startorcomplet.data)
        info = {}
        info['email'] = user.email
        if(startOrcomplete == 1):
            info['message'] = 'Hello, this is SITE and we like to remind you that you have a task need to Start'
        if(startOrcomplete == 2):
            info['message'] = 'Hello, this is SITE and we like to remind you that you have a task need to Complete'
        if(startOrcomplete == 3):
            info['message'] = 'Hello, this is SITE and we like to remind you that you have a task need to Start and Complete soon'
        
        if(TimeOrDay == 2):
            now = date.today()
            dateslect = form.date.data
            now = str(now)
            dateslect = str(dateslect)
            datetimeFormat = '%Y-%m-%d'
            diff = datetime.strptime(dateslect, datetimeFormat)- datetime.strptime(now, datetimeFormat)
            duration = diff.total_seconds()
            duration = float(duration)
        if(TimeOrDay == 1):
            datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
            now = str(datetime.now())
            now = datetime.strptime(now, datetimeFormat)
            dateslect = str(form.date.data)+" "+str(form.time.data)+"."+str(00)
            dateslect = datetime.strptime(dateslect, datetimeFormat)
            diff = dateslect - now
            duration =diff.total_seconds()
            duration = float(duration)
        print(duration)
        send_mail.apply_async(args=[info], countdown = duration)
        return redirect(url_for('taskboard'))
    return render_template('reminder.html', title = 'Set up reminder', form = form) 

@app.route('/addsubtask/<int:task_id>', methods=['GET','POST'])
@login_required
def newsubtask(task_id):
    form = Addsubtask()
    task = Task.query.get(task_id)
    if request.method == 'POST' :
        if form.validate_on_submit():
            subtasks = Subtask(subtask=form.addsubtask.data, task_id=task.id)   
            db.session.add(subtasks)
            db.session.commit()
        return redirect('/taskboard')
    return render_template('subtask.html', form=form)

@app.route('/addcollaborator', methods=['GET', 'POST'])
@login_required
def Collaborator():
    form = Addcollaborator()

    if form.validate_on_submit():
        currentuser = current_user
        user = User.query.filter_by(username=form.addcollaborator.data).first()
        current_user.collaborate= current_user.id
        user.collaborate=current_user.collaborate
        db.session.commit()
        return redirect('/collaboratetaskboard')
    return render_template('collaborate.html', form=form)  

@app.route('/assignuser/<int:task_id>', methods = ['GET','POST'])
@login_required
def assignuser(task_id):
    form = AssignUser()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.assignuser.data).first()
        task = Task.query.get(task_id)
        task.assign_user = user.username
        db.session.commit()
        return redirect('/collaboratetaskboard')
    return render_template('assignuser.html', form = form)

@app.route('/calendar', methods = ['GET','POST'])
@login_required
def calender():
    user = User.query.filter_by(username=current_user.username).first()
    form = AddEvent()
    if form.validate_on_submit():
        event = Event(title=form.addtitle.data, date=datetime.strptime(str(form.adddate.data),'%Y-%m-%d'), author=user)
        db.session.add(event)
        db.session.commit()
        print(event.user_id)
        return redirect('/calendar')
    events = Event.query.filter_by(user_id = user.id).all()
    print(events)
    listEvent = []
    for item in events:
        listEvent.append({
            'title': item.title,
            'date': item.date
        })
    return render_template('calendar.html', title = 'Calendar', posts=listEvent, form = form)