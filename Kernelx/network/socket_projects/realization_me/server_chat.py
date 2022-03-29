import socket
import threading
import logging

# _________________________________CREATE SERVER_SOCKET_____________________________________
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '127.0.0.1'
port = 1032
server_socket.bind((ip, port))
server_socket.listen(5)

# ________________def dog LOGS _________________________________________

# def logs_server(filelog, text_to_log, logging_level):
#     format_logs = '%(asctime)s - %(message)s '
#     logging.basicConfig(filename=filelog, filemode='a', format=format_logs,
#                         level=logging_level)
#     logging.info(text_to_log)

client_socket_set = set()


def listen_for_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
        except Exception:
            client_socket_set.remove(client_socket)
        for client_socket in client_socket_set:
            client_socket.send(('Пересланное сообщение' + message).encode())
        print(message)
        print('done ')


while True:
    try:
        client_socket, client_address = server_socket.accept()
        print(f'Клиент под адресом {client_address} подключился')
        # logs_server('connect.log', 'Client to connection server', logging_level=logging.INFO)
        client_socket_set.add(client_socket)
    except Exception:
        server_socket.close()
    print(client_socket_set)
    t = threading.Thread(target=listen_for_client, args=(client_socket,))
    t.daemon = True
    t.start()
