import argparse
import json
import requests, re, operator
from lyrics_finder import return_lyrics
from lyrics_api import *

headers = {
    'x-rapidapi-host': "ENTER WORDS API HOST URL",
    'x-rapidapi-key': "ENTER API KEY FOR WORDS API"
    }


parser = argparse.ArgumentParser(
        description="Retrieve lyrics information for a given song",
        prog="IMLYRIC",
        epilog="Powered by Musixmatch and Spotify")

parser.add_argument("song_name",
                    help="input the name of a known cocktail")

parser.add_argument("--album", help="name of the album")
parser.add_argument("--artist", help="name of the artist")
parser.add_argument("--song", help="title of the song")
parser.add_argument('--verbose', '-v', action='store_true', help="show additional logs")
parser.add_argument("--version", action="version", version="IMLYRIC 1.0")

parser.add_argument("-l", "--lyric", action="store_true",
                   help="get song lyrics")
args = parser.parse_args()
song = args.song_name

def throw_console_errors(message):
    """Show arguments' errors"""
    return argparse.ArgumentParser().error(message)


#------------------------------------------


if args.lyric:
    return_lyrics(song)

    

#PROVA PUSH
