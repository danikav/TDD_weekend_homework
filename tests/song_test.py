import unittest
from src.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Gold", "Spandeau Ballet")

    def test_song_has_name (self):
        self.assertEqual("Gold", self.song.song_name)
    
    