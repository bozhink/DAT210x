# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('', sep=',')

# Find nan
df.Feature.isnull()
df.Feature.notnull()

df.isnull()
df.notnull()


# Any time a nan is encountered, replace it with a scalar value:
df.my_feature.fillna( df.my_feature.mean() )
df.fillna(0)

# Forward/Backeard fill
df.fillna(method='ffill')  # fill the values forward
df.fillna(method='bfill')  # fill the values in reverse
df.fillna(limit=5)
df.fillna(method='ffill',limit=1)  # fill the values forward
df.fillna(method='bfill',limit=1)  # fill the values in reverse

# Interpolation
df.interpolate(method='polynomial', order=2)


# Remove nan
df = df.dropna(axis=0)  # row 
df = df.dropna(axis=1)  # column

# Drop any row that has at least 4 NON-NaNs within it:
df = df.dropna(axis=0, thresh=4)


# Delete fratures
# Axis=1 for columns
df = df.drop(labels=['Features', 'To', 'Delete'], axis=1)


# Drop duplicates
df = df.drop_duplicates(subset=['Feature_1', 'Feature_2'])

df = df.reset_index(drop=True)

df = df.dropna(axis=0,
               thresh=2).drop(labels=['ColA'],
                              axis=1).drop_duplicates(subset=['ColB', 'ColC']).reset_index()


# Type cast
df.Date = pd.to_datetime(df.Date, errors='coerce')
df.Height = pd.to_numeric(df.Height, errors='coerce')
df.Weight = pd.to_numeric(df.Weight, errors='coerce')
df.Age = pd.to_numeric(df.Age, errors='coerce')
df.Age.unique()
df.Age.value_counts()





