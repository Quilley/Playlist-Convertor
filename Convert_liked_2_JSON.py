import requests
import json

# Replace with your Spotify API credentials
client_id = "e49780644eba43679b85ffb0e5d09ee4"
client_secret = "03e38a698f37464ea0a3ff6c51aa2876"
access_token = "your_access_token"  # Obtain this using the Spotify API authentication

# Make a GET request to retrieve liked songs
url = "https://api.spotify.com/v1/me/tracks"
headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    liked_songs = response.json()
    with open("liked_songs.json", "w", encoding="utf-8") as json_file:
        json.dump(liked_songs, json_file, ensure_ascii=False, indent=4)
    print("Liked songs saved to liked_songs.json")
else:
    print(f"Failed to retrieve liked songs. Status code: {response.status_code}")
