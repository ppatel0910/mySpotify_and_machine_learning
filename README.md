![picture_of_spotify_logo](https://github.com/ppatel0910/mySpotify_and_machine_learning/blob/main/images/Spotify-Generic-Header-1440x820-1.png)

## Background

#### Spotify is a leading digital platform for streaming music, podcasts, and playlists, offering users a vast selection of audio content. Accessible through its app or website, Spotify allows listeners to enjoy on-demand music, curate personalized playlists, and explore new artists and genres. With both free and premium subscription tiers, Spotify has become a go-to destination for music lovers globally. (and personally myself)

#### As a daily user of Spotify, I can attest that the song/tracks recommended are not up to par. So naturally, I sought out a way to recommend myself better songs. Within this notebook, I will use the Spotify Web API to extract songs and features from my own playlists to produce new song recommendations for myself.

#### To use the Spotify API, users should start with the Spotify API documentation, link below
[Spotify_web_api_documentation](https://developer.spotify.com/documentation/web-api)

## General Process

#### I connected to the Spotify web API using the instructions provided from the link above, and was granted a client ID, and a client secret key. With these credentials, I requested an access token and was successfully able to make calls to the Spotify web API. I then made calls to the Spotify API to retrieve data such as music features and my personal Spotify playlists. Using these input features, I was able to use the spotipy API to recommend new songs to myself. Users can adapt this code to their own Spotify accounts upon creation of their own developer credentials. 

## Results