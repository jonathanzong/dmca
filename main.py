import twitter_api_keys
import tweepy
from app.forms import SurveyForm
import json
import os

from flask import Flask, session, request, redirect, url_for, render_template

from utils.common import DbEngine
from app.models import *

app = Flask(__name__)
app.secret_key = 'such secret very key!' # session key

consumer_key = twitter_api_keys.TWITTER_CONSUMER_KEY
consumer_secret = twitter_api_keys.TWITTER_CONSUMER_SECRET

ENV = os.environ['CS_ENV'] = "development" # TODO

CONFIG_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config")
db_session = DbEngine(CONFIG_DIR + "/{env}.json".format(env=ENV)).new_session()

def is_logged_in():
  return 'user' in session

@app.route('/')
def index():
  if is_logged_in():
    return redirect(url_for('debrief'))
  return render_template('index.html')

@app.route('/debrief', methods=('GET', 'POST'))
def debrief():
  if not is_logged_in():
    return redirect(url_for('index'))
  user = session['user']
  # TODO: if user has filled out survey, redirect to /complete

  # TODO: look up conditions for user by user['id'],
  #       conditionally render template

  # handle form submission
  form = SurveyForm()
  if form.validate_on_submit():
    results_dict = request.form.to_dict()
    del results_dict['csrf_token']
    results_dict['twitter_user_id'] = user['id']

    res = TwitterUserSurveyResult(twitter_user_id=user['id'],
                                  survey_data=json.dumps(results_dict).encode('utf-8'))
    db_session.add(res)
    db_session.commit()
    return redirect('/complete')
  return render_template('debrief.html', user=user, form=form)

@app.route('/complete')
def complete():
  if not is_logged_in():
    return redirect(url_for('index'))
  return render_template('complete.html')

@app.route('/login')
def login():
  callback_url = url_for('oauth_authorized', _external=True)
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)
  try:
    redirect_url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
    return redirect(redirect_url)
  except tweepy.TweepError:
    return 'Error! Failed to get request token.'

@app.route('/logout')
def logout():
  del session['user']
  return redirect(url_for('index'))

@app.route('/oauth_authorized')
def oauth_authorized():
  verifier = request.args.get('oauth_verifier')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  token = session['request_token']
  del session['request_token']
  auth.request_token = token

  try:
    auth.get_access_token(verifier)
    api = tweepy.API(auth)
    user = api.me()

    # TODO: store access_token?
    session['user'] = {'id': user.id, 'screen_name': user.screen_name}

    return redirect(url_for('debrief'))
  except tweepy.TweepError:
    return 'Error! Failed to get access token.'
