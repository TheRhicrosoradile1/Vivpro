
import pandas as pd
import json
 
# Corrected the attribute name to dumps
# with open('app/src/data/data.json') as user_file:
#     song_data = user_file.read()
song_data_df = None

def load_data(song_data_df):
    if song_data_df is not None:
        return song_data_df
    song_data_df = pd.read_json('/Users/abhinandanvyas/Recruit assignment/Vivpro/app/src/data/data.json')
    song_data_df['ratings'] = song_data_df.apply(lambda row: [], axis=1)

    # Calculate the average rating for each row
    song_data_df['avg_rating'] = 0
    return song_data_df
# song_data_df['index'] = song_data_df.index
# print(song_data.columns)
# print(song_data.head())