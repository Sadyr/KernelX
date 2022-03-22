import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 10001
client_socket.connect((ip,port))

#welcome = client_socket.recv(1024).decode()
#print(welcome)
while True:
    #mes = input()
    #client_socket.send(mes.encode())
    peres = client_socket.recv(1024).decode()
    #print(mes)
    print(peres)
#client_socket.close()
