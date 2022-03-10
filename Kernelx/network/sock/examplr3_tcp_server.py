# example3 tcp (tcp server socket)
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8877))
sock.listen(5)


def recieve_msg(client_machine):  # Функция для приема сообщений от клиента
    message = client_machine.recv(1024).decode()
    return f'{username_client}:{message}'


def sender_msg(client_machine, text):  # Отправка сообщений клиенту
    message = client_machine.send(text)
    return f'Следующее сообщение отправлено клиенту: {text}'


while True:
    try:
        print('Сервер ожидает соединения . . .')
        client, addr = sock.accept()

    except KeyboardInterrupt:
        sock.close()
        break
    else:
        username_client = client.recv(1024).decode()
        text = f' Добро пожаловать в чат {username_client} '.encode()
        sender_msg(client, text)
        print(f'{username_client} подключился')
    while True:
        message_from_client = recieve_msg(client)
        if len(message_from_client) > len(username_client)+1:
            print(message_from_client)



        #client.close()
        #print('Сокет закрыт')
        #break
