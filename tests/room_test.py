import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        song_1 = Song("Gold", "Spandeau Ballet")
        song_2 = Song("Piano Man", "Billy Joel")
        song_3 = Song("Irelands Call", "Phil Coulter")
        song_4 = Song("Everywhere", "Fleetwood Mac")
        songs = [song_1, song_2, song_3, song_4]
        self.room = Room(1, 10, songs)

    def test_count_songs(self):
        self.assertEquals(4, len(self.room.songs))

    def test_add_song_to_room(self):
        new_song = Song("Area Codes", "Ludacris")
        self.room.add_song(new_song)
        self.assertEqual(5, len(self.room.songs))

    def test_check_guest_in(self):
        guest_1 = Guest("Dani")
        self.room.check_guest_in(guest_1)
        self.assertEqual(1, len(self.room.guests))

    def test_check_guest_out(self):
        guest_1 = Guest("Dani")
        self.room.check_guest_in(guest_1)
        self.room.check_guest_out(guest_1)
        self.assertEqual(0, len(self.room.guests))


