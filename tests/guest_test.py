import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Dani", 50000)

    def test_guest_has_name(self):
        self.assertEqual("Dani", self.guest.guest_name)

    def test_guest_has_money(self):
        self.assertEqual(50000, self.guest.money)