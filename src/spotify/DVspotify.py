import pandas as pd
import spotipy
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyClientCredentials
import os

class DVspotify:
    cid = 'fd8f6370d5f241e581a546cfd19525a4'
    secret = 'd05f3d021bd64e858d0e1f70dc160621'
    sp = None
    client_credentials_manager = None
    real_path = os.path.realpath('../')

    def __init__(self):
        self.client_credentials_manager = SpotifyClientCredentials(client_id=self.cid, client_secret=self.secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        self.spotify_ids = pd.read_csv(self.real_path + '\\src\\data\\processed\\spotify\\spotifyIDs.csv')
        #self.spotify_ids = pd.read_csv('projects.danielvivas.com/song_recommender/spotipyIDs.csv')

    def msd_id_to_spotify_id(self, track_id):
        record = self.spotify_ids[self.spotify_ids['trackID'] == track_id]['SpotifyID']
        if record.shape[0] > 0:
            return self.spotify_ids[self.spotify_ids['trackID'] == track_id]['SpotifyID'].iloc[0].split(':')[2]
        else:
            return "Metadata not found"

    def get_full_name(self, track_id, translate):
        if translate:
            try:
                track_id = self.msd_id_to_spotify_id(track_id)
                results = self.sp.track(track_id)
                return results['artists'][0]['name'] + ' - ' + results['name']
            except SpotifyException as e:
                return "ID not found"

    def recently_played(self, limit=50):
        return self.sp.current_user_recently_played(limit)










#test = DVspotify()
#print(test.msd_id_to_spotify_id('SOBFNSP12AF72A0E22'))
#print(test.get_full_name('SOBFNSP12AF72A0E22', translate=True))
#print(test.recently_played())