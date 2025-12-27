import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def albumTrackInfo(spotify, album_id):
    album_song_ids = []
    album_song_pop = []
    results = spotify.album_tracks(album_id)
    tracklist_count = len(results['items'])
    
    for i in range(tracklist_count):
        album_song_ids.append(results['items'][i]['id'])

    for i in range(len(album_song_ids)):
        track_results = spotify.track(album_song_ids[i])
        name = track_results['name']
        popularity = track_results['popularity']
        album_song_pop.append(popularity)
        print(f'{name} (Popularity: {popularity})')
        
    print()
    print(f'Max popularity: {max(album_song_pop)}')
    print(f'Min popularity: {min(album_song_pop)}')
    print(f'Average popularity: {round(sum(album_song_pop)/len(album_song_pop), 2)}')
    print('---')
    
if __name__ == "__main__":
##    album_id = '355bjCHzRJztCzaG5Za4gq' # el mal querer
##    album_id = '6jbtHi5R0jMXoliU2OS0lo' # motomami
##    album_id = '3SUEJULSGgBDG1j4GQhfYY' # LUX
##    album_id = '4bxHLppgdmaYJk0yfdcP0l' # con altura
##    album_id = '3844bY26oeSkqd06th4EYp' # Yo x Ti, Tu x Mi
##    album_id = '5omNd3Mkij9C3ZeW19rRmv' # despecha
##    album_id = '50uChhk7AKkzDKytDixjYW' # rr
    album_id = ['355bjCHzRJztCzaG5Za4gq', '6jbtHi5R0jMXoliU2OS0lo', '3SUEJULSGgBDG1j4GQhfYY', '4bxHLppgdmaYJk0yfdcP0l', '3844bY26oeSkqd06th4EYp', '5omNd3Mkij9C3ZeW19rRmv', '50uChhk7AKkzDKytDixjYW']
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='', client_secret=''))
    
    for i in range(len(album_id)):
        albumTrackInfo(spotify, album_id[i])
