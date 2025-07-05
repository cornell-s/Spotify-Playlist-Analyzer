
# app/playlist_analysis.py

import pandas as pd

def extract_track_data(sp, playlist_id):
    """
    Extract track-level audio features and metadata from a Spotify playlist.
    Returns a DataFrame with audio features and metadata like artist and track name.
    """
    tracks = sp.playlist_tracks(playlist_id)
    features_list = []
    track_names = []
    artist_names = []
    genres_list = []

    for item in tracks['items']:
        track = item['track']
        if track:
            name = track['name']
            track_id = track['id']
            artists = [artist['name'] for artist in track['artists']]
            artist_id = track['artists'][0]['id']

            audio_features = sp.audio_features([track_id])[0]
            if audio_features:
                audio_features['name'] = name
                audio_features['artist'] = ", ".join(artists)

                # Try to get genre from the first artist (may be missing)
                try:
                    artist_info = sp.artist(artist_id)
                    genres = artist_info.get('genres', [])
                    audio_features['genre'] = genres[0] if genres else "Unknown"
                except:
                    audio_features['genre'] = "Unknown"

                features_list.append(audio_features)

    return pd.DataFrame(features_list)

def get_top_genres(df, top_n=5):
    """
    Returns a Series of the top N genres in the playlist.
    """
    return df['genre'].value_counts().head(top_n)

def get_top_artists(df, top_n=5):
    """
    Returns a Series of the top N artists in the playlist.
    """
    return df['artist'].value_counts().head(top_n)
