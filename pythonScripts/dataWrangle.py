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

d = {'col1': ['hello | brian | this | is | wack','sureley | you | can | figure | d'], 'col2' : ['ffs','you | got| this']}
df1 = pd.DataFrame(data=d)
print("DF1: ", df1)

def split_row_list(row, row_accumulator, tc, sep):
    ''' (series, list, str, str) -> list
    Data in the target column (tc) of the row series are split according to the separator (sep) and copied with the
    data contained within rows other columns. The new rows are appended to the row_accumulator list which is returned.
    '''
    # Create list of separated values for each row in target columns
    split_list = row[tc].split(sep)
    for s in split_list:
        # Create dict containing all data from row
        new_row = row.to_dict()
        # Set target column value to each element in split_list
        new_row[tc] = s
        # Create list containing new row data
        row_accumulator.append(new_row)
    return row_accumulator


def split_rows(df, tc, sep):
    ''' (DataFrame, str, str) -> DataFrame

    Splits all rows in target column (tc) in DataFrame (df) according to separator (sep).
    Returns a new DafaFrame with all rows in tc split, with all other columns copied.
    '''

    new_rows = []
    df.apply(split_row_list, axis=1, args=(new_rows, tc, sep))
    split_df = pd.DataFrame(new_rows)
    return split_df


col1_df = split_rows(df1, 'col1', '|')
col12_df = split_rows(col1_df, 'col2', '|')
print(col12_df)
