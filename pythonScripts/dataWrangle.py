import pandas as pd
import numpy as np

df = pd.read_csv('/home/ding/coding/DAND/investigate_dataset_project/movies_dataset/tmdb-movies.csv', engine='python')

def clean_data(df):
    '''
    Set of common functions used to clean up df
    return None
    '''
    df.drop_duplicates(inplace=True)
    drop_columns = ['homepage', 'tagline', 'imdb_id']
    df.drop(labels=drop_columns, axis=1, inplace=True)
