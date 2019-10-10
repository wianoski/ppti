import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 3030))

msg = 'Kono dio da'
but = msg.encode()
client.send(but)
from_server = client.recv(4096)
client.close()
