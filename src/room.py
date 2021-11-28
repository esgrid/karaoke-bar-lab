class Room:
    def __init__(self, number, guests, songs, fee, total_capacity):
        self.number = number
        self.guests = [{"guest": guest, "tab": 0} for guest in guests]
        self.songs = songs
        self.fee = fee
        self.total_capacity = total_capacity
        self.earnings = 0

    def space_in_room(self):
        return (self.total_capacity - len(self.guests)) > 0

    def guest_in_room(self, guest):
        return guest.name in [x["guest"].name for x in self.guests]

    def add_remove_guest(self, guest, add_guest):
        if add_guest and not self.guest_in_room(guest) and self.space_in_room(): 
            self.guests.append({"guest": guest, "tab": 0})
            return f"Guest {guest.name} added successfully."
        elif not add_guest and self.guest_in_room(guest): 
            self.guests = [x for x in self.guests if x["guest"].name != guest.name]
            return f"Guest {guest.name} removed successfully."
        elif add_guest:
            return f"{guest.name} is already in the room."
        else:
            return f"{guest.name} is not in the room."
    
    def song_in_room(self, song):
        return song.name in [room_song.name for room_song in self.songs]

    def add_remove_song(self, song, add_song):
        if add_song and not self.song_in_room(song):
            self.songs.append(song)
            return "Song added successfully."
        elif not add_song and self.song_in_room(song):
            self.songs = [s for s in self.songs if s.name != song.name]
            return "Song removed successfully."
        elif add_song:
            return f"{song.name} is already in the room list."
        else:
            return f"{song.name} cannot be removed because it is not on the list."

    def charge_fee(self):
        self.earnings += self.fee

    def charge_extra_expenses(self, guest, amount):
        if guest.name in [r_guest["guest"].name for r_guest in self.guests]:
            if guest.can_afford(amount):
                guest.pay(amount)
                self.earnings += amount
                return "Charge paid successfully."
            else:
                return f"{guest.name} cannot afford £{amount}."
        else:
            return f"{guest.name} is not in the room."

    def favourite_song(self, guest):
        return guest.fav_song.lower() in [song.name.lower() for song in self.songs]
    

