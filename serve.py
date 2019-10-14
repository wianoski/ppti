import socket
import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode



def insertData(data):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='fingerLog',
                                            user='wianoski',
                                            password='')

        queryInsert = """INSERT INTO log_finger (finger_id, finger_number, finger_time) VALUES (NULL, """+ data +""", NULL)"""


        cursor = connection.cursor()
        result = cursor.execute(queryInsert)
        connection.commit()
        print("Record inserted successfully into db")
        # cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into  {}".format(error))



print("Waiting for all connection....")
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
            insertData(this.decode("utf-8"))

            f = open("data.txt", 'w')
            f.write(this.decode("utf-8"))

    print("Over")
    # print(data)