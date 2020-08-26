import socket

INDREAM_SERVER = '40.89.179.218'
TURKIYEDENAL_SERVER='157.230.110.170'
TEST_SERVER='dev1.crbn.az'
ports = [21, 22, 25, 3306]
#ports = [ 3306]
print()

for port in ports:
    try:
        s = socket.socket()
        print('banner for port: {}'.format(port))
        s.connect((INDREAM_SERVER, port))
        response = s.recv(1024)
        print('response: {}'.format(response))
        print()
        s.close()
    except TimeoutError as e:
        print('sorry. couldn\'t connect :( port may be closed')

