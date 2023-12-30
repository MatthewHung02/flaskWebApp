from flask import Blueprint, render_template, redirect, request, session, jsonify
from datetime import datetime, timedelta
import urllib.parse
import json
import requests
import os


token_url = "https://accounts.spotify.com/api/token"
base_url = "https://api.spotify.com/v1/"


#f = open('C:\\Users\\user\\Documents\\spotifycheckersecrets.txt')
#data = json.load(f)
seatgeekid = os.environ.get('sgid')
seatgeeksecret = os.environ.get('sgsecret')
spotifyid = os.environ.get('spotifyid')
spotifysecrets = os.environ.get('spotifysecret')


scope = "user-top-read"
type = "artists"
term = "medium_term"
spotifyclientid = "499455d664a942e78b3cdaa4f47774a5"


views = Blueprint("veiws", __name__)

@views.route("/")
def base():
  return render_template("index.html")

@views.route("/index")
def index():
  return render_template("index.html")

@views.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@views.route("/spotifychecker")
def spotifychecker():
    if 'access_token' not in session:
       return redirect('/login')
    if datetime.now().timestamp > session['expires_at']:
       return "Sorry, log back in"
    
    headers = {
       'Authorization' : f"Bearer {session['access_token']}"
    }

    response = request.get(base_url + "me/top/artists", headers = headers)
    artists = response.json()
    return jsonify(artists)

#render_template("spotifychecker.html")

@views.route("/login")
def login():
    paramaters = {
       'client_id':spotifyclientid,  
       'type': type,
       'time_range': term,
       'show_dialog':True,
       'redirect_uri': 'https://www.matthew-hung.com/',
       'response_type' : 'code'
     }
    
    auth_url2 = f"https://accounts.spotify.com/authorize?{urllib.parse.urlencode(paramaters)}"
    return redirect(auth_url2)

@views.route("/callback")
def callback():
   redirect_url = "https://www.matthew-hung.com/"
   if 'error' in request.args:
      return jsonify({'error':request.args['error']})
   if 'code' in request.args:
      request_body = {
         'code' : request.args['code'],
         'grant_type' : 'authorization_code',
         'redirect_uri' : redirect_url,
         'client_id' : spotifyid,
         'client_secret': spotifysecrets,
         #'response_type' : 'code'

      }

      response = requests.post(token_url, data=request_body)
      tokeninfo = response.json()

      session['access_token'] = tokeninfo['access_token']
      session['refresh_token'] = tokeninfo['refresh_token']
      session['expires_at'] = datetime.now().timestamp + tokeninfo['refresh_token']

      return redirect('/spotifychecker')
   




