import socket
import json

print("Waiting connection....")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 3040))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            data.decode(encoding="utf-8")
            if not data:
                break
            # conn.sendall(data)
            this = data
            # this = data
            print('you got data: ',this.decode("utf-8"))

            f = open("data.txt", 'w')
            f.write(this.decode("utf-8"))

    print("Over")
    # print(data)