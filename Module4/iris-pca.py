# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from pandas.tools.plotting import andrews_curves
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')
# If the above line throws an error, use plt.style.use('ggplot') instead

# Load up SKLearn's Iris Dataset into a Pandas Dataframe
data = load_iris()
df = pd.DataFrame(data.data,
                  columns=data.feature_names)
df['target_names'] = [data.target_names[i] for i in data.target]

# Andrews Curves Start Here:
plt.figure()
andrews_curves(df, 'target_names')
plt.show() 


# PCA
df.drop(['target_names'], axis=1, inplace=True)

pca = PCA(n_components=2)
pca.fit(df)
T = pca.transform(df)

print df.shape
print T.shape

plt.plot(T)
plt.show()

plt.scatter(T[:,0], T[:,1], c='r', marker='>')
plt.show()

