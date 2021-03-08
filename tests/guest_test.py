import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Dani")

    def test_guest_has_name(self):
        self.assertEqual("Dani", self.guest.guest_name)