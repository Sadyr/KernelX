import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

username = input()
sock.connect(('', 10000))
sock.send(username.encode())


def after_connection_to_server(server_socket):
    welcome_msg_from_server = server_socket.recv(1024).decode()
    if len(welcome_msg_from_server) > 0:
        return print(f'Server: {welcome_msg_from_server}')

while True:
    after_connection_to_server(sock)
