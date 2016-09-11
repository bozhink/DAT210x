# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 22:43:08 2016

@author: bozhin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(1000, 5),
                  columns=['a', 'b', 'c', 'd', 'e'])
print df.corr()

plt.imshow(df.corr(),
           cmap=plt.cm.Blues,
           interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks,
           df.columns,
           rotation='vertical')
plt.yticks(tick_marks,
           df.columns)

plt.show()
