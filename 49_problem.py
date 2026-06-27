import numpy as np

today = np.datetime64('today')

days= today + np.timedelta64(7, 'D')
week = today + np.timedelta64(2, 'W')
year = today + np.timedelta64(365, 'D')

print("After 7 days:", days)
print("After 2 Week:", week)
print("After 1 year:", year)