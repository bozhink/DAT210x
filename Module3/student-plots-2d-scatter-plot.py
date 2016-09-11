# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 21:50:34 2016

@author: bozhin
"""
import pandas as pd
import matplotlib

matplotlib.style.use('ggplot') # Look Pretty

# If the above line throws an error, use plt.style.use('ggplot') instead


student_dataset = pd.read_csv("Datasets/students.data", index_col=0)
student_dataset.plot.scatter(x='G1', y='G3')
