import numpy as np

def less_set_to_one(df, column):
    '''Takes in a dataframe column and reassigns to 1 all values that are less than or equal to 1.
    Overwrites the input column!'''
    df[column] = np.where(df[column] <= 1, 1, df[column])
    
def great_set_to_one(df, column):
    '''Takes in a dataframe column and reassigns to 1 all values that are greater than or equal to 1.
    Overwrites the input column!'''
    df[column] = np.where(df[column] >= 1, 1, df[column])
    
def zero_to_median(df, column):
    '''Takes in a dataframe column and reassigns to the column's median value all values that are less than
    or equal to 0.
    Overwrites the input column!'''
    df[column] = np.where(df[column] <= 0, df[column].median(), df[column])
    
def one_to_median(df, column):
    '''Takes in a dataframe column and reassigns to the column's median value all values that are equal to 1.
    Overwrites the input column!'''
    df[column] = np.where(df[column] == 1, df[column].median(), df[column])
    
def neg_one_to_median(df, column):
    '''Takes in a dataframe column and reassigns to the column's median value all values that are equal to -1.
    Overwrites the input column!'''
    df[column] = np.where(df[column] == -1, df[column].median(), df[column])