import paramiko
import re
import time

IP='40.89.179.218'
PORT='22'
USERNAME='gismat'
PASSWORD='CrbnTechIndream2019'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(IP, username=USERNAME, password=PASSWORD)

while True:
    response = client.exec_command('top')
    cpu = re.search(b'%Cpu\(s\):(s\)+(.+?)(\s)+us', response)
    print('cpu = {}'.format(cpu))
    util = cpu.group(2).decode('UTF-8')

    with open('./cpu-data.txt','a') as cpufile:
        cpufile.write(utl+'\n')
    time.sleep(5)
