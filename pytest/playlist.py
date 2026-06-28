"""
Build a playlist that behaves like a real
python sequence using dunder methods
"""
class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        minute = self.duration // 60
        second = self.duration % 60
        return f"{self.title} by {self.artist} ({minute:02}:{second:02})"
    
    def __repr__(self):
        return self.__str__()

class Playlist:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)
        print(f"{track.title} added to playlist")

    def __len__(self):
        return len(self.tracks)

    def __str__(self):
        return f"Playlist: {len(self.tracks)} tracks"
    

    def __iter__(self):
        return iter(self.tracks)
    
    def __getitem__(self, index):
        return self.tracks[index]
        

t1 = Track("Loss Yourself", "Eminem", 326)       
t2 = Track("FEAR", "Kendrick", 284)       
t3 = Track("Carbon", "Muqata'a", 197)       
t4 = Track("Pyramids", "Frank Ocean", 543)       

pl = Playlist()
pl.add_track(t1)
pl.add_track(t2)
pl.add_track(t3)
pl.add_track(t4)

print(t1)
print(len(pl))
print(str(pl))

for track in pl:
    print(track)

print(pl[2])
print(pl[0:-1])