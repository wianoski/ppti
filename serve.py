import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 3040))
    s.listen()
    conn, addr = s.accept()
    print("Waiting connection....")
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            data.decode('utf-8')
            if not data:
                break
            # conn.sendall(data)
            print('you got data: ',data)
    print("Over")