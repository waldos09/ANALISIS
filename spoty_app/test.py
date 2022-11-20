# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:07:51 2022

@author: waldo
"""
import json
import requests
import secret



class lastFMSpotify:
    def __init__(self):
        self.token = secret.spotify_token()
        self.api_key = secret.last_fm_api_key()
        self.user_id = secret.spotify_user_id()
        self.spoty_headers = {"Content-Type": "application/json",
                        "Authorization" : f"Bearer {self.token}"}
        self.playlist_id = ''
        self.song_info = {}
        self.uris = []
        
        
        
    def Tops_songs(self):
        params = {'limit': 20, 'api_key': self.api_key}
        url = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&format=json'
        
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print('Error')
        res = response.json()
        for item in res['tracks']['track']:
            song = item['name'].title()
            artist = item['artist']['name'].title()
            #print(song, artist)z
            self.song_info[song] = artist
        self.get_url_song()
        self.create_spoty_playlist()
        self.add_songs()
        
    
    def get_url_song(self):
        
        for song_name,artist in self.song_info.items():
            url = f'https://api.spotify.com/v1/search?query=track%3A{song_name}+artist%3A{artist}&type=track&offset=0&limit=10'
            response = requests.get(url, headers= self.spoty_headers)
            
            #saber si el estatus es correcto (200) print(response.status_code)
            
            res = response.json()            
            output_uri = res['tracks']['items']
            uri = output_uri[0]['uri']
            #print(song_name,uri)
            self.uris.append(uri)
    
    def create_spoty_playlist(self):
        #data debe ser de tipo diccionario y no json
        data = {
          "name": "Top songs API",
          "description": "Last top songs on spoty",
          "public": True
        }
        #con esto pasamo data como un dic 
        data = json.dumps(data)
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = requests.post(url, data=data, headers=self.spoty_headers)
        #print(response.status_code)
        if response.status_code == 201:
            #print("Se creo la playlist")
            res = response.json()
            self.playlist_id = res['id']
        else:
            print(response.content)
    
    
    
    def add_songs(self):
        
        uri_list = json.dumps(self.uris)
        url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"   
        
        response = requests.post(url, data = self.uris , headers = self.spoty_headers)
        if response.status_code == 201:
            print('Se han añadido las canciones ')
    
    def list_songs(self):
        pass



d = lastFMSpotify()
d.Tops_songs()




