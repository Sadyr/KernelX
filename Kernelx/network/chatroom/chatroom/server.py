import socket
from threading import Thread
import datetime


# server's IP address
SERVER_HOST = "0.0.0.0"
print(f"Адрес текущего сервера {SERVER_HOST}")
SERVER_PORT = 5002 # port we want to use
print(f"Порт для соедтинение текущего сервера {SERVER_PORT}")

separator_token = "<SEP>" # we will use this to separate the clietn name & message

# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
print(f"Создан сокет{s}")
# make hte port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
print(f"Делаем сокет многоразовым{s}")
s.bind((SERVER_HOST, SERVER_PORT))
print(f"Прикрепляем за сокетом  {s} IP  и PORT")
# listen for upcoming connection
s.listen(5)
print(f"Слушаем сокет  {s} ")
print(f"[*] lisstening as {SERVER_HOST}:{SERVER_PORT}")

print(" Создаем функцию для слушание клиентов")
def listen_for_client(cs,client_address):
    """
    THis function keep listening for a message from "cs" socket
    Whenever a message is received, broadcast it to all other connected clietns
    """
    while True:
        try:
            # keep listening for a message from 'cs' socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connection
            # remove it from is the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a message, replace the "SEP"
            # token with ": " for nice printing
            msg = msg.replace(separator_token, ": ")
            if len(msg) > 0:
                msg_logs = open('msg_logs', 'a')
                msg_logs.write(str(client_address) + msg +'\n')
                msg_logs.close()
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg.encode())

while True:
    # we keep listening for new connection all the time
    #print(f"Собирается подключиться клиент по адресу {client_address} ")

    client_socket, client_address = s.accept()
    print(f"принимаем клиента по адресу по адресу {client_address} ")

    print(f"[+] {client_address} Подключился.")
    # add the new connected  client to connected sockets
    client_sockets.add(client_socket)

    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,client_address))
    # make the thread daemon so it ends whenever the  main thread ends
    t.daemon = True
    # start the thread
    t.start()

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close

