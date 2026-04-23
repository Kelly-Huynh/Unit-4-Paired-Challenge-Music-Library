# {{Music Library}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep *track* of my music listening
> I want to *add* tracks I've _listened_ to and *see* a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

# [{track:track_name, listened: False}, {track:track_name, listened: False},]
# [{track_name:False}]

class MusicLibrary():
    def __init__(self):
        # Parameters:
        # self.tracks = []
        pass
    
    def add(self, track):
        # Parameter:
        #   track: string
        # side-effects: 
        #   adds track to self.track list using .append

    def listened(self, track):
        # Parameter:
        #   track: string
        # side-effects: 
        #   marks track as listened by changing value of listened track
        # listened = True / False
    def all_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   list of keys of dictionary, using .keys

    def listened_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   list of keys that have True value from dictionary, using .keys

    def unplayed_tracks(self):
        # Parameters:
        #   none
        # Returns:
        #   list of keys that have False value from dictionary, using .keys
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE
"""
Given a track name
Add track and false boolean to #self.tracks
"""
def test_add_track_successfully_to_list():
    pass
"""
Not given a track name
Returns an empty list
"""
def test_not_given_track_name_returns_empty_list():
    pass

"""
Given a track name that has been listened to
Updates the track boolean to True in #self.tracks
"""
def test_listened_track_name_marked_as_true():
    pass

"""
Given a track name that has been listened to
Returns an error if that track doesn't exist
"""
def test_listened_throws_error_if_track_doesnt_exist():
    pass

"""
Given a request to view all tracks
Returns a list of track names
"""
def test_all_tracks_returns_list_of_track_names():
    pass

"""
Given a request to view all tracks
Returns an error if track list is empty
"""
def test_all_tracks_throws_error_if_empty():
    pass


"""
Given a request to view listened tracks
Returns a list of tracks that have been listened to
"""    
def test_listened_tracks_returns_tracks_marked_as_true():
    pass

"""
Given a request to view unplayed tracks
Returns a list of tracks that have not been listened to
"""
def test_unplayed_tracks_returns_tracks_marked_as_false():
    pass

"""
Checking if a track name is duplicated in both unplayed and listened lists
Returns True / False
"""
def test_if_duplicate_track_exists_in_both_lists():
    pass
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
