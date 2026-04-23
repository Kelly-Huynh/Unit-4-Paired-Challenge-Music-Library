from lib.music_library import MusicLibrary
import pytest

"""
Given a track name
Add track and false boolean to #self.tracks
"""
def test_add_track_successfully_to_list():
    music_library = MusicLibrary()
    music_library.add("Hello")
    assert music_library.tracks == {"Hello": False}

"""
Not given a track name
Returns an empty list
"""
def test_not_given_track_name_returns_empty_list():
    music_library = MusicLibrary()
    assert music_library.tracks == {}

"""
Given a track name that has been listened to
Updates the track boolean to True in #self.tracks
"""
def test_listened_track_name_marked_as_true():
    music_library = MusicLibrary()
    music_library.add("Hello")
    music_library.add("American Pie")
    music_library.listened("Hello")
    assert music_library.tracks["Hello"] is True

"""
Given a track name that has been listened to
Returns an error if that track doesn't exist
"""
def test_listened_throws_error_if_track_doesnt_exist():
    music_library = MusicLibrary()
    music_library.add("Hello")
    print(music_library.tracks)
    with pytest.raises(Exception) as e:
        music_library.listened("abc")
    assert str(e.value) == "Track does not exist."

"""
Given a request to view all tracks
Returns a list of track names
"""
def test_all_tracks_returns_list_of_track_names():
    music_library = MusicLibrary()
    music_library.add("Hello")
    music_library.add("American Pie")
    music_library.listened("Hello")
    assert music_library.all_tracks() == ["Hello", "American Pie"]

"""
Given a request to view all tracks
Returns an error if track list is empty
"""
def test_all_tracks_throws_error_if_empty():
    music_library = MusicLibrary()
    with pytest.raises(Exception) as e:
        music_library.all_tracks()
    assert str(e.value) == "Tracklist is empty."

"""
Given a request to view listened tracks
Returns a list of tracks that have been listened to
"""    
def test_listened_tracks_returns_tracks_marked_as_true():
    music_library = MusicLibrary()
    music_library.add("Hello")
    music_library.add("American Pie")
    music_library.listened("Hello")
    assert music_library.listened_tracks() == ["Hello"]

"""
Given a request to view unplayed tracks
Returns a list of tracks that have not been listened to
"""
def test_unplayed_tracks_returns_tracks_marked_as_false():
    music_library = MusicLibrary()
    music_library.add("Hello")
    music_library.add("American Pie")
    music_library.listened("Hello")
    assert music_library.unplayed_tracks() == ["American Pie"]

"""
Given a request to view unplayed tracks
Throws an error, as empty list
"""
def test_unplayed_tracks_throws_an_error_if_empty():
    music_library = MusicLibrary()
    music_library.add("Hello")
    music_library.add("American Pie")
    music_library.listened("Hello")
    music_library.listened("American Pie")
    with pytest.raises(Exception) as e:
        music_library.unplayed_tracks()
    assert str(e.value) == "No unplayed tracks."

"""
Given a request to view listened tracks
Throws an error, as empty list
"""
def test_listened_tracks_throws_an_error_if_empty():
    music_library = MusicLibrary()
    music_library.add("Hello")
    music_library.add("American Pie")
    with pytest.raises(Exception) as e:
        music_library.listened_tracks()
    assert str(e.value) == "No listened tracks."
