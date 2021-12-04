import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotify_secrets import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from input import playlist_name, playlist_description, is_playlist_public, track_limit, offset

SPOTIFY_SCOPE = "user-library-read, playlist-read-private, playlist-read-collaborative, playlist-modify-private, playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, 
                                                client_secret=SPOTIFY_CLIENT_SECRET,
                                                redirect_uri=SPOTIFY_REDIRECT_URI,
                                                scope=SPOTIFY_SCOPE))
# gets user id
user_id = sp.me()['id']

# gets playlist id
playlist_id = sp.user_playlist_create(user_id, playlist_name, public=is_playlist_public, description=playlist_description)["id"]

# finds all the items in the current user's library
library = sp.current_user_saved_tracks(limit=track_limit, offset=offset)

# gets track_id from library tracks
track_id = []
for item in library['items']:
    if not item['track']:
        continue
    track_id.append(item['track']['id'])

# adds tracks into the newly created playlist
sp.user_playlist_add_tracks(user_id, playlist_id, track_id);



    

