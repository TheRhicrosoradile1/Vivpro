from pydantic import BaseModel

from typing import Optional,Any
# from .models import Song

# class Song():
#     class Song:
#         def __init__(self, song_builder):
#             self.id = song_builder.id
#             self.title = song_builder.title
#             self.danceability = song_builder.danceability
#             self.energy = song_builder.energy
#             self.key = song_builder.key
#             self.loudness = song_builder.loudness
#             self.mode = song_builder.mode
#             self.acousticness = song_builder.acousticness
#             self.instrumentalness = song_builder.instrumentalness
#             self.liveness = song_builder.liveness
#             self.avg_rating = song_builder.avg_rating
#             self.ratings = song_builder.ratings
            
class PaginatedResponse(BaseModel):
    songList: list[Any]  ## TODO: better this 
    total: int
