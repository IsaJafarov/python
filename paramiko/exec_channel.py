import paramiko
import time

def execute_command(command):
    print('>>> {} <<<\n'.format(command))
    stdin,stdout,stderr = client.exec_command(command)
    for line in stdout.readlines(): 
        print(line )


IP='40.89.179.218'
PORT='22'
USERNAME='gismat'
PASSWORD='CrbnTechIndream2019'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect(IP, username=USERNAME, password=PASSWORD)
print('\nconnection established\n')

execute_command('ifconfig')

execute_command('ls -la')
