import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('89.219.32.27',55000))
sock.send(bytes('Hello, world', encoding = 'UTF-8'))
data = sock.recv(1024)
sock.close()
print(data)







#
# HABR
# import socket
#
# sock = socket.socket()
# sock.connect(("89.219.32.27", 9090))
# sock.send(bytes('Hello, world Sadyr aka', encoding = 'UTF-8'))
# data = sock.recv(1024)
# sock.close()
#
# print(data)
