from flask import Blueprint, render_template, redirect, request, session, jsonify
from datetime import datetime, timedelta
import urllib.parse
import json
import requests
import os


token_url = "https://accounts.spotify.com/api/token"
base_url = "https://api.spotify.com/v1/"

#os.env uses vercel's enviroment variables
seatgeekid = os.environ.get('sgid')
seatgeeksecret = os.environ.get('sgsecret')
spotifyid = os.environ.get('spotifyid')
spotifysecrets = os.environ.get('spotifysecret')

baseeventURL = "https://api.seatgeek.com/2/events?performers.slug={0}&client_id={1}&client_secret={2}&per_page=100"



scope = "user-top-read user-follow-read"
type = "artists"
term = "medium_term"



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
    if datetime.now().timestamp > float(session['expires_at']):
       return "Sorry, log back in"


#render_template("spotifychecker.html")

@views.route("/login")
def login():
    paramaters = {
       'client_id':spotifyid,  
       #'type': type,
       #'time_range': term,
       'show_dialog':True,
       'redirect_uri': 'https://www.matthew-hung.com/callback',
       'response_type' : 'code',
       'scope' : scope
     }
    
    auth_url2 = f"https://accounts.spotify.com/authorize?{urllib.parse.urlencode(paramaters)}"
    #return redirect(auth_url2)
    return redirect(auth_url2)

@views.route("/callback")
def callback():
   #redirect url set in spotify dev
   redirect_url = "https://www.matthew-hung.com/callback"
   if 'error' in request.args:
      return jsonify({'error':request.args['error']})
   if 'code' in request.args:
      request_body = {
         'code' : request.args['code'],
         'grant_type' : 'authorization_code',
         'redirect_uri' : redirect_url,
         'client_id' : spotifyid,
         'client_secret': spotifysecrets
      }

      response = requests.post(token_url, data=request_body)
      tokeninfo = response.json()

      session['access_token'] = tokeninfo['access_token']
      session['refresh_token'] = tokeninfo['refresh_token']
      session['expires_at'] = datetime.now().timestamp() + tokeninfo['expires_in']
      return redirect('/charts')
   
@views.route("/charts")
def charts():
   
   if 'access_token' not in session:
      return redirect('/login')
   if datetime.now().timestamp() > float(session['expires_at']):
      return redirect('/login')
      
   headers = {'Authorization' : f"'Bearer {session['access_token']}'"}
   response = requests.get(base_url + "me/top/artists", headers=headers)
   
   spotifyjson = response.json()

   
   listylist = []
   for doc in spotifyjson['items']:
      listylist.append(doc['name'])
   
   fulllist = {'data' : []}
   for each in listylist:
      url = baseeventURL.format(each, seatgeekid, seatgeeksecret)
      sg2response = requests.get(url)
      responsejson = sg2response.json()
      fulllist['data'].append(responsejson)
   return fulllist

@views.route("/spotifycharts")
def spotifycharts():
   return render_template("spotifychecker.html")
              
   




