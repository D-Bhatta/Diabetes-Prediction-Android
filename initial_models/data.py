import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling

#read the data
diabetes = pd.read_csv('diabetes.csv')
print(diabetes.columns)
diabetes.head()
print(diabetes.groupby('Outcome').size())
diabetes.info()

#seaborn count plot
count_plot = sns.countplot(x=diabetes['Outcome'],label="Count",data=diabetes)
fig = count_plot.get_figure()
fig.savefig('output.png') 

#profile the data
#pfrep=pandas_profiling.ProfileReport(diabetes)
#pfrep.to_file('./profile_report.html')