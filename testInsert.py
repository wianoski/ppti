import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='fingerLog',
                                         user='wianoski',
                                         password='')

    mySql_insert_query = """INSERT INTO log_finger (finger_id, finger_number, finger_time) 
                           VALUES 
                           (NULL, '42',NULL) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_insert_query)
    connection.commit()
    print("Record inserted successfully into ")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into  {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")