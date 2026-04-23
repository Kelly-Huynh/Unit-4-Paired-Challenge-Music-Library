class MusicLibrary:
    def __init__(self):
        self.tracks = []
    
    def add(self, track):
        # side-effects: 
        #   adds track to self.track list using .append
        self.tracks.append(track)

    def listened(self, track):
        # Parameter:
        #   track: string
        # side-effects: 
        #   marks track as listened by changing value of listened track
        # listened = True / False
        pass

    def all_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   list of keys of dictionary, using .keys
        pass

    def listened_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   list of keys that have True value from dictionary, using .keys
        pass

    def unplayed_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   list of keys that have False value from dictionary, using .keys
        pass