import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Replace these with your Spotify API credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'

# Authentication - without user login
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_mood_input():
    moods = ['happy', 'sad', 'energetic', 'calm', 'focused']
    print("What mood are you in? Choose from the following:")
    print(", ".join(moods))
    mood = input("Enter your mood: ").lower()

    if mood not in moods:
        print("Invalid mood. Please choose a valid one.")
        return get_mood_input()

    return mood

# This function will connect to the Spotify API and get a playlist based on the mood.
def get_playlist_for_mood(mood):
    # Map moods to Spotify categories (you can customize this)
    mood_to_genre = {
        'happy': 'pop',
        'sad': 'acoustic',
        'energetic': 'workout',
        'calm': 'chill',
        'focused': 'focus'
    }

    genre = mood_to_genre.get(mood, 'pop')

    # Search for playlists related to the genre
    playlists = sp.search(q=f'genre:{genre}', type='playlist', limit=5)
    return playlists['playlists']['items']

if __name__ == "__main__":
    mood = get_mood_input()
    playlists = get_playlist_for_mood(mood)
    
    print(f"Here are some playlists for your {mood} mood:\n")
    for idx, playlist in enumerate(playlists):
        print(f"{idx+1}. {playlist['name']} - {playlist['external_urls']['spotify']}")
