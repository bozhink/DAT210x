# -*- coding: utf-8 -*-
import pandas as pd

ordered_satisfaction = [
    'Very Unhappy',
    'Unhappy',
    'Neutral',
    'Happy',
    'Very Happy'
]

df = pd.DataFrame({'satisfaction':['Mad', 'Happy', 'Unhappy', 'Neutral']})
df.satisfaction = df.satisfaction.astype('category',
                                         ordered=True,
                                         categories=ordered_satisfaction
                                        ).cat.codes

print(df)





vertebrates = [
    'Bird',
    'Bird',
    'Mammal',
    'Fish',
    'Amphibian',
    'Reptile',
    'Mammal'
]

df = pd.DataFrame({'vertebrates':vertebrates})
print(df)

df1 = pd.DataFrame(df.vertebrates)
df1.vertebrates = df1.vertebrates.astype('category').cat.codes
print(df1)

df2 = pd.DataFrame(df.vertebrates)
df2 = pd.get_dummies(df, columns=['vertebrates'])
print(df2)


