import socket

TCP_IP='192.168.0.118'
TCP_PORT=6996
BUFFER_SIZE=100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)

conn,addr = s.accept()
print('connection address: {}'.format(addr))

while True:
    data=conn.recv(BUFFER_SIZE)
    if not data:
        break;
    print('received data: {}'.format(data))
    conn.send(data)

conn.close



