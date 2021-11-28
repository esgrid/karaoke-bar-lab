import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Juan", 100.00, "Song 1")
        self.guest2 = Guest("Juanito", 10.00, "Song 2")
        self.song = Song("Song 1", "Artist 1")
        self.room = Room(1, [], [], 10, 50)
    
    def test_guest_has_name(self):
        self.assertEqual("Juan", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertTrue(self.guest.wallet > 0)
    
    def test_guest_has_favourite_song(self):
        self.assertIsInstance(self.guest.fav_song, str)
    
    # @unittest.skip("Delete when testing for guest can afford")
    def test_guest_can_afford(self):
        self.assertTrue(self.guest.can_afford(self.room.fee))

    # @unittest.skip("Delete when testing for guest cannot afford")
    def test_guest_cannot_afford(self):
        self.assertTrue(not self.guest2.can_afford(self.room.fee))
    
    def test_guest_go_in_room(self):
        self.guest.go_in_room(self.room.number)
        self.assertEqual(self.room.number, self.guest.room)

    def test_pay(self):
        self.guest.pay(10)
        self.assertEqual(90, self.guest.wallet)

    def test_fav_song_in_room(self):
        self.assertEqual("Yeah baby!", self.guest.fav_song_in_room([self.song]))
        self.assertEqual("Boring!", self.guest2.fav_song_in_room([self.song]))