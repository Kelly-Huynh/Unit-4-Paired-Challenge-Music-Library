from lib.music_library import MusicLibrary

"""
Given a track name
Add track and false boolean to #self.tracks
"""
def test_add_track_successfully_to_list():
    music_library = MusicLibrary()
    music_library.add("Hello")
    assert music_library.tracks == ["Hello"]

# """
# Not given a track name
# Returns an empty list
# """
# def test_not_given_track_name_returns_empty_list():
#     pass

# """
# Given a track name that has been listened to
# Updates the track boolean to True in #self.tracks
# """
# def test_listened_track_name_marked_as_true():
#     pass

# """
# Given a track name that has been listened to
# Returns an error if that track doesn't exist
# """
# def test_listened_throws_error_if_track_doesnt_exist():
#     pass

# """
# Given a request to view all tracks
# Returns a list of track names
# """
# def test_all_tracks_returns_list_of_track_names():
#     pass

# """
# Given a request to view all tracks
# Returns an error if track list is empty
# """
# def test_all_tracks_throws_error_if_empty():
#     pass


# """
# Given a request to view listened tracks
# Returns a list of tracks that have been listened to
# """    
# def test_listened_tracks_returns_tracks_marked_as_true():
#     pass

# """
# Given a request to view unplayed tracks
# Returns a list of tracks that have not been listened to
# """
# def test_unplayed_tracks_returns_tracks_marked_as_false():
#     pass

# """
# Checking if a track name is duplicated in both unplayed and listened lists
# Returns True / False
# """
# def test_if_duplicate_track_exists_in_both_lists():
#     pass