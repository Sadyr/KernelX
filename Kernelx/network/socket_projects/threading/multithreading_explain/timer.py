import time
from threading import Thread


def remind():
    print("О чем Вам напомнить?")
    text = str(input())
    print("Через сколько минут?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print(text)


# Create a new thread
th = Thread(target=remind, args=())
th.start()
# running a new thread
time.sleep(20)
print("Пока поток работает, мы можем сделать что-нибудь еще")
