from typing import Annotated

from fastapi import Depends,Header, HTTPException,APIRouter,Path

from src.requests import ( AddSongRatingRequest )
# from src.responses import (  )
from src.service import ( get_songs_attribute_by_title,get_paginated_songs_data,add_song_rating)


router = APIRouter()

#Route to check the health of the service
@router.get("/health")
async def health_check():
    """
    Return the health of the service 
        200 for health status 
        any other for signifiying error or downtime
    """
    return 200

@router.get("/all/limit/{limit}/offset/{offset}")
async def get_songs(
    limit : Annotated[int, Path(title="limit of data to be returned")],
    offset: Annotated[int, Path(title="offset of data to be returned")]):
    
    print(f"GET PAGINATED SONG CALLED WITH limit:{limit} ,offset: {offset}")
    res = await get_paginated_songs_data(limit,offset)
    return {"data": res}

@router.get("/attribute/title/{title}")
async def get_songs_attribute(
    title : Annotated[str, Path(title="limit of data to be returned")]):
    
    res = await get_songs_attribute_by_title(title)
    return {"data":res}

@router.post("/ratings/")
async def set_ratings(
    request_body : AddSongRatingRequest):
    song_title = request_body.song_title
    # song_id = None
    # if song_title is None or song_title == "":
    song_id = request_body.song_id
    rating = request_body.rating
    res = await add_song_rating(song_title,song_id,rating)
    return {"data":res}

# Write a backend REST APIs to serve normalized data generated in step 1.1. We believe
# APIs for enabling following two use cases are MUST HAVE in order to make it practically
# useful backend project.
# 1.2.1 [MUST HAVE] Front end should be able to request ALL the items in a normalized
# data set.
# Bonus point if you can implement pagination in API.
# 1.2.2 [MUST HAVE] Given a title as input, return all the attributes of that song
# 1.2.3 [ NICE TO HAVE] User should be able to rate a song using star rating ( 5 start being
# highest). Please be mindful of the fact that this requires normalized data to have one
# more column say star rating.
# 1.2.4 [BONUS] Write Unit tests