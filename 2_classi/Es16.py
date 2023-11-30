
#Pelusi Matteo e Tamburini Filippo 4M Es16

class Artist:
    def __init__(self, name):
        self.name = name

    def create_album(self, title):
        return Album(title)

class Album:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def contains_songs(self, song):
        self.songs.append(song)

class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class PremiumAlbum(Album):
    def __init__(self, title, exclusive_content):
        super().__init__(title)
        self.exclusive_content = exclusive_content

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

class Subscription:
    def __init__(self, type, price):
        self.type = type
        self.price = price

class User:
    def __init__(self, subscription, playlist, username, email):
        self.subscription = subscription
        self.playlist = playlist
        self.username = username
        self.email = email

#Esempio 
user1 = User("Premium","Crime1", "Franchino Er Criminale", "crimefranchi@gmail.com",)
artist1 = Artist("BabyGang & Simba la Gru")

album1 = artist1.create_album("La divina stronzata")
premium_album1 = artist1.create_album("Vattene in lobby v.2")

song1 = Song("Volevo te", 2.6)
song2 = Song("Omar", 3.2)

album1.contains_songs(song1)
premium_album1.contains_songs(song2)

playlist1 = Playlist("Xv3R")
playlist1.add_song(song1)
playlist1.add_song(song2)

subscription1 = Subscription("Premium", 13.99)
user1.subscription = subscription1

#Fase di stampa
print("User Information:")
print("User Name: ", user1.username)
print("User Email: ", user1.email)
print("Subscription Type: ", user1.subscription.type,"- Price: ",user1.subscription.price,"\n")

print("Name Of The Playlist:")
print(playlist1.name)
print("Name Of The Album:")
print(album1.artist1)
