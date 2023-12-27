import requests
import json

f = open('C:\\Users\\user\\Documents\\spotifycheckersecrets.txt')
data = json.load(f)
seatgeekid = data['sgid']
seatgeeksecret = data['sgsecret']
spotifyid = data['spotifyid']
spotifysecrets = data['spotifysecret']

baseeventURL = "https://api.seatgeek.com/2/events?performers.slug={0}&client_id={1}&client_secret={2}"
url = baseeventURL.format("yoke-lore", seatgeekid, seatgeeksecret)
print(url)
response = requests.get(url)

spotifyresponsejson = response.content


'''
get top five artists from spotify
query the concerts from those artists and display the concerts in the same state
'''


