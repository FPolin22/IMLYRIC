

import requests
import json
from lyrics_api import *


def return_lyrics(song,response=""):
    artist= input("Please enter the name of the artist of the song ->")
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist + track_search_parameter + song + api_key
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    print("API Call: " + api_call)
    print()
    print(data['lyrics']['lyrics_body'])
    
    
                  
