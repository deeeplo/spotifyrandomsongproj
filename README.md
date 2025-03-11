# Spotify Random Song Picker

A web application that randomly selects a song from your Spotify playlists and liked songs. When a song is selected, you can click on it to search for it directly on Spotify.

## Features

- 🎵 Randomly selects songs from your Spotify playlists and liked songs
- 🎨 Modern, responsive UI with Spotify-themed design
- 🔍 Clickable results that open Spotify search
- 🔄 Loading animation while fetching songs
- 🐳 Docker support for easy deployment

## Prerequisites

Before running the application, you'll need:

1. A Spotify Developer Account
2. Spotify API credentials (Client ID and Client Secret)
3. Docker (if running with Docker) OR Python 3.9+ (if running locally)

## Setup

### 1. Spotify API Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new application
3. Get your Client ID and Client Secret
4. Add `http://localhost:3000` to your Redirect URIs in the app settings

### 2. Environment Variables

Create a `.env` file in the project root with your Spotify credentials:

```
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
```

## Running the Application

### Option 1: Using Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t spotify-random-song .
```

2. Run the container:
```bash
docker run -p 5000:5000 --env-file .env spotify-random-song
```

3. Open your browser and go to `http://localhost:5000`

### Option 2: Running Locally

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to `http://localhost:5000`

## Usage

1. When you first access the application, you'll need to authenticate with your Spotify account
2. Click the "Get Random Song" button to select a random song
3. Click on the displayed song to search for it on Spotify
4. Repeat as many times as you like!

## Troubleshooting

- If you see an authentication error, make sure your Spotify API credentials are correct in the `.env` file
- If the application can't access your playlists, ensure you've granted the necessary permissions during the Spotify authentication
- If running with Docker, make sure ports are properly mapped and the `.env` file is being properly read

## License

This project is licensed under the MIT License - see the LICENSE file for details. 