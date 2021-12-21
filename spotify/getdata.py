################################################################################
###################### code for working with spotify api, using spotipy

import json
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import time

client_id = "CLIENT_ID"  # insert your client id
client_secret = "CLIENT_SECRET"  # insert your client secret id here

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlist_id = ""  # insert your playlist id
# results = sp.playlist(playlist_id)


def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist["tracks"]["items"]:
        track = item["track"]
        ids.append(track["id"])
    return ids


def getTrackFeatures(id):
    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta["name"]
    album = meta["album"]["name"]
    artist = meta["album"]["artists"][0]["name"]
    release_date = meta["album"]["release_date"]
    length = meta["duration_ms"]
    popularity = meta["popularity"]

    # features
    acousticness = features[0]["acousticness"]
    danceability = features[0]["danceability"]
    energy = features[0]["energy"]
    instrumentalness = features[0]["instrumentalness"]
    liveness = features[0]["liveness"]
    loudness = features[0]["loudness"]
    speechiness = features[0]["speechiness"]
    tempo = features[0]["tempo"]
    time_signature = features[0]["time_signature"]

    track = [
        name,
        album,
        artist,
        release_date,
        length,
        popularity,
        danceability,
        acousticness,
        danceability,
        energy,
        instrumentalness,
        liveness,
        loudness,
        speechiness,
        tempo,
        time_signature,
    ]
    return track


ids = getTrackIDs("angelicadietzel", "4R0BZVh27NUJhHGLNitU08")

tracks = []
for i in range(len(ids)):
    time.sleep(0.5)
    track = getTrackFeatures(ids[i])
    tracks.append(track)

# create dataset
df = pd.DataFrame(
    tracks,
    columns=[
        "name",
        "album",
        "artist",
        "release_date",
        "length",
        "popularity",
        "acousticness",
        "danceability",
        "energy",
        "instrumentalness",
        "liveness",
        "loudness",
        "speechiness",
        "tempo",
        "time_signature",
    ],
)

df.to_csv("spotify.csv", sep=",")
