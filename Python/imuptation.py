# 1: replace missing data with mean... doesnt change the mean 
# Rubbish for correlations!
# 2: Linear regression - predict the missing value
# but this over emphasised existing trends 
# missing values will have exact value giving false presision
# 3: Much better methods not covered here!
import pandas
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    baseball['weight'] = baseball['weight'].fillna(baseball['weight'].mean())
    

    return baseball