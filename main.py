import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

# Replace these with your Spotify API credentials
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''

# Authentication - without user login
auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_mood_input():
    moods = [
    'happy',
    'sad',
    'energetic',
    'calm',
    'focused',
    'romantic',
    'angry',
    'melancholic',
    'confident',
    'nostalgic',
    'chill',
    'inspired',
    'reflective',
    'lonely',
    'motivated',
    'playful',
    'anxious',
    'hopeful',
    'adventurous',
    'tired',
    'excited',
    'grateful',
    'rebellious',
    'curious',
    'optimistic',
    'celebratory',
    'heartbroken',
    'frustrated',
    'mysterious',
    'serene',
    'free-spirited',
    'silly',
    'disoriented'
]

    print("What mood are you in? Choose from the following:")
    i=0
    for _mood in moods:
        i+=1
        print(i, _mood)

    mood = input("Enter your mood: ").lower()
    # print(mood)

    try:
        if mood in moods:
            return mood
        
        if mood.isdigit():
            mood_index = int(mood)
            mood = moods[mood_index - 1]

            return mood
    except Exception as err:

        print('Please choose the right number or type the mood.', err)
        # return get_mood_input()

# This function will connect to the Spotify API and get a playlist based on the mood.
def get_playlist_for_mood(mood):
    # Map moods to Spotify categories (you can customize this)

    mood_to_genre = {
    'happy': 'pop',  # Upbeat, cheerful tunes with catchy rhythms
    'sad': 'acoustic',  # Stripped-back acoustic sounds for emotional reflection
    'energetic': 'electronic',  # High-energy, fast-paced beats like EDM or dance
    'calm': 'ambient',  # Soothing, atmospheric music to relax
    'focused': 'classical',  # Complex but non-intrusive music for concentration
    'romantic': 'r&b',  # Smooth, soulful melodies with emotional depth
    'angry': 'metal',  # Aggressive, loud, and intense music to channel emotions
    'melancholic': 'indie',  # Thought-provoking, often introspective alternative sounds
    'confident': 'hip-hop',  # Strong beats and lyrics to boost self-confidence
    'nostalgic': 'retro',  # Throwback tunes from earlier decades, e.g., 80s or 90s
    'chill': 'lo-fi',  # Relaxed, downtempo beats often used for background music
    'inspired': 'indie folk',  # Acoustic-driven with storytelling and emotional depth
    'reflective': 'jazz',  # Smooth, improvisational tunes for introspective moments
    'lonely': 'blues',  # Deep, emotional music reflecting solitude and longing
    'motivated': 'rock',  # Strong, driving rhythms for inspiration and motivation
    'playful': 'funk',  # Groovy, lively tunes that are upbeat and fun
    'anxious': 'trip-hop',  # A mix of electronic and hip-hop, often dark and moody
    'hopeful': 'gospel',  # Uplifting, often spiritual music
    'adventurous': 'world',  # Eclectic sounds from different cultures and countries
    'tired': 'downtempo',  # Slower, mellow electronic music for unwinding
    'excited': 'dance',  # High-energy, rhythmic music to boost excitement
    'lonely': 'country',  # Ballads and storytelling tunes reflecting personal struggles
    'grateful': 'soul',  # Warm, rich melodies with emotional resonance
    'rebellious': 'punk',  # Raw, high-energy music with themes of defiance
    'curious': 'experimental',  # Unconventional, avant-garde music for exploration
    'optimistic': 'synthwave',  # Retro-futuristic electronic music with hopeful vibes
    'celebratory': 'latin',  # Rhythmic, upbeat Latin music perfect for celebrations
    'heartbroken': 'folk',  # Emotional and narrative-driven acoustic music
    'frustrated': 'industrial',  # Harsh, mechanical sounds to express anger or frustration
    'mysterious': 'psychedelic',  # Trippy, mind-bending sounds for deep contemplation
    'serene': 'new age',  # Calming, meditative music for peace and serenity
    'free-spirited': 'reggae',  # Laid-back, carefree tunes with rhythmic grooves
    'silly': 'electro swing',  # Fun, upbeat tunes combining vintage swing with modern beats
    'disoriented': 'drone',  # Slow, evolving soundscapes that create a hypnotic atmosphere
}


    genre = mood_to_genre.get(mood, 'pop')

    # Search for playlists related to the genre
    playlists = sp.search(q=f'genre:{genre}', type='playlist', limit=7)
    return playlists['playlists']['items']

if __name__ == "__main__":
    mood = get_mood_input()
    playlists = get_playlist_for_mood(mood)
    
    print(f"Here are some playlists for your {mood} mood:\n")
    for idx, playlist in enumerate(playlists):
        print(f"{idx+1}. {playlist['name']} - {playlist['external_urls']['spotify']}")
