# # download modsim.py if necessary
import modsim
from datetime import datetime
import  time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process
import sys
from threading import Thread
# Создаем обьек system
def make_system(T_init, volume, r, t_end,T_env):
    return modsim.System(T_init=T_init,
                  T_final=T_init,
                  volume=volume,
                  r=r,
                  t_end=t_end,
                  T_env=T_env,
                  t_0=0,
                  dt=1)

# ПОИСК корня и значение r
def func(x):
    return (x-1) * (x-2) * (x-3)
res = modsim.root_scalar(func, bracket=[0.7,1.5])
print(res)

def error_func(r, system):
    system.r = r
    results = run_simulation(system, change_func)
    return make_system.T_final - 70

def change_func(t, T, make_system):
    r, T_env, dt = make_system.r, make_system.T_env, make_system.dt
    return -r * (T - T_env) * dt

def run_simulation(make_system, change_func):
    t_array = modsim.linrange(make_system.t_0, make_system.t_end, make_system.dt)
    n = len(t_array)

    series = modsim.TimeSeries(index=t_array)
    series.iloc[0] = make_system.T_init

    for i in range(n-1):
        t = t_array[i]
        T = series.iloc[i]
        series.iloc[i+1] = T + change_func(t, T, make_system)

    make_system.T_final = series.iloc[-1]
    return (series)
# Задается следующие параметры
T_init = 90 #начальная температура кофе
T_final = 70 # Конечная температура
volume = 300 #обьем жидкости
t_end = 30 # время процесса
T_env = -25 #температура окр среду
t_0 = 0 #Начальная временная метка
dt = 1 #Временной шаг
r= 0.01 #r - константа, характерезующая скорость передачи тепла между обектом и окр средой

coffee = make_system(T_init=90, volume=300, r=0.01, t_end=30, T_env=22)
tea = make_system(T_init=90, volume=300, r=0.01, t_end=60, T_env=22)
# Запуск последовательно двух функций

start_time_res1 = time.time()
results_coffee = run_simulation(coffee, change_func)
finish_time_res1 = time.time()
time_res1 = finish_time_res1-start_time_res1

start_time_res2= time.time()
results_tea = run_simulation(tea, change_func)
finish_time_res2 = time.time()
time_res2 = finish_time_res2-start_time_res2

result_lin = time_res2+time_res1 # Время выполнение двух функций последовательно
print(result_lin)
print('Выполнено линейно')

time_proc = time.time()
thread1 = Thread(target=run_simulation, args=(make_system(T_init=90, volume=300, r=0.01, t_end=30, T_env=22), change_func))
thread2 = Thread(target=run_simulation, args=(make_system(T_init=90, volume=300, r=0.01, t_end=60, T_env=22), change_func))
thread1.start()
thread2.start()
res = thread1.join()
res2 = thread2.join()
time_proc2 = time.time()

result_par = time_proc2-time_proc # Время выполнение паралельной функции
print(result_par)
print('Выполнено паралельно')

#print(results)
#print(results2)

# plt.plot(results_tea)
# plt.plot(results_coffee)

# modsim.decorate(xlabel='Time (minute)',
#          ylabel='Temperature (C)',
#           title='Coffee Cooling')
#
# # # create data
# # x = [10,20,30,40,50]
# # y = [30,30,30,30,30]
#
# # plot line
# # plt.plot(x, y)
# plt.show()


x = [1,2,3,4,5]
y = [3,3,3,3,3]

# plot lines
#plt.plot(x, y, label = "coffe")
#plt.plot(y, x, label = "tea")
plt.plot(results_coffee,  label = "coffee")
plt.plot(results_tea,  label = "tea")
plt.legend()
plt.show()
