import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import datetime as dt 
plt.rcParams["axes.unicode_minus"]=False

data = pd.read_csv('data.csv')

print data.head()

data.plot(figsize=(10,6))
plt.ylabel('zhangdiefu')
plt.show()