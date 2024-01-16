from datetime import datetime
from .repository import *
from .models import Song
from .data.songs_data import song_data_df, load_data
from fuzzywuzzy import fuzz
from .responses import PaginatedResponse


# ----------------------------------------------------------------
async def get_songs_attribute_by_title(title:str):
    song_data = load_data(song_data_df)
    song_data['title_lower'] = song_data['title'].str.lower()
    title_lower = title.lower()
    
    result_df = song_data[song_data['title_lower']==(title_lower)]
    # Drop the temporary 'title_lower' column
    result_df = result_df.drop(columns=['title_lower'])
    
    if result_df.empty:
        result_df = song_data[song_data['title_lower'].str.contains(title_lower)]
        # If no exact match, check for partial matches (75-80% match)
        partial_matches = song_data[song_data['title_lower'].apply(lambda x: fuzz.ratio(x, title_lower) >= 50)]

        print(f"partial_matches : {partial_matches} ")
        # Drop the temporary 'title_lower' column
        partial_matches = partial_matches.drop(columns=['title_lower'])

        return {
            "data":{
                "results":result_df.to_dict(orient='records'),
                "complete_match":False,
                "partial_matches":partial_matches.to_dict(orient='records'),
                "status" : "success",
                "message" : "rating added successfully",
                "status_code" : "200"
                },
            "error": ""
            }
    else:
        return {
            "data":{
                "results":result_df.to_dict(orient='records'),
                "complete_match":True,
                "partial_matches":None,
                "status" : "success",
                "message" : "rating added successfully",
                "status_code" : "200"
                },
            "error": ""
            }
    
# ----------------------------------------------------------------

'''
Query parameters: limit, offset, and pagesize for flexible pagination.
Pydantic models: Ensure data validation and clarity.
Offset calculation: Handle both offset and page parameters for convenience.
'''
async def get_paginated_songs_data(limit:int,offset:int):
    song_data = load_data(song_data_df)
    end_offset = offset + limit
    print("")
    song_list = song_data.iloc[offset:end_offset]
    print(f"song data is {song_list}")
    return song_list.to_dict(orient='records')  

    ##TODO: correct this 
    # return PaginatedResponse(songList=song_list, total=len(song_data))

# ----------------------------------------------------------------

async def add_song_rating(song_title:str,song_id:int,rating:int):
    song_data = load_data(song_data_df)
    if song_id is not None or song_title == "":
        song = song_data[song_data['id']==(id)].to_dict(orient='records')
    if not song:
        song_data['title_lower'] = song_data['title'].str.lower()
        title_lower = song_title.lower()
        song = song_data[song_data['title_lower']==(title_lower)].to_dict(orient='records')
        
    print("song : ",song)
    
    if not song:
        return {
            "data":{},
            "error": "Item not found"
            }
    # if len(song["ratings"]) > 0:
    song[0]["ratings"].append(rating)  # Assuming a `ratings` list in the Item model
    average_rating = sum(song[0]["ratings"]) / len(song[0]["ratings"])
    song[0]["avg_rating"] = average_rating
    # else :
    #     song.ratings = [rating]  # Assuming a `ratings` list in the Item model
    #     average_rating = sum(song.ratings) / len(song.ratings)
    #     song.avg_rating = average_rating
    
    return {
            "data":{
                "rating":     song[0]["ratings"],  
                "avg_rating" : song[0]["avg_rating"],
                "status" : "success",
                "message" : "rating added successfully",
                "status_code" : "200"
                },
            "error": ""
            }


    