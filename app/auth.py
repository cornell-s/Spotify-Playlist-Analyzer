
# app/auth.py

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Define the scope for Spotify access
SCOPE = "playlist-read-private playlist-read-collaborative"

def create_spotify_client():
    """
    Creates and returns a Spotify client with OAuth authentication.
    """
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=SCOPE,
        cache_path=".cache"  # Optional: caches token locally
    ))
