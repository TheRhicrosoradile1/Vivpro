class Song:
    def __init__(self, song_builder):
        self.id = song_builder.id
        self.title = song_builder.title
        self.danceability = song_builder.danceability
        self.energy = song_builder.energy
        self.key = song_builder.key
        self.loudness = song_builder.loudness
        self.mode = song_builder.mode
        self.acousticness = song_builder.acousticness
        self.instrumentalness = song_builder.instrumentalness
        self.liveness = song_builder.liveness
        self.avg_rating = song_builder.avg_rating
        self.ratings = song_builder.ratings

class SongBuilder:
    def __init__(self):
        self.song = Song(self)

    def set_id(self, song_id):
        self.id = song_id
        return self

    def set_title(self, title):
        self.title = title
        return self

    def set_danceability(self, danceability):
        self.danceability = danceability
        return self

    def set_energy(self, energy):
        self.energy = energy
        return self

    def set_key(self, key):
        self.key = key
        return self

    def set_loudness(self, loudness):
        self.loudness = loudness
        return self

    def set_mode(self, mode):
        self.mode = mode
        return self

    def set_acousticness(self, acousticness):
        self.acousticness = acousticness
        return self

    def set_instrumentalness(self, instrumentalness):
        self.instrumentalness = instrumentalness
        return self

    def set_liveness(self, liveness):
        self.liveness = liveness
        return self
    
    def set_avg_rating(self, avg_rating):
        self.avg_rating = avg_rating
        return self
    
    def set_ratings(self,rating):
        if self.ratings is not None or self.ratings.is_empty()==False:
            self.ratings = [rating]
        else:
            self.ratings.append(rating)
        return self
    def build(self):
        return self.song