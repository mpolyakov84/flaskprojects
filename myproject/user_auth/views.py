from myproject import db, login_manager
from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required
from myproject.models import Users
from myproject.user_auth.forms import RegisterForm, LoginForm

blueprint_auth = Blueprint('auth', __name__, template_folder='templates/user_auth')


@blueprint_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('You are logged in.', 'success')

            next = request.args.get('next')

            if next == None or not next.startswith('/'):
                next = url_for('auth.welcome')

            return redirect(next)
    return render_template('login.html',form=form)


@blueprint_auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(form.username.data,
                     form.email.data,
                     form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are registered successfully.', 'success')

        return redirect(url_for("auth.login"))
    return render_template('register.html', form=form)


@blueprint_auth.route('/welcome')
@login_required
def welcome():
    return render_template('welcome_user.html')

@blueprint_auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'success')
    return redirect(url_for('index'))

