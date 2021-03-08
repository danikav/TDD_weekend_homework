class Room():

    def __init__ (self, room_number, capacity, songs =[]):
        self.room_number = room_number
        self.capacity = capacity
        self.songs = songs
        self.guests = []

    def add_song(self, new_song):
        self.songs.append(new_song)

    def check_guest_in(self, new_guest):
        self.guests.append(new_guest)

    def check_guest_out(self, guest):
        self.guests.remove(guest)