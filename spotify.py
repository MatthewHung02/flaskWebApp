import requests
import json
import os

#f = open('C:\\Users\\user\\Documents\\spotifycheckersecrets.txt')
#data = json.load(f)
seatgeekid = os.environ.get('sgid')
seatgeeksecret = os.environ.get('sgsecret')
spotifyid = os.environ.get('spotifyid')
spotifysecrets = os.environ.get('spotifysecret')

baseeventURL = "https://api.seatgeek.com/2/events?performers.slug={0}&client_id={1}&client_secret={2}"
url = baseeventURL.format("yoke-lore", seatgeekid, seatgeeksecret)
print(url)
response = requests.get(url)

spotifyresponsejson = response.content


'''
get top five artists from spotify
query the concerts from those artists and display the concerts in the same state
'''


