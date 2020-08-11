import pandas as pd
import numpy as np
# Read dataset columns

all_columns = pd.read_csv('static/data/sold_geocoded.csv',low_memory=False).columns.values
print (all_columns)
use_cols = ['MLSNUM','DisplayX','DisplayY','ZIP','AGE','BATHS','BEDS','GARAGE','LISTDATE',
            'LISTPRICE','LOTSIZE','PROPTYPE','SOLDPRICE','SQFT', 'PPSF', 'PHOTOURL', 'REMARKS', 'LISTMONTH']
# Load data with selected set of features
df_all = pd.read_csv('static/data/sold_geocoded.csv', usecols=use_cols)
print (df_all.head())

# Clean PPSF data
# PPSF has many "inf" values that need to be removed
# Take a look at the function below and 
# make sure there are no any "nan" or "inf" values left

df_all['PPSF'] = df_all['PPSF'].round(2)

# array to store indices
indexes = []

# colect all indices that contain "inf" value
for p in enumerate(df_all['PPSF']):
    if p[1] == np.inf:
        indexes.append(p[0])
        
# drop all rows with "inf" values        
df_all = df_all.drop(df_all.index[indexes])

# Check the shape of the data - you should be able to see (158874, 17)
print (df_all.shape)
print (df_all.dtypes)
