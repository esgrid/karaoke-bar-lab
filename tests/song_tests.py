import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Song", "Artist")
    
    def test_song_name(self):
        self.assertEqual("Song", self.song.name)

    def test_song_artist(self):
        self.assertEqual("Artist", self.song.artist)