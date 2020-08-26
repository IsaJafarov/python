import paramiko

IP='40.89.179.218'
USERNAME='gismat'
PASSWORD='CrbnTechIndream2019'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(IP, username=USERNAME, password=PASSWORD)


ftp_client = ssh_client.open_sftp()
ftp_client.get('/home/gismat/db_dump.sql','/home/isa/Desktop/coming_file.sql')
ftp_client.close()