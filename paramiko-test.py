import paramiko
import time

username = 'gismat'
ip = '40.89.179.218'
password = 'CrbnTechIndream2019'
cmd_command_1 = 'show ip int brief'

try:
    # log in
    session = paramiko.SSHClient()

    # auto accept unknown host keys
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    print('connect...')
    # connect
    session.connect(ip, username=username, password=password)

    print('invoke shell...')
    # start an interactive shell
    connection = session.invoke_shell()
    time.sleep(2)
    #welcome = str(connection.recv(65535))
    #welcome = welcome.replace('\\r\\n','\n')
    #print( welcome )

    # set terminal length for entire output - disable pagination
    #connection.send("enable\n")
    #connection.send("terminal length 0\n")
    #time.sleep(1)

    #connection.send(cmd_command_1+"\n")
    #time.sleep(2)

    #while True:
     #   command = input('\nEnter command: ')
      #  connection.send(command+'\n')
       # time.sleep(2)
        #print(str(connection.recv(65535)).replace('\\r\\n','\n'))
    connection.send('ls -l\n')
    connection.send('pwd\n')
    connection.send('ifconfig\n')
    time.sleep(1)
    output = print(str(connection.recv(65535)).replace('\\r\\n','\n'))
    print(output)

    time.sleep(2)   
    print('\n*********************\n')
    output = print(str(connection.recv(65535)).replace('\\r\\n','\n'))
    print(output)
    session.close()
except paramiko.AuthenticationException:
    print('username or password is invalid')