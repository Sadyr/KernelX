# example3 tcp (tcp server socket)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)


def receive_msg_from_client(client_address, client_username):  # Функция для приема сообщений от клиента
    message = client_address.recv(1024).decode()
    return f'{client_username}:{message}'


def sender_msg_to_client(client_address, client_username, text):  # Отправка сообщений клиенту
    message = client_address.send(text.encode())
    return f'Сообщение отправлено {client_username}: {text}'


def welcome_msg_to_client(client_address):
    client_username = client_address.recv(1024).decode()
    welcome_msg = f' Добро пожаловать в чат {client_username} '.encode()
    client_address.send(welcome_msg)
    connect_message = f'{client_username} подключился'
    return client_username, connect_message


while True:
    try:
        print('Сервер ожидает соединения . . .')
        client, addr = sock.accept()
        client_username, connect_msg = welcome_msg_to_client(client)
        print(connect_msg)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        while True:
            msg_from_client = receive_msg_from_client(client, client_username)
            if len(msg_from_client) > 0:
                print(msg_from_client)
            else:
                continue

set_clients = ()
while True:
    client_socket, client_address = sock.accept()
    print(f"+ Клиент с адресом подключился {client_address}")
    set_clients.add(client_socket)





