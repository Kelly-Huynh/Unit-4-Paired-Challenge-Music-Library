import pytest

class MusicLibrary:
    def __init__(self):
        self.tracks = {}

    """
    {
        {'Hello': False },
        {'abc' : True }
    }
    """
    
    def add(self, track):
        self.tracks[track] = False

    def listened(self, track):
        if track in self.tracks:
            self.tracks[track] = True
        else:
            raise Exception("Track does not exist.")

    def all_tracks(self):
        if self.tracks == {}:
            raise Exception("Tracklist is empty.")
        else:
            return list(self.tracks.keys())

    def listened_tracks(self):
        listened_tracklist = []
        for track in self.tracks:
            if self.tracks[track] is True:
                listened_tracklist.append(track)
        if listened_tracklist == []:
            raise Exception("No listened tracks.")
        else:
            return listened_tracklist

    def unplayed_tracks(self):
        unplayed_tracklist = []
        for track in self.tracks:
            if self.tracks[track] is False:
                unplayed_tracklist.append(track)
        if unplayed_tracklist == []:
            raise Exception("No unplayed tracks.")
        else:
            return unplayed_tracklist