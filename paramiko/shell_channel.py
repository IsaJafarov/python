import paramiko
import time

def edit_response(raw_response):
    return str(raw_response).replace('\\r\\n','\n')

IP='40.89.179.218'
PORT='22'
USERNAME='gismat'
PASSWORD='CrbnTechIndream2019'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect(IP, username=USERNAME, password=PASSWORD)
print('\nconnection established')

channel = client.invoke_shell()
print('\nchannel created ')

time.sleep(4)
print(edit_response(channel.recv(65535)), end='\n')

print('---')

sentBytes = channel.send("pwd\n")
time.sleep(2)
print( edit_response(channel.recv(65535)) )

print('---')

sentBytes = channel.send("mkdir test\n")
time.sleep(2)
print( edit_response(channel.recv(65535)) )

print('---')

sentBytes = channel.send("ls\n")
time.sleep(2)
print( edit_response(channel.recv(65535)) )


channel.close()
print('channel closed')