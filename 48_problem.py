# How to get the dates of yesterday, today and tomorrow?
import numpy as np

today = np.datetime64('Today')
yesterday = today - np.timedelta64(1,'D')
tomarrow = today + np.timedelta64(1,'D')

print("Yesterday:",yesterday)
print('Today:',today)
print('Tomarrow:',tomarrow)