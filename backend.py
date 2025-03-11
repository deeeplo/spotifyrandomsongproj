import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import os
from dotenv import load_dotenv

load_dotenv()

# Your Spotify API credentials
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = 'http://localhost:3000'

# Scopes needed
scope = 'playlist-read-private,playlist-read-collaborative,user-library-read'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))
# Function to get all tracks from playlists
def get_playlist_tracks(sp):
    playlists = sp.current_user_playlists()
    tracks = []
    while playlists:
        for playlist in playlists['items']:
            results = sp.playlist_tracks(playlist['id'])
            tracks.extend([(item['track']['name'], item['track']['artists'][0]['name']) for item in results['items']])
            if results['next']:
                results = sp.next(results)
                tracks.extend([(item['track']['name'], item['track']['artists'][0]['name']) for item in results['items']])
            else:
                break
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            break
    return tracks

# Function to get liked songs
def get_liked_songs(sp):
    results = sp.current_user_saved_tracks()
    liked_songs = [(item['track']['name'], item['track']['artists'][0]['name']) for item in results['items']]
    while results['next']:
        results = sp.next(results)
        liked_songs.extend([(item['track']['name'], item['track']['artists'][0]['name']) for item in results['items']])
    return liked_songs

# Combine all tracks
all_tracks = get_playlist_tracks(sp) + get_liked_songs(sp)

# Randomly select a song
random_song = random.choice(all_tracks)

print(f"Randomly selected song: {random_song[0]} by {random_song[1]}")