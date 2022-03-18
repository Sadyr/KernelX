# example 1

import socket

# create tcp socket client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# connecting in port 8888
def after_connection_to_server(server_socket):  # данная функция получает первое сообщение от сервера при подключении к серверу
    welcome_msg_from_server = server_socket.recv(1024).decode()
    if len(welcome_msg_from_server) > 0:
        return print(f'Server: {welcome_msg_from_server}')


def send_msg_to_server(server_socket, message):
    sender = server_socket.send(message.encode())
    print(f"You: {message}")


def receive_msg_from_server(server_socket):
    msg_from_server = server_socket.recv(1024).decode()
    return f'Server: {msg_from_server}'


username = socket.gethostname()
sock.connect(('', 8888))
sock.send(username.encode())
after_connection_to_server(sock)

while True:
    msg = input()
    if len(msg) > 0:
        send_msg_to_server(sock, msg)
    else:
        continue








