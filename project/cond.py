# # download modsim.py if necessary
import modsim
# from os.path import basename, exists
#
# def download(url):
#     filename = basename(url)
#     if not exists(filename):
#         from urllib.request import urlretrieve
#         local, _ = urlretrieve(url, filename)
#         print('Downloaded ' + local)
#
# download('https://github.com/AllenDowney/ModSimPy/raw/master/' +
#          'modsim.py')
# print('k')

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy

def make_system(T_init, volume, r, t_end):
    return modsim.System(T_init=T_init,
                  T_final=T_init,
                  volume=volume,
                  r=0.01,
                  t_end=t_end,
                  T_env=22,
                  t_0=0,
                  dt=1)

def change_func(t, T, make_system):
    r= 0.01
    T_env = 22
    dt = 1
    return -r * (T - T_env) * dt

t_array = modsim.linrange(0,30,1)

series = modsim.TimeSeries(index=t_array)
s = series.iloc[0] = 90
print(series)
print(s)
n = 30
for i in range(n-1):
    t = t_array[i]
    T = series.iloc[i]
    b = series.iloc[i+1] = T + change_func(t, T, make_system)
    print(b)
print(series)
#df = pd.DataFrame(t_arrays)
#print(df)
#print(s)
# print(s)
# print(series)
