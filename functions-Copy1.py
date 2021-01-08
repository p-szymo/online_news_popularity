import numpy as np
from scipy.stats import ttest_ind

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
    
def log_col(df, column):
    '''Takes in a dataframe column and creates a new column with a log transformation.
    Drops the input column!'''
    new_col = 'log_' + column
    df[new_col] = df[column].apply(lambda x: np.log(x))
    df.drop(columns=column, inplace=True)
    
def find_extremes(df):
    '''Takes in a dataframe and returns a list of columns with values farther than 4 standard deviations from the mean.'''
    extreme_list = []
    for column in list(df.columns):
        if df[column].max() > (df[column].mean() + 4*df[column].std()):
            extreme_list.append(column)
        if df[column].min() < (df[column].mean() - 4*df[column].std()):
            extreme_list.append(column)
    return extreme_list

def rein_extremes(df, columns):
    '''Takes in a dataframe and a list of columns and changes any values farther than 4 standard deviations from the mean
    to 4 standard deviations from the mean.
    Overwrites the input column!'''
    for column in columns:
        mean = df[column].mean()
        std = df[column].std()
        conditions = [df[column] > mean + 4*std,
                      df[column] < mean - 4*std]
        choices = [mean + 4*std,
                   mean - 4*std]
        df[column] = np.select(conditions, choices, df[column])
        
def two_way_tests(series_list):
    '''Takes in a list of series and runs a two-sided t-test on every combination within the list.
    Returns a dictionary with the indices of the tested series as the keys and the test results as the values.
    '''
    compare_dict = {}
    for i in range(len(series_list)):
        count = i+1
        while count < len(series_list):
            compare_dict.update({(i,count): ttest_ind(series_list[i], series_list[count])})
            count += 1
    return compare_dict
        
        
        
        
        