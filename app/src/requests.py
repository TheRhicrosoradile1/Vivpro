from pydantic import BaseModel
from typing import Optional

class AddSongRatingRequest(BaseModel):
    song_title:str
    song_id:Optional[int]
    rating:int
