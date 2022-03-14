import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 10000))
sock.listen(5)

set_clients = set()

while True:
    try:
        client_socket, client_address = sock.accept()
        client_username = client_socket.recv(1024).decode()
        welcome_msg = f' Добро пожаловать в чат {client_username} '.encode()
        client_socket.send(welcome_msg)
        connect_message = f'{client_username} подключился'
        set_clients.add(client_username)
        print(set_clients)
    except Exception:
        sock.close()
        break



