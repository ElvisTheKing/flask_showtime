from flask import Flask, redirect, url_for, session, request
from flask_oauthlib.client import OAuth, OAuthException
from flask.ext.login import login_user,logout_user,login_required,current_user
from showtime import app,login_manager,db
from showtime.models import User

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

oauth = OAuth(app)

facebook = oauth.remote_app(
    'facebook',
    consumer_key=app.config.get("FACEBOOK_APP_ID"),
    consumer_secret=app.config.get("FACEBOOK_APP_SECRET"),
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth'
)

@app.route('/login')
def login():
    if not current_user.is_anonymous():
        return redirect('/')

    callback = url_for(
        'facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True
    )
    return facebook.authorize(callback=callback)

@app.route('/debug_login')
def debug_login():
    if app.debug:
        login_user(User.query.first(),True)
        return redirect('/')
    else:
        abort(404)


@app.route('/login/authorized')
def facebook_authorized():
    resp = facebook.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: %s' % resp.message

    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')

    user = User.query.filter(User.remote_id == me.data['id']).first()
    if not user:
        user = User(remote_id=me.data['id'])

    user.email = me.data['email']
    db.session.add(user)
    db.session.commit()

    login_user(user,True)

    return redirect('/')


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')