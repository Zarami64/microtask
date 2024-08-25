from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from authlib.integrations.flask_client import OAuth
from . import db, login_manager, create_app
from .models import User, Video
from .forms import RegistrationForm, LoginForm, ProfileForm
from werkzeug.utils import secure_filename
import os

app = create_app()
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    google_client = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google_client.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google_client = oauth.create_client('google')
    token = google_client.authorize_access_token()
    resp = google_client.get('userinfo')
    user_info = resp.json()
    user = User.query.filter_by(email=user_info['email']).first()
    if user is None:
        user = User(
            first_name=user_info['given_name'],
            last_name=user_info['family_name'],
            email=user_info['email'],
            google_id=user_info['sub']
        )
        db.session.add(user)
        db.session.commit()
    login_user(user)
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.phone = form.phone.data
        if form.profile_picture.data:
            picture_file = secure_filename(form.profile_picture.data.filename)
            form.profile_picture.data.save(os.path.join('app/static/profile_pics', picture_file))
            current_user.profile_picture = picture_file
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('profile.html', form=form, user=current_user)

@app.route('/admin/set_video', methods=['GET', 'POST'])
@login_required
def set_video():
    if current_user.email != 'admin@example.com':  # Replace with actual admin check
        return "Unauthorized", 403
    if request.method == 'POST':
        title = request.form['title']
        url = request.form['url']
        new_video = Video(title=title, url=url, user_id=current_user.id)
        db.session.add(new_video)
        db.session.commit()
        flash('Video set successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('set_video.html')

@app.route('/watch_video/<int:video_id>')
@login_required
def watch_video(video_id):
    video = Video.query.get_or_404(video_id)
    return render_template('watch_video.html', video=video)
