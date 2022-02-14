import socket

from past.builtins import raw_input

client_socket = socket.socket()
port = 12345
client_socket.connect(('89.219.32.27',port))

recv_msg = client_socket.recv(1024)
print(recv_msg)

send_msg = raw_input(b'Enter your user name (prefix with #):')
client_socket.send(send_msg)

while True:
    recv_msg = client_socket.recv(1024)
    print(recv_msg)
    send_msg = raw_input(b"Send your message in format [@user:message] ".encode())
    if send_msg == b'exit':
        break

    else:
        client_socket.send(send_msg)
client_socket.close()
