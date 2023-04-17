from flask import Flask, render_template, request, redirect, url_for, session
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0
from config import Config
import os


app = Flask(__name__)
app.config.from_object(Config)
#app.secret_key = os.environ.get("FLASK_SECRET_KEY")

auth0_domain = os.environ.get("AUTH0_DOMAIN")
auth0_client_id = os.environ.get("AUTH0_CLIENT_ID")
auth0_client_secret = os.environ.get("AUTH0_CLIENT_SECRET")
auth0_audience = f"https://{auth0_domain}/api/v2/"

get_token = GetToken(auth0_domain)
token = get_token.client_credentials(auth0_client_id,
                                     auth0_client_secret,
                                     auth0_audience)
mgmt_api_token = token["access_token"]

auth0 = Auth0(auth0_domain, mgmt_api_token)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        auth0.passwordless_start(
            client_id=auth0_client_id,
            connection='email',
            email=email,
            send='link',
            auth_params={
                'scope': 'openid email'
            }
        )
        session['email'] = email
        return redirect(url_for('verify'))
    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        email = session.get('email')
        verification_code = request.form['verification_code']
        response = auth0.passwordless_login(
            client_id=auth0_client_id,
            connection='email',
            email=email,
            verification_code=verification_code,
            scope='openid email'
        )
        session['token'] = response['id_token']
        return redirect(url_for('profile'))
    return render_template('verify.html')

@app.route('/profile')
def profile():
    token = session.get('token')
    user_info = auth0.tokeninfo(token)
    return render_template('profile.html', user_info=user_info)

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/logout')
def logout():
    session.clear()
    params = {'returnTo': url_for('home', _external=True), 'client_id': auth0_client_id}
    return redirect(auth0.api_client.authorize_url(**params))
