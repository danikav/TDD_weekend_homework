class Room():

    def __init__ (self, room_number, capacity, entry_fee, songs =[]):
        self.room_number = room_number
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.songs = songs
        self.guests = []
        self.till = 0

    def add_song(self, new_song):
        self.songs.append(new_song)

    def check_guest_in(self, new_guest):
        if len(self.guests) < self.capacity: 
            self.guests.append(new_guest)
        else:
            return "Sorry this room is full!"

    def check_guest_out(self, guest):
        if len(self.guests) > 0:
            self.guests.remove(guest)

    def charges_fee(self, guest):
        if guest.money >= self.entry_fee:
            guest.money -= self.entry_fee
            self.till += self.entry_fee
        else:
            return "Sorry you can't afford this"

    def check_favourite_song(self, guest):
        for song in self.songs:
            if guest.favourite_song == song.song_name:
                return "Whooo"
        else:
            return "Oh no"

    def check_cash_in_till(self):
        return self.till
    
        