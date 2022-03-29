import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 1032
client_socket.connect((ip, port))


def listen_for_message():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

t = threading.Thread(target=listen_for_message)
t.daemon = True
t.start()

# welcome = client_socket.recv(1024).decode()
# print(welcome)
while True:
    your_mes_for_chat = input()
    client_socket.send(your_mes_for_chat.encode())
    print(your_mes_for_chat)


# client_socket.close()
