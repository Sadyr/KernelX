import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')
while True:
    conn,addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    conn.send(data.upper())
conn.close()







# import socket
# HABR
# sock = socket.socket()
# sock.bind(('', 9090))
# sock.listen(1)
# conn, addr = sock.accept()
# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
#     conn.send(data.upper())
# conn.close()

