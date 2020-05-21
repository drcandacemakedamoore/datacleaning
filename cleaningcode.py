
# Cleaning up data in Python
# 'skimming' at data in Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# step 2 is to load up the actual data into a dataframe we will call 'df'
# replace my file with your new file here
#here is an example without the path:

#df = pd.read_csv (r'Path where the CSV file is stored\File name.csv')

# now for real

df = pd.read_csv('C:/Users/makeda/programming/fakepatients.csv')
# the next step, step 3, part one, is to check we loaded by looking at say 20 elements- taking a peek
print (df.head(20))
#step 3.5 is to get details on the whole csv table
print('The column names on the table are:',df.columns)
print("The table has x entries with y data points- x,y here are:", df.shape)
print("Let's see the types of data:", df.dtypes)
print("The whole thing is ",df.info)
# step 4 is to start to clean up the data a bit
# let's look at how many duplicates we have
# duplicates here meanthe wholeline is duplicated

df.duplicated().sum()
# we can clean it later
