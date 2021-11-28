class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.room = ""
    
    def can_afford(self, room_fee_or_expense):
        return self.wallet > room_fee_or_expense
    
    def go_in_room(self, room_number):
        self.room = room_number
    
    def pay(self, amount):
        self.wallet -= amount

    def fav_song_in_room(self, songs_in_room):
        if self.fav_song in [song.name for song in songs_in_room]:
            return "Yeah baby!"
        else:
            return "Boring!"