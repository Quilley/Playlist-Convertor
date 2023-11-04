from flask import Flask, render_template, redirect, request, url_for
import requests

app = Flask(__name)

# Replace with your Spotify Developer App credentials
SPOTIFY_CLIENT_ID = 'e49780644eba43679b85ffb0e5d09ee4'
SPOTIFY_CLIENT_SECRET = '03e38a698f37464ea0a3ff6c51aa2876'
SPOTIFY_REDIRECT_URI = 'http://localhost:5000/callback'

# Spotify API authorization URL
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

@app.route('/')
def index():
    # Construct the Spotify login URL
    login_url = f"{SPOTIFY_AUTH_URL}?client_id={SPOTIFY_CLIENT_ID}&redirect_uri={SPOTIFY_REDIRECT_URI}&response_type=code&scope=user-read-private%20user-read-email"
    return render_template('index.html', login_url=login_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': SPOTIFY_REDIRECT_URI,
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    }

    # Request the access token
    response = requests.post(SPOTIFY_TOKEN_URL, data=data)
    access_token = response.json().get('access_token')

    # You can now use the access_token to make Spotify API requests on behalf of the user

    return f'Access Token: {access_token}'

if __name__ == '__main__':
    app.run(debug=True)
