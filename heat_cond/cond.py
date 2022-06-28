import modsim
import  time
from threading import Thread
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys

#sys.stdout = open('file.txt', 'w')
#print('test')

def make_system(T_init, volume, r, t_end,T_env):
    return modsim.System(T_init=T_init,
                  T_final=T_init,
                  volume=volume,
                  r=r,
                  t_end=t_end,
                  T_env=T_env,
                  t_0=0,
                  dt=1)

def func(x):
    return (x-1) * (x-2) * (x-3)

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


T_init = 90
T_final = 70
volume = 300
t_end = 30
T_env = 22
t_0 = 0
dt = 1
r=0.0115

coffee = make_system(T_init=T_init, volume=volume, r=r, t_end=t_end, T_env=T_env)
tea = make_system(T_init=65, volume=300, r=0.01, t_end=40, T_env=22)

start_time_res1 = time.time()
results_coffee = run_simulation(coffee, change_func)
finish_time_res1 = time.time()
time_res1 = finish_time_res1-start_time_res1

start_time_res2= time.time()
results_tea = run_simulation(tea, change_func)
finish_time_res2 = time.time()
time_res2 = finish_time_res2-start_time_res2

time_proc = time.time()
thread1 = Thread(target=run_simulation, args=(make_system(T_init=90, volume=300, r=0.01, t_end=30, T_env=22), change_func))
thread2 = Thread(target=run_simulation, args=(make_system(T_init=65, volume=300, r=0.01, t_end=40, T_env=22), change_func))
thread1.start()
thread2.start()
res = thread1.join()
res2 = thread2.join()
time_proc2 = time.time()

result_lin = time_res2+time_res1
lin = result_lin*1000
result_par = time_proc2-time_proc
par=result_par*1000

print('Мақсаты:')
print("Стакандағы ыстық коффе немесе шайдың  жылуының қоршаған ортаға тарауына байланысты температурының ұақытқа байланысты өзгерісін анықтау үшін дифференициалды теңдеуді шешуге арналған алгоритмді құру:")
print('Құрылған алгоритмді тізбектей және паралельді орындау арқылы салыстыру, нәтижелерін бекіту:)')
print()
print("Функцияның параметрлеріне берілетін аргументтер кестесі")
print()

print(''' 
T_init : Бастапқы температура
T_final : Соңғы температура
volume: Көлемі
t_end: Толык өту уаұыты
T_env: Қоршаған орта температурасы
t_0 : Уақыт бойынша санақ бастау мезеті
dt : Уақыт қадамы
r: нысандар арасында жыду алмасу коэфиценті, тұраұты шама
''')
dota_teams = ["T_init", "T_final", "volume", "time_end", "T_env", 't_0',"dt","r"]
dota_team = ["Coffe", "Tea"]
data = [[T_init, T_final, volume, t_end,T_env, t_0  , dt, r],
[65, T_final, volume, 40,T_env, t_0  , dt, r]]
format_row = "{:>12}" * (len(dota_teams) + 1)
print(format_row.format("", *dota_teams))
for team, row in zip(dota_team, data):
    print(format_row.format(team, *row))
print()
print('Екі функцияны тізбектей және паралельді орындалу уақыттарыңың нәтижелері;')
dota_teams = ["Тiзбектей", "Паралельдi"]
dota_team = ["Уакыты (мс)"]
data = [[round(lin), round(par)]]
format_row = "{:>12}" * (len(dota_teams) + 1)
print(format_row.format("", *dota_teams))
for team, row in zip(dota_team, data):
    print(format_row.format(team, *row))
print()
print()
print('Коффенің параметрлерінің мәндері  берілген дифферциалды теңдеудің нәтижесі: ')
results_coffee.index.name= 'Уакыт'
results_coffee = results_coffee.reset_index(name='Температурасы')
print('Тізбектің алғашқы 5-нітиже:')
print(results_coffee.head(5))
print('Тізбектің соңғы 5-нәтиже:')
print(results_coffee.tail(5))
print()

print('Шайдың параметрлерінің мәндері  берілген дифферциалды теңдеудің нәтижесі: ')
results_tea.index.name= 'Уакыт'
results_tea = results_tea.reset_index(name='Температурасы')
print('Тізбектің алғашқы 5-нітиже:')
print(results_tea.head(5))
print('Тізбектің соңғы 5-нәтиже:')
print(results_tea.tail(5))
#sys.stdout.close()


