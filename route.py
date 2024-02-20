from flask import render_template, redirect, flash, url_for, make_response
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash
from app import app, storage, bcrypt
from app.forms import LoginForm

@app.route('/auth/sign_in', methods=['GET', 'POST'], strict_slashes=False)
def sign_in():
    """Handle the sign_in route"""
    if current_user.is_authenticated:
        # Redirect user to their dashboard or another page
        flash('You are already signed in')
        return redirect(url_for('dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = storage.get(None, form.id.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Welcome {user.first_name}, You have been logged in', 'success')
            response = make_response(redirect(url_for('dashboard')))
            response.headers['Cache-Control'] = (
                'no-cache, no-store, must-revalidate')
            return response
        else:
            flash('Invalid ID or password', 'error')
            response = make_response(redirect(url_for('sign_in')))
            response.headers['Cache-Control'] = (
                'no-cache, no-store, must-revalidate')
            return response

    return render_template('login.html', form=form)
