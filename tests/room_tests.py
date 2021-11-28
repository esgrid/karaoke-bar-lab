import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Guest", 20.00, "Song")
        self.guest1 = Guest("Guest 1", 35.00, "Song 1")
        self.guest2 = Guest("Guest 2", 45.00, "Song 2")
        self.guest3 = Guest("Guest 3", 50.00, "Song 3")
        self.guests = [self.guest1, self.guest2, self.guest3]

        self.song = Song("Song", "Artist")
        self.song1 = Song("Song 1", "Artist 1")
        self.song2 = Song("Song 2", "Artist 2")
        self.song3 = Song("Song 3", "Artist 3")
        self.songs = [self.song1, self.song2, self.song3]
        
        self.fees = [10, 15, 8]

        self.room1 = Room(1, self.guests, self.songs, self.fees[0], 20)
        self.room2 = Room(2, self.guests[0:2], self.songs[0:2], self.fees[1], 2)
        self.room3 = Room(3, self.guests[0:1], self.songs[0:1], self.fees[2], 15)


    # @unittest.skip("Delete or comment to test")
    def test_add_remove_guest(self):
        message = self.room1.add_remove_guest(self.guest, True)
        self.assertEqual(self.guest.name, self.room1.guests[3]["guest"].name)
        self.assertEqual(f"Guest {self.guest.name} added successfully.", message)
        message2 = self.room2.add_remove_guest(self.guest1, False)
        self.assertIsNot(self.guest1.name, [x["guest"].name for x in self.room2.guests])
        self.assertEqual(f"Guest {self.guest1.name} removed successfully.", message2)

        message3 = self.room1.add_remove_guest(self.guest, True)
        self.assertEqual(f"{self.guest.name} is already in the room.", message3)
        message4 = self.room2.add_remove_guest(self.guest1, False)
        self.assertEqual(f"{self.guest1.name} is not in the room.", message4)

    def test_space_in_room_True(self):
        self.assertTrue(self.room1.space_in_room())
    
    def test_space_in_room_False(self):
        self.assertTrue(not self.room2.space_in_room())

    # @unittest.skip("Delete to test if guest is in the room")
    def test_guest_in_room_True(self):
        self.assertTrue(self.room1.guest_in_room(self.guest1))

    # @unittest.skip("Delete to test if guest is not in the room")
    def test_guest_in_room_False(self):
        self.assertTrue(not self.room1.guest_in_room(self.guest))
    
    def test_song_in_room_True(self):
        self.assertTrue(self.room1.song_in_room(self.song1))

    def test_song_in_room_False(self):
        self.assertTrue(not self.room2.song_in_room(self.song))

    def test_add_remove_song(self):
        message = self.room1.add_remove_song(self.song, True)
        self.assertEqual(self.song.name, self.room1.songs[3].name)
        self.assertEqual("Song added successfully.", message)
        message2 = self.room2.add_remove_song(self.song1, False)
        self.assertIsNot(self.song1.name, [song.name for song in self.room2.songs])
        self.assertEqual("Song removed successfully.", message2)
        
        message3 = self.room1.add_remove_song(self.song, True)
        self.assertEqual(f"{self.song.name} is already in the room list.", message3)
        message4 = self.room2.add_remove_song(self.song1, False)
        self.assertEqual(f"{self.song1.name} cannot be removed because it is not on the list.", \
                        message4)

    def test_charge_fee(self):
        self.room1.charge_fee()
        self.assertEqual(10, self.room1.earnings)

    def test_charge_extra_expenses(self):
        message = self.room1.charge_extra_expenses(self.guest, 10)
        self.assertEqual(f"{self.guest.name} is not in the room.", message)
        added = self.room1.add_remove_guest(self.guest, True)
        self.assertEqual(f"Guest {self.guest.name} added successfully.", added)
        message1 = self.room1.charge_extra_expenses(self.guest, 10)
        self.assertEqual(10, self.guest.wallet)
        self.assertEqual("Charge paid successfully.", message1)
        self.assertEqual(f"{self.guest.name} cannot afford £{10}.", \
                        self.room1.charge_extra_expenses(self.guest, 10))

    def test_favourite_song(self):
        self.assertTrue(self.room1.favourite_song(self.guest1))
        self.assertTrue(not self.room2.favourite_song(self.guest))