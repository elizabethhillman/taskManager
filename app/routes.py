from app import db
from app import app
from flask import render_template, flash, redirect
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from app.forms import LoginForm, SignupForm, ChangePasswordForm
from app.models import User, Post



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
            flash('Invalid username or password')
            return redirect('/login')
        # let flask_login library know what user logged int
        # it also means that their password was correct
        login_user(user)
         # return to page before user got asked to login
        # for example, if user tried to access a wedpage called profile, but since they
        # weren't logged in they would get redirected to login page. After they log in
        # the user will be redirected to their previous request, which would be the profile
        # page in this case.
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

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
            newuser = User(username=form.username.data, email=form.email.data, password = form.password.data)
            db.session.add(newuser)
            db.session.commit()
        else:
            return f'''<html><body>
                        {form.username.data} already exixt
                        <a href="">Login</a>
                        </body>
                        </html>'''
    return render_template('signup.html', title='Sign up', form=form)

@app.route('/changepassword', methods = ['GET', 'POST'])
def changepassword():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = current_user
        oldpassword = User.query.filter_by(password = form.oldpassword.data).first()
        if oldpassword is None or not oldpassword.check_password(form.oldpassword.data):
            flash('Wrong password')
            return redirect('/changepassword')
        else:
            user.password = user.set_password(form.newpassword.data)
            db.session.add(user)
            db.session.commit()
            flash('Successful Change Password')
            return redirect('/changepassword')
    return render_template('changepassword.html', title = 'Change password', form=form)