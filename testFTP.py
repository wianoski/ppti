from ftplib import FTP
import os

host = "10.30.40.23"
uname = "biofarma_server"
upass = "biofarmasofun"

ftp = FTP()
connect_server = ftp.connect(host=host, port=21, timeout=None)
print(connect_server)
login_status = ftp.login(user=uname, passwd=upass)
print(login_status)