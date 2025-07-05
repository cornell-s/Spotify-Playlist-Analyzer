
# app/streamlit_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
from app.auth import create_spotify_client

st.title("🎧 Spotify Playlist Analyzer")

# Create Spotify client
sp = create_spotify_client()

# Get current user's playlists
playlists = sp.current_user_playlists(limit=10)
playlist_options = {pl["name"]: pl["id"] for pl in playlists["items"]}
playlist_name = st.selectbox("Choose a playlist", list(playlist_options.keys()))

if playlist_name:
    tracks = sp.playlist_tracks(playlist_options[playlist_name])
    features_list = []
    track_names = []

    for item in tracks['items']:
        track = item['track']
        if track:  # Check if track is not None
            name = track['name']
            track_id = track['id']
            audio_features = sp.audio_features([track_id])[0]
            if audio_features:
                features_list.append(audio_features)
                track_names.append(name)

    df = pd.DataFrame(features_list)
    df["name"] = track_names

    st.subheader("Danceability of Songs")
    fig = px.bar(df, x="name", y="danceability")
    st.plotly_chart(fig)

    st.subheader("Energy vs. Valence")
    fig2 = px.scatter(df, x="energy", y="valence", hover_name="name")
    st.plotly_chart(fig2)
