# -*- coding: utf-8 -*-
import pandas as pd


df = pd.read_csv('Datasets/direct_marketing.csv',
                 sep=',')

print df.head(5)


print
print


#
# Produces a series object:
print 'Series objects:'
print
print df.recency.head(5)
print
print df['recency'].head(5)
print
print df.loc[:, 'recency'].head(5)
print
print df.iloc[:, 0].head(5)
print
print df.ix[:, 0].head(5)


print
print


#
# Produces a dataframe object:
print 'Dataframe objects:'
print
print df[['recency']].head(5)
print
print df.loc[:, ['recency']].head(5)
print
print df.iloc[:, [0]].head(5)


print
print


#
# Row Indexing
print 'Row Indexing'
print
print df[0:2]
print
print df.iloc[0:2, :]
# The last important difference is that .loc[] and .ix[]
# are inclusive of the range of values selected,
# where .iloc[] is non-inclusive. In that sense,
# df.loc[0:1, :] would select the first two rows,
# but only the first row would be returned using df.iloc[0:1, :].


print
print

#
# Boolean Indexing
print 'Boolean Indexing'
print
print df.recency < 7
print
print df[ df.recency < 7 ].head(5)
print
print df[ (df.recency < 7) & (df.newbie == 0) ].head(5)


print
print


#
# Writing to a Slice
print 'Writing to a Slice'
print
df[df.recency < 7] = -100
print df.head(5)
