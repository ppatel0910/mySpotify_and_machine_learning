![picture_of_spotify_logo](https://github.com/ppatel0910/mySpotify_and_machine_learning/blob/main/images/Spotify-Generic-Header-1440x820-1.png)

## Background

#### Spotify is a leading digital platform for streaming music, podcasts, and playlists, offering users a vast selection of audio content. Accessible through its app or website, Spotify allows listeners to enjoy on-demand music, curate personalized playlists, and explore new artists and genres. With both free and premium subscription tiers, Spotify has become a go-to destination for music lovers globally. (and personally myself)

#### As a daily user of Spotify, I can attest that the song/tracks recommended are not up to par. So naturally, I sought out a way to recommend myself better songs. Within this repository, I will use the Spotify Web API, in conjunction with the lightweight Python library,Spotipy, to extract songs and music features from my own playlist. Using the extracted data I will produce new song recommendations for myself.

#### To use the Spotify API, users should start with the Spotify API documentation, link below:
[Spotify_web_api_documentation](https://developer.spotify.com/documentation/web-api)

#### Below is the link to the Spotipy documentation:
[Spotipy_documentation](https://spotipy.readthedocs.io/en/2.22.1/#examples)

## General Process

#### I connected to the Spotify web API using the instructions provided from the link above, and was granted a client ID, and a client secret key. With these credentials, I requested an access token and was successfully able to make calls to the Spotify web API. I then made calls to the Spotify API using the imported Python library, Spotipy, to retrieve data such as music features. I then compiled the extracted data into a pandas dataframe. There was not much data cleaning to be done, as I essentially collected the data myself. I created a graph showing which genres of music I like the most using the dataframe. Using this dataframe I was able to train a  mdel to recommend songs to myself 

# plot the audio features amongst the constructed dataframe to see what i typically like regarding music

## Results

### Resources Used 


- [Spotify_documentation](https://developer.spotify.com/documentation/web-api)
- [Spotify_documentation](https://developer.spotify.com/documentation/web-api/reference/get-recommendations)
- [Spotify_documentation](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- [Youtube_spotify_web_api_tutoriaL](https://www.youtube.com/watch?v=oNyaiWgqKDI)
- [Spotify_web_api_tutoriaL_article](https://levelup.gitconnected.com/music-analysis-with-spotify-api-59c080734c6e)