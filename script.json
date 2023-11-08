// Replace with your Spotify API credentials
const clientID = 'e49780644eba43679b85ffb0e5d09ee4';
const redirectURI = '03e38a698f37464ea0a3ff6c51aa2876';

const loginWithSpotify = () => {
    const scope = 'user-library-read';
    const spotifyAuthURL = `https://accounts.spotify.com/authorize?client_id=${clientID}&response_type=token&redirect_uri=${redirectURI}&scope=${scope}`;
    window.location = spotifyAuthURL;
};

const getLikedSongs = () => {
    const accessToken = window.location.hash.substr(1).split('&')[0].split('=')[1];
    const likedSongsURL = 'https://api.spotify.com/v1/me/tracks';

    fetch(likedSongsURL, {
        headers: {
            'Authorization': `Bearer ${accessToken}`
        }
    })
    .then(response => response.json())
    .then(data => {
        const likedSongsList = document.getElementById('liked-songs');
        data.items.forEach(song => {
            const listItem = document.createElement('li');
            listItem.textContent = song.track.name;
            likedSongsList.appendChild(listItem);
        });
        document.getElementById('login-button').style.display = 'none';
        document.getElementById('songs-container').style.display = 'block';
    })
    .catch(error => console.error(error));
};

if (window.location.hash) {
    getLikedSongs();
}
