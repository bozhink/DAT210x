# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')

sql_dataframe  = pd.read_sql_table('my_table', engine, columns=['ColA', 'ColB'])
xls_dataframe  = pd.read_excel('my_dataset.xlsx', 'Sheet1', na_values=['NA', '?'])

json_dataframe = pd.read_json('my_dataset.json', orient='columns')

csv_dataframe  = pd.read_csv('my_dataset.csv', sep=',')
table_dataframe= pd.read_html('http://page.com/with/table.html')[0]

df = pd.read_csv('my_dataset.csv', sep=',')

# Writing an existing dataframe to disk is just as straightforward:
df.to_sql('table', engine)
df.to_excel('dataset.xlsx')
df.to_json('dataset.json')
df.to_csv('dataset.csv')

# If you do have column titles already defined in your dataset but wish to rename them, in that case, use the writeable .columns property:
df.columns = ['new', 'column', 'header', 'labels']

df.head(5)
df.describe()
df.columns
df.index

# View Column DataTypes
df.dtypes
