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
        song_5 = Song("I'm on a boat", "The Lonely Island")
        song_6 = Song("Jolene", "Dolly Parton")
        songs = [song_1, song_2, song_3, song_4, song_5, song_6]
        self.room = Room(1, 4, songs)

    def test_count_songs(self):
        self.assertEqual(6, len(self.room.songs))

    def test_add_song_to_room(self):
        new_song = Song("Area Codes", "Ludacris")
        self.room.add_song(new_song)
        self.assertEqual(7, len(self.room.songs))

    def test_check_guest_in(self):
        guest_1 = Guest("Dani")
        self.room.check_guest_in(guest_1)
        self.assertEqual(1, len(self.room.guests))

    def test_check_guest_out(self):
        guest_1 = Guest("Dani")
        self.room.check_guest_in(guest_1)
        self.room.check_guest_out(guest_1)
        self.assertEqual(0, len(self.room.guests))

    def test_can_guests_fit__too_many(self):
        guest_1 = Guest("Zsolt")
        guest_2 = Guest("Chris")
        guest_3 = Guest("Malcolm")
        guest_4 = Guest("Dani")
        guest_5 = Guest("Tim")
        self.room.check_guest_in(guest_1)
        self.room.check_guest_in(guest_2)
        self.room.check_guest_in(guest_3)
        self.room.check_guest_in(guest_4)
        self.assertEqual("Sorry this room is full!", self.room.check_guest_in(guest_5))
        self.assertEqual(4, len(self.room.guests))


