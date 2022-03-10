# example 1

import socket
# create tcp socket client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting in port 8888
username = 'Sadyr'
sock.connect(('', 8877))
sock.send(username.encode())


while True:
    msg_from_server = sock.recv(1024).decode()
    if len(msg_from_server) == 0:
        continue
    else:
        print(f'Сообщение от сервера: {msg_from_server}')
    while True:
        message_to_server = input()
        msg_to_server = message_to_server.encode()
        sock.send(msg_to_server)
        continue

# close socket connection
#sock.close()


