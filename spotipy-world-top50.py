import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import time
import pandas as pd

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

#ISO Country Codes from https://www.nationsonline.org/oneworld/country_code_list.htm#:~:text=The%20ISO%20country%20codes%20are,a%20country%20or%20a%20state.
playlists = ['37i9dQZEVXbMDoHDwVN2tF', '37i9dQZEVXbK8BKKMArIyl', '37i9dQZEVXbLrQBcXqUtaC', '37i9dQZEVXbMMy2roB9myp', '37i9dQZEVXbJPcfkRz0wJ0', '37i9dQZEVXbKNHh6NIXu36', '37i9dQZEVXbIYfjSLbWr4V', '37i9dQZEVXbJqfMFK4d691', '37i9dQZEVXbMXbN3EUUhlg', '37i9dQZEVXbNfM2w2mq1B8', '37i9dQZEVXbJNSeeHswcKB', '37i9dQZEVXbKj23U1GF4IR', '37i9dQZEVXbL0GavIqMTeb', '37i9dQZEVXbOa2lmxNORXQ', '37i9dQZEVXbNxXF4SkHj9F', '37i9dQZEVXbMZAjGMynsQX', '37i9dQZEVXbL3J0k32lWnN', '37i9dQZEVXbM4UZuIrvHvA', '37i9dQZEVXbJlM6nvL1nD1', '37i9dQZEVXbLn7RQmT5Xv2', '37i9dQZEVXbLxoIml4MYkT', '37i9dQZEVXbKIVTPX9a2Sb', '37i9dQZEVXbNFJfN1Vw8d9', '37i9dQZEVXbLRQDuF5jeBp', '37i9dQZEVXbLesry2Qw2xS', '37i9dQZEVXbNBz9cRCSFkY', '37i9dQZEVXbMxcczTSoGwZ', '37i9dQZEVXbIPWwFssbupI', '37i9dQZEVXbJqdarpmTJDL', '37i9dQZEVXbLy5tBFyQvd4', '37i9dQZEVXbJp9wcIM9Eo5', '37i9dQZEVXbLwpL8TjsxOG', '37i9dQZEVXbNHwMxAkvmF8', '37i9dQZEVXbLZ52XmnySJg', '37i9dQZEVXbObFQZ3JLcXt', '37i9dQZEVXbKM896FDX8L1', '37i9dQZEVXbKMzVsSGQ49S', '37i9dQZEVXbJ6IpvItkve3', '37i9dQZEVXbIQnj7RRhdSX', '37i9dQZEVXbKXQ4mDTEBXq', '37i9dQZEVXbM472oKPNKzS', '37i9dQZEVXbIP3c3fqVrJY', '37i9dQZEVXbKAbrMR8uuf7', '37i9dQZEVXbJWuzDrTxbKS', '37i9dQZEVXbMx56Rdq5lwc', '37i9dQZEVXbKCF6dqVpDkS', '37i9dQZEVXbKGcyg6TFGx6', '37i9dQZEVXbJlfUljuZExa', '37i9dQZEVXbJU9eQpX8gPT', '37i9dQZEVXbO3qyFxbkOE1', '37i9dQZEVXbISk8kxnzfCq', '37i9dQZEVXbKY7jLzlJ11V', '37i9dQZEVXbJvfa0Yxg7E7', '37i9dQZEVXbM8SIrkERIYl', '37i9dQZEVXbJkgIdfsJyTw', '37i9dQZEVXbKypXHVwk1f0', '37i9dQZEVXbNOUPGj7tW6T', '37i9dQZEVXbJfdy5b0KP7W', '37i9dQZEVXbN6itCcaL3Tt', '37i9dQZEVXbKyJS56d1pgi', '37i9dQZEVXbLnolsZ8PSNw', '37i9dQZEVXbNZbJ6TZelCq', '37i9dQZEVXbK4gjvS1FjPY', '37i9dQZEVXbMH2jvi6jvjk', '37i9dQZEVXbLoATJ81JYXz', '37i9dQZEVXbJiyhoAPEfMK', '37i9dQZEVXbMnz8KIWsvf9', '37i9dQZEVXbMnZEatlMSiu', '37i9dQZEVXbIVYVBNw9D5K', '37i9dQZEVXbKkidEfWYRuD', '37i9dQZEVXbMJJi3wgRbAy', '37i9dQZEVXbNLrliB10ZnX', '37i9dQZEVXbLdGSmz6xilI']#provar amb dues llistes, una per països i una per ids.
countries = ['Global', 'DEU', 'SAU', 'ARG', 'AUS', 'AUT', 'BLR', 'BOL', 'BRA', 'BGR', 'BEL', 'CAN', 'CHL', 'COL', 'KOR', 'CRI', 'DNK', 'ARE', 'ECU', 'EGY', 'SLV', 'SVK' , 'ESP', 'USA', 'EST', 'PHL', 'FIN', 'FRA', 'GRC', 'GTM', 'HND', 'HKG', 'HUN', 'IND', 'IDN', 'IRL', 'ISL', 'ISR', 'ITA', 'JPN', 'KAZ', 'CZE', 'DOM', 'LVA', 'LTU','NLD', 'LUX', 'MYS', 'MAR', 'MEX', 'NIC', 'NGA', 'NOR', 'NZL', 'PAK', 'PAN', 'PRY', 'PER', 'POL', 'PRT', 'GBR', 'ROU', 'SGP', 'ZAF', 'SWE', 'CHE', 'THA', 'TWN', 'TUR', 'UKR', 'URY', 'VEN', 'VNM']
weeknum = "2023W46"

for i in range (64,66):
  print(f"{i}, {countries[i]}")
  country = []
  week = []
  track_name = []
  artist_name = []
  album_name = []
  copyright = []
  publication_date = []
  available_markets = []
  popularity = []
  danceability = []
  acousticness = []
  duration = []
  energy = []
  instrumentalness = []
  key = []
  liveness = []
  loudness = []
  mode = []
  speechiness = []
  tempo = []
  time_signature = []
  valence = []

  playlist_data = sp.playlist(playlists[i])  # Get the playlist data
  list_tracks = playlist_data['tracks']['items']
  total_df = {}
  time.sleep(20.2) #Sleep to not saturate the API.


  for track in list_tracks:
    audio_features = sp.audio_features(track['track']['id'])
    song_features = {} #We create the dictionary for each song.
    time.sleep(5.2)

    if audio_features is None or audio_features[0] is None: #Let's make sure there isn't any None value.
      continue

    else:
      #Date
      week.append(weeknum)

      #Country
      country.append(countries[i])

      #Track Name
      track_name.append(track['track']['name'])

      #Artist name
      artist_name.append(track['track']['artists'][0]['name'])

      #Album Name
      album_name.append(track['track']['album']['name'])

      #Popularity
      popularity.append(track['track']['popularity'])

      #Publication Date
      publication_date.append(track['track']['album']['release_date'])

      #Available markets
      if 'available_markets' in track['track'] and track['track']['available_markets'] is not None and len(track['track']['available_markets']) > 0:
        available_markets.append(track['track']['available_markets'][0])
      else:
        available_markets.append("None")

      #Danceability
      danceability.append(audio_features[0]['danceability'])

      #Acousticness
      acousticness.append(audio_features[0]['acousticness'])

      #Duration
      duration.append(audio_features[0]['duration_ms'])

      #Energy
      energy.append(audio_features[0]['energy'])

      #Instrumentalness
      instrumentalness.append(audio_features[0]['instrumentalness'])

      #Key
      key.append(audio_features[0]['key'])

      #Liveness
      liveness.append(audio_features[0]['liveness'])

      #Loudness
      loudness.append(audio_features[0]['loudness'])

      #Mode
      mode.append(audio_features[0]['mode'])

      #Speechiness
      speechiness.append(audio_features[0]['speechiness'])

      #Tempo
      tempo.append(audio_features[0]['tempo'])

      #Time Signature
      time_signature.append(audio_features[0]['time_signature'])

      #Valence
      valence.append(audio_features[0]['valence'])


    total_df['Country'] = country
    total_df['Track Name'] = track_name
    total_df['Artist Name'] = artist_name
    total_df['Album Name'] = album_name
    total_df['Popularity'] = popularity
    total_df['Date'] = publication_date
    total_df['Markets'] = available_markets
    total_df['Danceability'] = danceability
    total_df['Acousticness'] = acousticness
    total_df['duration'] = duration
    total_df['Energy'] = energy
    total_df['Instrumentalness'] = instrumentalness
    total_df['Key'] = key
    total_df['Liveness'] = liveness
    total_df['Loudness'] = loudness
    total_df['Mode'] = mode
    total_df['Speechiness'] = speechiness
    total_df['Tempo'] = tempo
    total_df['TSignature'] = time_signature
    total_df['Positiveness'] = valence

  df = pd.DataFrame(total_df)
  df.to_csv(f'/{countries[i]}{weeknum}.csv', index=False) #We create the file for every country.
# Save the DataFrame to a CSV file
