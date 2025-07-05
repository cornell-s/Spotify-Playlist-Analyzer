
# 🎧 Spotify Playlist Analyzer

The **Spotify Playlist Analyzer** is an interactive web app that allows users to analyze the musical characteristics of their Spotify playlists. Using the Spotify Web API and audio features such as danceability, energy, and valence, this tool provides insightful visualizations that help users understand the mood, genre trends, and artist composition of their music.

---

## 🔍 Features

- 🔐 **Spotify OAuth Login** – Securely connect with your Spotify account
- 🎵 **Playlist Selection** – Choose from your own playlists
- 📊 **Visual Analytics**:
  - Bar chart of song **danceability**
  - Scatterplot of **energy vs. valence**
  - (Coming soon) Top genres and artists pie chart
- 💡 **(Optional)** Mood-based song recommendations

---

## 🧰 Tech Stack

- **Python** – Core language
- **Streamlit** – Interactive frontend UI
- **Spotipy** – Python wrapper for Spotify Web API
- **Plotly** – Interactive and attractive charts
- **dotenv** – Secure management of API keys

---

## 🚀 Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/spotify-playlist-analyzer.git
   cd spotify-playlist-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root directory and add your Spotify Developer credentials:
   ```env
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
   ```

   - Get these by registering an app at: [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)

4. **Run the app**
   ```bash
   streamlit run app/streamlit_app.py
   ```

---

## 📸 Screenshots

*(You can add images of the UI here after deployment or local testing)*

---

## 🧠 Learning Outcomes

This project demonstrates:
- API integration using OAuth2
- Real-time data collection and analysis
- Data visualization with Plotly
- Frontend UI development using Streamlit
- Environment variable security with `.env`

---

## 📌 Future Improvements

- Add top artist and genre pie charts
- Recommend similar songs based on playlist mood
- Deploy via [Streamlit Cloud](https://streamlit.io/cloud) or [Render](https://render.com)
- Add support for exporting stats to CSV or PDF

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for improvements or new features.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🎓 Acknowledgments

- [Spotify for Developers](https://developer.spotify.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly](https://plotly.com/python/)
