![picture_of_spotify_logo](https://github.com/ppatel0910/mySpotify_and_machine_learning/blob/main/images/Spotify-Generic-Header-1440x820-1.png)

## Background

#### Spotify is a leading digital platform for streaming music, podcasts, and playlists. The service offers users a vast selection of audio content such as songs and podcasts. Accessible through its app or website, Spotify allows listeners to enjoy on-demand music, curate personalized playlists, explore 1000s of Spotify curated playlists, and more. With both free and premium subscription tiers, Spotify has become a go-to destination for music lovers globally. (and personally myself :stuck_out_tongue_closed_eyes:)

#### As a daily user of Spotify, I can attest that the song/tracks recommended are not up to par. So naturally, I sought out a way to recommend myself better songs. Within this repository, I will use the Spotify Web API, in conjunction with the lightweight Python library,Spotipy, to extract songs and music features from my own playlist. Using the extracted data I will produce new song recommendations for myself.

#### To use the Spotify API, users should start with the Spotify API documentation, link below:
[Spotify_web_api_documentation](https://developer.spotify.com/documentation/web-api)

#### Below is the link to the Spotipy documentation:
[Spotipy_documentation](https://spotipy.readthedocs.io/en/2.22.1/#examples)

## General Process

#### I connected to the Spotify web API using the instructions provided from the link above, and was granted a client ID, and a client secret key. With these credentials, I requested an access token and was successfully able to make calls to the Spotify web API. I then made calls to the Spotify API using the imported Python library, Spotipy, to retrieve data such as music features. I then compiled the extracted data into a pandas dataframe. There was not much data cleaning to be done, as I essentially collected the data myself. I created a graph showing which genres of music I like the most using the dataframe. Using this dataframe I was able to train a  mdel to recommend songs to myself 

## Results

#### This graph depicts the number of playlists in each category in the initial dataframe 'df' 

![number_of_playlists_in_each_category](https://github.com/ppatel0910/mySpotify_and_machine_learning/blob/main/images/initial_category_bar_graph.png)

#### Below shows the number of different playlists that were listened to based on the year. 

![number_of_playlists_listened_to_by_year_graph](https://github.com/ppatel0910/mySpotify_and_machine_learning/blob/main/images/playlists_based_on_year.png)

#### Visual of audio features of the track "I love it" by Lil Pump featuring Kanye West.

![visual_of_list_of_audio_features_of_a_song](https://github.com/ppatel0910/mySpotify_and_machine_learning/blob/main/images/example_of_track_audio_features.png)

#### The graph belows shows the hour of the day that I listened to my recently played songs. Based on my recent listening history, only two songs were listened to in the morning, and the rest were after 4pm. I listen to Spotify everyday, so this graph will constantly be changing when the code is run based on my current listening habits.  

![number_of_songs_played_based_on_hour](https://github.com/ppatel0910/mySpotify_and_machine_learning/blob/main/images/number_of_songsplayed-based-on-hour.png)


### Resources Used 


- [Spotify_documentation](https://developer.spotify.com/documentation/web-api)
- [Spotify_documentation](https://developer.spotify.com/documentation/web-api/tutorials/getting-started)
- [Spotify_documentation](https://developer.spotify.com/documentation/web-api/reference/get-recommendations)
- [Spotify_documentation](https://developer.spotify.com/documentation/web-api/concepts/scopes)
- [Youtube_spotify_web_api_tutoriaL](https://www.youtube.com/watch?v=oNyaiWgqKDI)
- [Spotify_web_api_tutoriaL_article](https://levelup.gitconnected.com/music-analysis-with-spotify-api-59c080734c6e)
- [Another_Spotify_web_api_tutoriaL_article](https://www.grace-dev.com/python-apis/python-spotify-api/)
- [Spotipy_documentation](https://spotipy.readthedocs.io/en/2.22.1/#features)
